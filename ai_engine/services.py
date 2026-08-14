from datetime import date

from projects.models import Project
from tasks.models import Task
from dpr.models import DailyProgressReport
from django.utils import timezone



def project_completion_risk(project_id):
    project = Project.objects.get(id=project_id)

    tasks = Task.objects.filter(project=project)

    total_tasks = tasks.count()
    completed_tasks = tasks.filter(status="COMPLETED").count()

    if total_tasks == 0:
        task_completion = 0
    else:
        task_completion = (completed_tasks / total_tasks) * 100

    reports = DailyProgressReport.objects.filter(
        task__project=project
    ).order_by("-report_date")

    if reports.exists():
        latest_progress = reports.first().progress_percentage
    else:
        latest_progress = 0

    risk_score = 0

    if task_completion < 50:
        risk_score += 40
    elif task_completion < 75:
        risk_score += 20

    if latest_progress < 50:
        risk_score += 30
    elif latest_progress < 75:
        risk_score += 15

    if risk_score >= 50:
        risk_level = "HIGH"
    elif risk_score >= 25:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "project_id": project.id,
        "project_name": project.project_name,
        "task_completion": round(task_completion, 2),
        "latest_progress": latest_progress,
        "risk_score": risk_score,
        "risk_level": risk_level,
    }


from decimal import Decimal

from contractors.models import Contractor
from billing.models import Billing


def project_cost_overrun_risk(project_id):
    project = Project.objects.get(id=project_id)

    contractors = Contractor.objects.filter(site=project.site)

    contract_value = sum(
        (contractor.contract_value for contractor in contractors),
        Decimal("0")
    )

    total_billed = sum(
        (billing.amount for billing in Billing.objects.filter(project=project)),
        Decimal("0")
    )

    if contract_value > 0:
        financial_progress = (
            total_billed / contract_value
        ) * 100
    else:
        financial_progress = Decimal("0")

    reports = DailyProgressReport.objects.filter(
        task__project=project
    ).order_by("-report_date")

    if reports.exists():
        physical_progress = reports.first().progress_percentage
    else:
        physical_progress = 0

    variance = float(financial_progress) - float(physical_progress)

    if variance >= 20:
        risk_level = "HIGH"
    elif variance >= 10:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return {
        "project_id": project.id,
        "project_name": project.project_name,
        "contract_value": float(contract_value),
        "total_billed": float(total_billed),
        "financial_progress": round(float(financial_progress), 2),
        "physical_progress": physical_progress,
        "variance": round(variance, 2),
        "risk_level": risk_level,
    }


from materials.models import Material


def material_stock_analysis(project_id):
    materials = Material.objects.filter(project_id=project_id)

    results = []

    for material in materials:
        quantity = float(material.quantity)
        minimum_stock = float(material.minimum_stock)

        if quantity <= minimum_stock:
            status = "LOW"
        else:
            status = "ADEQUATE"

        results.append({
            "material_id": material.id,
            "material_name": material.material_name,
            "quantity": quantity,
            "unit": material.unit,
            "minimum_stock": minimum_stock,
            "status": status,
        })

    return {
        "project_id": project_id,
        "materials": results,
    }

from django.db.models import Count, Avg
from labour.models import Labour
from projects.models import Project


def labour_requirement_prediction(project_id):
    project = Project.objects.get(id=project_id)

    labour_records = Labour.objects.filter(
        task__project_id=project_id
    )

    role_data = (
        labour_records
        .values("role")
        .annotate(
            workers=Count("id", distinct=True),
            avg_hours=Avg("hours_worked"),
        )
    )

    results = []

    for role in role_data:
        role_name = role["role"]
        current_workers = role["workers"]
        avg_hours = round(float(role["avg_hours"] or 0), 2)

        # Heuristic:
        # Each active task assigned to a role represents
        # one expected worker requirement.
        active_tasks = labour_records.filter(
            role=role_name,
            task__status__in=["PENDING", "IN_PROGRESS"]
        ).values("task_id").distinct().count()

        required_workers = max(active_tasks, 1)
        difference = current_workers - required_workers

        if difference < 0:
            status = "SHORTFALL"
        elif difference > 0:
            status = "SURPLUS"
        else:
            status = "ADEQUATE"

        results.append({
            "role": role_name,
            "current_workers": current_workers,
            "estimated_required_workers": required_workers,
            "difference": difference,
            "average_hours_worked": avg_hours,
            "status": status,
        })

    return {
        "project_id": project.id,
        "project_name": project.project_name,
        "labour_forecast": results,
    }

from django.utils import timezone


def delay_prediction(project_id):
    project = Project.objects.get(id=project_id)

    tasks = Task.objects.filter(project=project)

    results = []

    today = timezone.localdate()

    for task in tasks:
        if task.due_date:
            days_remaining = (task.due_date - today).days
        else:
            days_remaining = None

        if task.status == "DONE":
            risk_level = "LOW"
            reason = "Task is completed."

        elif days_remaining is not None and days_remaining < 0:
            risk_level = "HIGH"
            reason = "Task is overdue and not completed."

        elif (
            days_remaining is not None
            and days_remaining <= 7
            and task.status == "TODO"
            and task.priority == "HIGH"
        ):
            risk_level = "HIGH"
            reason = (
                "High-priority task is not started and is due within 7 days."
            )

        elif (
            days_remaining is not None
            and days_remaining <= 7
            and task.status == "TODO"
        ):
            risk_level = "MEDIUM"
            reason = "Task is not started and is due within 7 days."

        else:
            risk_level = "LOW"
            reason = "Task is currently on track."

        results.append({
            "task_id": task.id,
            "task_name": task.task_name,
            "status": task.status,
            "priority": task.priority,
            "due_date": task.due_date,
            "days_remaining": days_remaining,
            "risk_level": risk_level,
            "reason": reason,
        })

    return {
        "project_id": project.id,
        "project_name": project.project_name,
        "delay_risk": results,
    }
def material_requirement_forecast(project_id):
    materials = Material.objects.filter(project_id=project_id)

    results = []

    for material in materials:
        quantity = float(material.quantity)
        minimum_stock = float(material.minimum_stock)

        if quantity < minimum_stock:
            shortage = minimum_stock - quantity
            status = "SHORTAGE"
        else:
            shortage = 0
            status = "ADEQUATE"

        results.append({
            "material_id": material.id,
            "material_name": material.material_name,
            "current_quantity": quantity,
            "unit": material.unit,
            "minimum_stock": minimum_stock,
            "estimated_requirement": minimum_stock,
            "shortage_quantity": shortage,
            "status": status,
        })

    return {
        "project_id": project_id,
        "materials": results,
    }
def dpr_progress_analysis(project_id):
    project = Project.objects.get(id=project_id)

    reports = (
        DailyProgressReport.objects
        .filter(task__project=project)
        .select_related("task")
        .order_by("-report_date")
    )

    results = []

    for report in reports:
        progress = report.progress_percentage

        if progress < 30:
            progress_status = "LOW"
        elif progress < 70:
            progress_status = "MODERATE"
        else:
            progress_status = "GOOD"

        results.append({
            "report_id": report.id,
            "task_id": report.task.id,
            "task_name": report.task.task_name,
            "report_date": report.report_date,
            "progress_percentage": progress,
            "workers_present": report.workers_present,
            "weather": report.weather,
            "progress_status": progress_status,
            "work_done": report.work_done,
            "remarks": report.remarks,
        })

    return {
        "project_id": project.id,
        "project_name": project.project_name,
        "dpr_analysis": results,
    }