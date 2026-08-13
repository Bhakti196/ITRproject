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