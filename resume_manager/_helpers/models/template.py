from _helpers.models.time import TimeModel, TimeSafeDeleteModel
from django.db import models
from django.utils.translation import gettext_lazy as _


class Template(TimeSafeDeleteModel):
    DEFAULT_COLUMNS_COUNT = 12
    DEFAULT_SECTIONS_GAP = 10

    columns_count = models.SmallIntegerField(
        db_column="template_columns_count",
        default=DEFAULT_COLUMNS_COUNT,
        verbose_name=_("columns count"),
        help_text=_("template columns count"),
    )

    sections_horizontal_gap = models.SmallIntegerField(
        db_column="template_sections_horizontal_gap",
        default=DEFAULT_SECTIONS_GAP,
        verbose_name=_("sections horizontal gap"),
        help_text=_("template sections horizontal gap"),
    )
    sections_vertical_gap = models.SmallIntegerField(
        db_column="template_sections_vertical_gap",
        default=DEFAULT_SECTIONS_GAP,
        verbose_name=_("sections vertical gap"),
        help_text=_("template sections vertical gap"),
    )

    edges_horizontal_gap = models.SmallIntegerField(
        db_column="template_edges_horizontal_gap",
        default=DEFAULT_SECTIONS_GAP,
        verbose_name=_("edges horizontal gap"),
        help_text=_("template edges horizontal gap"),
    )
    edges_vertical_gap = models.SmallIntegerField(
        db_column="template_edges_vertical_gap",
        default=DEFAULT_SECTIONS_GAP,
        verbose_name=_("edges vertical gap"),
        help_text=_("template edges vertical gap"),
    )

    class Meta:
        abstract = True


# Section
class TemplateSection(TimeModel):
    start_column = models.SmallIntegerField(
        db_column="section_start_column",
        verbose_name=_("start column"),
        help_text=_("section start column"),
    )
    start_row = models.SmallIntegerField(
        db_column="section_start_row",
        verbose_name=_("start row"),
        help_text=_("section start row"),
    )

    column_count = models.SmallIntegerField(
        db_column="section_column_count",
        verbose_name=_("column count"),
        help_text=_("section column count"),
    )
    row_count = models.SmallIntegerField(
        db_column="section_row_count",
        verbose_name=_("row count"),
        help_text=_("section row count"),
    )

    min_columns = models.SmallIntegerField(
        db_column="section_min_columns",
        null=True,
        blank=True,
        verbose_name=_("min columns"),
        help_text=_("section min columns"),
    )
    max_columns = models.SmallIntegerField(
        db_column="section_max_columns",
        null=True,
        blank=True,
        verbose_name=_("max columns"),
        help_text=_("section max columns"),
    )

    min_rows = models.SmallIntegerField(
        db_column="section_min_rows",
        null=True,
        blank=True,
        verbose_name=_("min rows"),
        help_text=_("section min rows"),
    )
    max_rows = models.SmallIntegerField(
        db_column="section_max_rows",
        null=True,
        blank=True,
        verbose_name=_("max rows"),
        help_text=_("section max rows"),
    )

    is_locked = models.BooleanField(
        db_column="section_is_locked",
        default=False,
        verbose_name=_("is locked"),
        help_text=_("is section locked"),
    )

    class Meta:
        abstract = True

        constraints = [
            # Max vs Min
            models.CheckConstraint(
                check=(
                    models.Q(max_columns__isnull=True)
                    | models.Q(min_columns__isnull=True)
                    | models.Q(max_columns__gte=models.F("min_columns"))
                ),
                name="%(class)s_section_mc_gte_mc",  # section_max_columns_must_be_gte_min_columns
            ),
            models.CheckConstraint(
                check=(
                    models.Q(max_rows__isnull=True)
                    | models.Q(min_rows__isnull=True)
                    | models.Q(max_rows__gte=models.F("min_rows"))
                ),
                name="%(class)s_section_mr_gte_mr",  # section_max_rows_must_be_gte_min_rows
            ),
            # Count vs Min
            models.CheckConstraint(
                check=(
                    models.Q(min_columns__isnull=True)
                    | models.Q(column_count__gte=models.F("min_columns"))
                ),
                name="%(class)s_section_cc_gte_mc",  # section_column_count_must_be_gte_min_columns
            ),
            models.CheckConstraint(
                check=(
                    models.Q(min_rows__isnull=True)
                    | models.Q(row_count__gte=models.F("min_rows"))
                ),
                name="%(class)s_section_rc_gte_mr",  # section_row_count_must_be_gte_min_rows
            ),
            # Count vs Max
            models.CheckConstraint(
                check=(
                    models.Q(max_columns__isnull=True)
                    | models.Q(column_count__lte=models.F("max_columns"))
                ),
                name="%(class)s_section_cc_lte_mc",  # section_column_count_must_be_lte_max_columns
            ),
            models.CheckConstraint(
                check=(
                    models.Q(max_rows__isnull=True)
                    | models.Q(row_count__lte=models.F("max_rows"))
                ),
                name="%(class)s_section_rc_lte_mr",  # section_row_count_must_be_lte_max_rows
            ),
        ]
