from django.core.management import BaseCommand

from mailing.services import mailing_sending


class Command(BaseCommand):
    """Запускает отправку рассылок из командной строки"""
    def handle(self, *args, **kwargs):
        mailing_sending()
