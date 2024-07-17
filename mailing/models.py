from django.db import models

from users.models import User
from pytils.translit import slugify


class Client(models.Model):
    """Клиент сервиса:
    контактный email,
    Ф. И. О.,
    комментарий.
    """
    email = models.EmailField(unique=True, verbose_name="Email")
    name = models.CharField(
        max_length=150,
        verbose_name="ФИО",
        blank=True,
        null=True,
        help_text="Введите ФИО",
    )
    comment = models.TextField(max_length=350, verbose_name="Комментарий")
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

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
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"Тема  рассылки: {self.topic}" f"Текст рассылки: {self.message}"

    class Meta:
        verbose_name = "рассылка (текст)"
        verbose_name_plural = "рассылки (текст)"


class MailingSettings(models.Model):
    """
        Рассылка (настройки):
    дата и время первой отправки рассылки;
    периодичность: раз в день, раз в неделю, раз в месяц;
    статус рассылки (например, завершена, создана, запущена).
    """
    DAILY = "Раз в день"
    WEEKLY = "Раз в неделю"
    MONTHLY = "Раз в месяц"

    PERIODICITY_CHOICES = [
        (DAILY, "Раз в день"),
        (WEEKLY, "Раз в неделю"),
        (MONTHLY, "Раз в месяц"),
    ]

    CREATED = "Создана"
    STARTED = "Запущена"
    COMPLETED = "Завершена"

    STATUS_CHOICES = [
        (COMPLETED, "Завершена"),
        (CREATED, "Создана"),
        (STARTED, "Запущена"),
    ]

    first_sent_datetime = models.DateTimeField(
        verbose_name="дата и время первой отправки рассылки",
        help_text="Укажите дату и время первой отправки рассылки",
        #        format="%d-%m-%Y %H^%M",
    )
    period = models.CharField(
        max_length=150,
        choices=PERIODICITY_CHOICES,
        verbose_name="периодичность",
        help_text="Укажите периодичность: раз в день, раз в неделю, раз в месяц",
    )
    status = models.CharField(max_length=150, choices=STATUS_CHOICES, default=CREATED, verbose_name="Статус")

     # one (text) to many (settings)
    mailing_message = models.ForeignKey(
        MailingMessage,
        null=True,
        verbose_name="Текст рассылки",
        on_delete=models.SET_NULL,
    )

    # many (clients) to many (settings)
    clients = models.ManyToManyField(Client, related_name="mailingsettings")
    owner = models.ForeignKey(
        User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        # Строковое отображение объекта
        return f"{self.mailing_message}"

    class Meta:
        verbose_name = "рассылка (настройки)"
        verbose_name_plural = "рассылки (настройки)"

        permissions = [
            (
                'can_view_mailingsettings',
                'Can view all mailingsettings'
            ),
            (
                'deactivate_mailingsettings',
                'Can deactivate mailingsettings'
            ),
        ]


class MailingAttempt(models.Model):
    """
    Попытка рассылки:
    дата и время последней попытки;
    статус попытки (успешно / не успешно);
    ответ почтового сервера, если он был.
    """
    SUCCESS = 'Успешно'
    FAIL = 'Неудача'
    ATTEMPT_STATUS = [
        (SUCCESS, 'Успешно'),
        (FAIL, 'Неудача'),
    ]

    last_try_sent_datetime = models.DateTimeField(
        verbose_name="дата и время последней попытки рассылки",
        auto_now_add=True
    )
    status = models.CharField(max_length=50, choices=ATTEMPT_STATUS, null=True, verbose_name="Статус")
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


class Blog(models.Model):
    """заголовок;
    slug (реализовать через CharField);
    содержимое;
    превью (изображение);
    дата создания;
    признак публикации;
    количество просмотров."""

    title = models.CharField(
        max_length=100,
        verbose_name="Заголовок статьи",
        help_text="Введите заголовок статьи",
    )
    slug = models.CharField(
        max_length=200,
        verbose_name="slug",
        blank=True,
        null=True,
    )
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name="Содержимое статьи",
        help_text="Введите текст статьи",
    )
    preview = models.ImageField(
        upload_to="media/photo",
        blank=True,
        null=True,
        verbose_name="Превью",
        help_text="Загрузите изображение",
    )
    created_at = models.DateField(
        auto_created=True,
        blank=True,
        null=True,
        verbose_name="Дата создания (записи в БД)",
        help_text="Введите Дату создания",
    )
    is_publication = models.BooleanField(default=True, verbose_name="опубликовано")
    views_count = models.PositiveIntegerField(default=0, verbose_name="просмотры")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"
        ordering = ["title"]
