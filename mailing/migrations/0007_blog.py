# Generated by Django 4.2.2 on 2024-07-11 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0006_alter_mailingsettings_clients"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(
                        auto_created=True,
                        blank=True,
                        help_text="Введите Дату создания",
                        null=True,
                        verbose_name="Дата создания (записи в БД)",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        help_text="Введите заголовок статьи",
                        max_length=100,
                        verbose_name="Заголовок статьи",
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="slug"
                    ),
                ),
                (
                    "content",
                    models.TextField(
                        blank=True,
                        help_text="Введите текст статьи",
                        null=True,
                        verbose_name="Содержимое статьи",
                    ),
                ),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="media/photo",
                        verbose_name="Превью",
                    ),
                ),
                (
                    "is_publication",
                    models.BooleanField(default=True, verbose_name="опубликовано"),
                ),
                (
                    "views_count",
                    models.PositiveIntegerField(default=0, verbose_name="просмотры"),
                ),
            ],
            options={
                "verbose_name": "Статья",
                "verbose_name_plural": "Статьи",
                "ordering": ["title"],
            },
        ),
    ]
