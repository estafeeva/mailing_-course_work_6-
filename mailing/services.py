import smtplib
from datetime import datetime, timedelta

import pytz
from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler
from mailing.models import Client, MailingSettings, MailingAttempt
from django.core.mail import send_mail

from django.core.cache import cache
from config.settings import CACHE_ENABLED

def mailing_sending():
    print("Рассылка началась")
    current_datetime = get_current_datetime()


    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = MailingSettings.objects.filter(first_sent_datetime__lte=current_datetime).filter(
        status__in=[MailingSettings.STARTED, MailingSettings.CREATED])

    for mailing in mailings:
        attempts = MailingAttempt.objects.filter(mailing=mailing)
        if attempts:
            a_list = [item.last_try_sent_datetime for item in attempts]
            last_attempt_datetime = max(a_list)

            if mailing.period == MailingSettings.DAILY:
                td = timedelta(days=1)
            elif mailing.period == MailingSettings.WEEKLY:
                td = timedelta(weeks=1)
            elif mailing.period == MailingSettings.MONTHLY:
                td = timedelta(days=30)
            else:
                td = timedelta(days=0)
            new_attempt_datetime = last_attempt_datetime + td
        else:
            new_attempt_datetime = mailing.first_sent_datetime

        if new_attempt_datetime <= current_datetime:
            mailing.status = MailingSettings.STARTED
            mailing.save()

            try:
                print(f'sending "{mailing.mailing_message.topic}" to "{[client.email for client in mailing.clients.all()]}"')
                # server_response = ""

                server_response = send_mail(
                    subject=mailing.mailing_message.topic,
                    message=mailing.mailing_message.message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[client.email for client in mailing.clients.all()],
                    fail_silently=False,
                )
                MailingAttempt.objects.create(status=MailingAttempt.SUCCESS,
                                                  server_reply=server_response,
                                                  mailing=mailing, )
                print('success')
            except smtplib.SMTPException as e:
                # При ошибке почтовика получаем ответ сервера - ошибка, которая записывается в е
                MailingAttempt.objects.create(status=MailingAttempt.FAIL,
                                                  server_reply=str(e),
                                                  mailing=mailing)
                print('fail')


def start_scheduler():
    scheduler = BackgroundScheduler()

    if not scheduler.get_jobs():
        scheduler.add_job(mailing_sending, 'interval', seconds=10)

    if not scheduler.running:
        scheduler.start()


def get_current_datetime():

    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)

    return current_datetime


def get_objects_from_cache(model_, key=""):
    """Получает данные по продуктам из кэша. Если кэш пуст, получает данные из БД."""
    if not CACHE_ENABLED:
        return model_.objects.all()
    objects_ = cache.get(key)
    if objects_ is not None:
        return objects_
    objects_ = model_.objects.all()
    cache.set(key, objects_)
    return objects_