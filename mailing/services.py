from apscheduler.schedulers.background import BackgroundScheduler
from mailing.models import Client, MailingSettings, MailingAttempt


def mailing_sending():
    print("Рассылка отправилась")


def start_scheduler():
    scheduler = BackgroundScheduler()

    if not scheduler.get_jobs():
        scheduler.add_job(mailing_sending, 'interval', seconds=20)

    if not scheduler.running:
        scheduler.start()
