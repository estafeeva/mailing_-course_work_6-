from time import sleep

from django.apps import AppConfig

from config.settings import RUN_SCHEDULER


class MailingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailing"

    def ready(self):
        if RUN_SCHEDULER:
            from mailing.services import start_scheduler
            sleep(2)
            start_scheduler()
            print('scheduler started')
        else:
            print('scheduler not started')