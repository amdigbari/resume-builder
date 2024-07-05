from _helpers.models import TimeModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from template.models import Template

User = get_user_model()


class Resume(TimeModel):
    is_template = models.BooleanField(
        default=False,
        verbose_name=_("is template"),
        help_text=_("is resume a template"),
    )

    forked_from = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="forks",
        verbose_name=_("forked from"),
        help_text=_("resume forked from"),
    )

    template = models.OneToOneField(
        Template,
        on_delete=models.CASCADE,
        verbose_name=_("template"),
        help_text=_("resume's template"),
    )

    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("title"),
        help_text=_("resume's title"),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="resumes",
        verbose_name=_("user"),
        help_text=_("resume's user"),
    )

    is_public = models.BooleanField(
        default=False,
        verbose_name=_("is public"),
        help_text=_("is resume public"),
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "title"], name="title_must_be_unique_per_user"
            )
        ]
