import os
from celery import Celery

from celery.schedules import crontab

from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
app = Celery('app') 

############### configuração BEAT #############################
app.conf.enable_utc = False
app.conf.update(timezone = "America/Sao_Paulo") 
app.conf.beat_schedule = {
    "enviar_email":{
        "task":"evento.tasks.verificar_prazo",
        "schedule":crontab(minute='*/5')
    }
}
###############################################################

app.config_from_object('django.conf.settings', namespace="CELERY") 
app.autodiscover_tasks() 