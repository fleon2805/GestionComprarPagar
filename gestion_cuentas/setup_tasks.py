# setup_tasks.py
from django_celery_beat.models import PeriodicTask, IntervalSchedule
from cuentas.tasks import notificar_facturas  # Importa tu tarea

def setup_periodic_tasks():
    # Configura un intervalo de 1 día
    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=1,
        period=IntervalSchedule.DAYS,
    )

    # Crea la tarea periódica
    PeriodicTask.objects.get_or_create(
        interval=schedule,
        name="Notificar facturas por vencer y vencidas",
        task="cuentas.tasks.notificar_facturas",
    )
    print("Tarea periódica creada con éxito.")
