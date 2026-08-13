from datetime import date

from projects.models import Project
from tasks.models import Task
from dpr.models import DailyProgressReport


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