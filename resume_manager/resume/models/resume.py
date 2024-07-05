from _helpers.models import Template
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Resume(Template):
    is_template = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name=_("is template"),
        help_text=_("is resume a template"),
    )

    forked_from = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="forks",
        db_index=True,
        verbose_name=_("forked from"),
        help_text=_("resume forked from"),
    )

    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        db_index=True,
        verbose_name=_("title"),
        help_text=_("resume's title"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="resumes",
        db_index=True,
        verbose_name=_("user"),
        help_text=_("resume's user"),
    )

    is_public = models.BooleanField(
        default=False,
        db_index=True,
        verbose_name=_("is public"),
        help_text=_("is resume public"),
    )
