from _helpers.models import TemplateSection
from django.db import models
from django.utils.translation import gettext_lazy as _
from resume.models.resume import Resume


class ResumeSection(TemplateSection):
    resume = models.ForeignKey(
        Resume,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name="sections",
        db_index=True,
        verbose_name=_("resume"),
        help_text=_("section's resume"),
    )

    content = models.TextField(
        verbose_name=_("content"),
        help_text=_("resume section's content"),
    )
