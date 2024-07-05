from _helpers.models import TimeModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from resume.models.resume import Resume
from template.models import Section


class ResumeSection(TimeModel):
    resume = models.ForeignKey(
        Resume,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name=_("resume"),
        help_text=_("section's resume"),
    )

    section = models.OneToOneField(
        Section,
        on_delete=models.CASCADE,
        verbose_name=_("section"),
        help_text=_("resume section's section"),
    )

    content = models.TextField(
        verbose_name=_("content"),
        help_text=_("resume section's content"),
    )
