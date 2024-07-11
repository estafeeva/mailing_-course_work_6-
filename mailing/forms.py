from django import forms
from django.forms import ModelForm
from mailing.models import Client, MailingSettings, MailingMessage


class ClientForm(ModelForm):
    """Пользователи могут создавать новых клиенто"""

    class Meta:
        model = Client
        #fields = "__all__"
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


#            field.help_text = 'Раз, два, три! Ура!'  # Выводит текст подсказки, для описания вводимых данных


class ClientModeratorForm(ModelForm):
    """Пользователи могут создавать новых клиентов"""

    class Meta:
        model = Client
        fields = "__all__"


class MailingSettingsForm(ModelForm):
    """Пользователи могут создавать новые настройки рассылки"""

    class Meta:
        model = MailingSettings
        #fields = "__all__"
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class MailingMessageForm(ModelForm):
    """Пользователи могут создавать новые сообщения для рассылки"""

    class Meta:
        model = MailingMessage
        #fields = "__all__"
        exclude = ('owner',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"