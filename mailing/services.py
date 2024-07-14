from apscheduler.schedulers.background import BackgroundScheduler
from mailing.models import Client, MailingSettings, MailingAttempt


def mailing_sending():
    print("Рассылка отправилась")
    """ zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    # создание объекта с применением фильтра
    mailings = Модель_рассылки.objects.filter(дата__lte=current_datetime).filter(
        статус_рассылки__in=[список_статусов])

    for mailing in mailings:
        try:
            server_response = send_mail(
                subject=mailing.mailing_message.title,
                message=mailing.mailing_message.message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[client.email for client in mailing.clients.all()],
                fail_silently=False
           )
           MailingAttempt.objects.create(status=MailingAttempt.SUCCESS,
                                              server_reply=server_response,
                                              mailing=mailing)
        except smtplib.SMTPException as e:
            # При ошибке почтовика получаем ответ сервера - ошибка, которая записывается в е
            Попытка рассылки.objects.create(...)"""




def start_scheduler():
    scheduler = BackgroundScheduler()

    if not scheduler.get_jobs():
        scheduler.add_job(mailing_sending, 'interval', seconds=20)

    if not scheduler.running:
        scheduler.start()
