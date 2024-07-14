from django.apps import AppConfig


class MailingConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "mailing"

    """def ready(self):
         from mailing.модуль_с_задачей import функция_старта 
         sleep(2)
         функция_старта()"""
