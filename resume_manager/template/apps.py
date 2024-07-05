from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TemplateConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "template"
    verbose_name = _("template")
