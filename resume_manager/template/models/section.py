from _helpers.models import TimeModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from template.models.template import Template


class Section(TimeModel):
    template = models.ForeignKey(
        Template,
        on_delete=models.CASCADE,
        related_name="sections",
        verbose_name=_("template"),
        help_text=_("section's template"),
    )

    start_column = models.SmallIntegerField(
        verbose_name=_("start column"), help_text=_("section start column")
    )
    start_row = models.SmallIntegerField(
        verbose_name=_("start row"), help_text=_("section start row")
    )

    column_count = models.SmallIntegerField(
        verbose_name=_("column count"), help_text=_("section column count")
    )
    row_count = models.SmallIntegerField(
        verbose_name=_("row count"), help_text=_("section row count")
    )

    min_columns = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name=_("min columns"),
        help_text=_("section min columns"),
    )
    max_columns = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name=_("max columns"),
        help_text=_("section max columns"),
    )

    min_rows = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name=_("min rows"),
        help_text=_("section min rows"),
    )
    max_rows = models.SmallIntegerField(
        null=True,
        blank=True,
        verbose_name=_("max rows"),
        help_text=_("section max rows"),
    )

    is_locked = models.BooleanField(
        default=False, verbose_name=_("is locked"), help_text=_("is section locked")
    )

    class Meta:
        constraints = [
            # Max vs Min
            models.CheckConstraint(
                check=(
                    models.Q(max_columns__isnull=True)
                    | models.Q(min_columns__isnull=True)
                    | models.Q(max_columns__gte=models.F("min_columns"))
                ),
                name="section_max_columns_must_be_higher_than_min_columns",
            ),
            models.CheckConstraint(
                check=(
                    models.Q(max_rows__isnull=True)
                    | models.Q(min_rows__isnull=True)
                    | models.Q(max_rows__gte=models.F("min_rows"))
                ),
                name="section_max_rows_must_be_higher_than_min_rows",
            ),
            # Count vs Min
            models.CheckConstraint(
                check=(
                    models.Q(min_columns__isnull=True)
                    | models.Q(column_count__gte=models.F("min_columns"))
                ),
                name="section_column_count_must_be_higher_than_min_columns",
            ),
            models.CheckConstraint(
                check=(
                    models.Q(min_rows__isnull=True)
                    | models.Q(row_count__gte=models.F("min_rows"))
                ),
                name="section_row_count_must_be_higher_than_min_rows",
            ),
            # Count vs Max
            models.CheckConstraint(
                check=(
                    models.Q(max_columns__isnull=True)
                    | models.Q(column_count__lte=models.F("max_columns"))
                ),
                name="section_column_count_must_be_lower_than_max_columns",
            ),
            models.CheckConstraint(
                check=(
                    models.Q(max_rows__isnull=True)
                    | models.Q(row_count__lte=models.F("max_rows"))
                ),
                name="section_row_count_must_be_lower_than_max_rows",
            ),
        ]
