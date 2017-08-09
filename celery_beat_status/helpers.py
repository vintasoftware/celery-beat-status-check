from celery.beat import Service
from django.utils import timezone
import datetime


def get_periodic_tasks_info():
    from celery.schedules import current_app
    schedule = Service(current_app).get_scheduler().get_schedule()
    tasks = []
    for key, entry in schedule.items():
        # entry.is_due() returns (is_due, time_in_seconds_for_next_execution)
        is_due_tpl = entry.is_due()

        next_execution = timezone.now() + datetime.timedelta(seconds=is_due_tpl[1])

        # remove delay between the timezone.now and the schedule entry due date
        next_execution = next_execution.replace(microsecond=0)

        tasks.append({
            'name': key,
            'is_due': is_due_tpl[0],
            'next_execution': next_execution
        })

    return tasks