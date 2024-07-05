from _helpers.models import TimeSafeDeleteModel
from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete import SOFT_DELETE_CASCADE


class Template(TimeSafeDeleteModel):
    DEFAULT_COLUMNS_COUNT = 12
    DEFAULT_SECTIONS_GAP = 10

    _safedelete_policy = SOFT_DELETE_CASCADE

    columns_count = models.SmallIntegerField(
        default=DEFAULT_COLUMNS_COUNT,
        verbose_name=_("columns count"),
        help_text=_("template columns count"),
    )

    sections_horizontal_gap = models.SmallIntegerField(
        default=DEFAULT_SECTIONS_GAP,
        verbose_name=_("sections horizontal gap"),
        help_text=_("template sections horizontal gap"),
    )
    sections_vertical_gap = models.SmallIntegerField(
        default=DEFAULT_SECTIONS_GAP,
        verbose_name=_("sections vertical gap"),
        help_text=_("template sections vertical gap"),
    )

    edges_horizontal_gap = models.SmallIntegerField(
        default=DEFAULT_SECTIONS_GAP,
        verbose_name=_("edges horizontal gap"),
        help_text=_("template edges horizontal gap"),
    )
    edges_vertical_gap = models.SmallIntegerField(
        default=DEFAULT_SECTIONS_GAP,
        verbose_name=_("edges vertical gap"),
        help_text=_("template edges vertical gap"),
    )
