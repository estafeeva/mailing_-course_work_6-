# Generated by Django 4.2.2 on 2024-07-14 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("mailing", "0008_mailingsettings_status_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="mailingsettings",
            options={
                "permissions": [
                    ("can_view_mailingsettings", "Can view all mailingsettings"),
                    ("deactivate_mailingsettings", "Can deactivate mailingsettings"),
                ],
                "verbose_name": "рассылка (настройки)",
                "verbose_name_plural": "рассылки (настройки)",
            },
        ),
    ]
