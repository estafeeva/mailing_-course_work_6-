from django.contrib import admin
from mailing.models import Client, Blog, MailingSettings, MailingAttempt, MailingMessage
from users.models import User


# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("email", "name", "comment", "owner")
    list_filter = ("email",)
    search_fields = ("name", "email")


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = (
        "topic",
        "message",
        "owner",
    )


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = (
        "first_sent_datetime",
        "period",
        "mailing_message",
        "owner",
    )


@admin.register(MailingAttempt)
class MailingAttemptAdmin(admin.ModelAdmin):
    list_display = (
        "last_try_sent_datetime",
        "status",
        "server_reply",
        "mailing",
    )


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "content",
        "preview",
        "created_at",
        "is_publication",
        "views_count",
    )
