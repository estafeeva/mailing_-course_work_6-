from django.db import models


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name="Email")
    name = models.CharField(
        max_length=150,
        verbose_name="ФИО",
        blank=True,
        null=True,
        help_text="Введите ФИО",
    )
    comment = models.TextField(max_length=350, verbose_name="Комментарий")

    def __str__(self):
        # Строковое отображение объекта
        return f"Клиент: {self.email}"

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"


class MailingMessage(models.Model):
    """
    Сообщение для рассылки:
    тема письма,
    тело письма.
    """

    topic = models.CharField(
        max_length=30, verbose_name="Тема письма", help_text="Введите тему письма"
    )
    message = models.CharField(
        max_length=350,
        verbose_name="Тело письма",
        help_text="Введите сообщение для рассылки",
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"Сообщение для рассылки: {self.topic}"

    class Meta:
        verbose_name = "рассылка (текст)"
        verbose_name_plural = "рассылки (текст)"


class MailingSettings(models.Model):
    first_sent_datetime = models.DateTimeField(
        verbose_name="дата и время первой отправки рассылки",
        help_text="Укажите дату и время первой отправки рассылки",
    )
    period = models.CharField(
        max_length=150,
        verbose_name="периодичность",
        help_text="Укажите периодичность: раз в день, раз в неделю, раз в месяц",
    )
    #    status = models.ForeignKey(StatusMailing, null=True, verbose_name='Статус', on_delete=models.SET_NULL)

    # one (text) to many (settings)
    mailing_message = models.ForeignKey(
        MailingMessage,
        null=True,
        verbose_name="Текст рассылки",
        on_delete=models.SET_NULL,
    )

    # many (clients) to many (settings)
    clients = models.ManyToManyField(Client)

    def __str__(self):
        # Строковое отображение объекта
        return f"Рассылка (настройки): {self.mailing_text}"

    class Meta:
        verbose_name = "рассылка (настройки)"
        verbose_name_plural = "рассылки (настройки)"


class MailingAttempt(models.Model):
    """
    Попытка рассылки:
    дата и время последней попытки;
    статус попытки (успешно / не успешно);
    ответ почтового сервера, если он был.
    """

    last_try_sent_datetime = models.DateTimeField(
        verbose_name="дата и время последней попытки рассылки"
    )
    status = models.BooleanField(null=True, verbose_name="Статус")
    server_reply = models.TextField(
        verbose_name="ответ почтового сервера", null=True, blank=True
    )

    # one (setting) to many (attempts)
    mailing = models.ForeignKey(
        MailingSettings, verbose_name="Настройка рассылки", on_delete=models.CASCADE
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"Попытка рассылки: {self.mailing}"

    class Meta:
        verbose_name = "попытка рассылки"
        verbose_name_plural = "попытки рассылок"
