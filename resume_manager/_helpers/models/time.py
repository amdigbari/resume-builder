from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete import SOFT_DELETE_CASCADE
from safedelete.models import SafeDeleteManager, SafeDeleteModel


# Time
class TimeModelQuerySet(models.QuerySet):
    """adding auto_now functionality for updating a queryset

    bulk_update() does not call save() method nor it fires pre_save and post_save signals
    on instance ( generally produces only single update query )
    so for updating the updated_at we overwrite the update() method in QuerySet

    """

    def update(self, **kwargs):
        if "updated_at" not in kwargs:
            kwargs["updated_at"] = datetime.now()
        return super().update(**kwargs)


class TimeModelManager(models.Manager.from_queryset(TimeModelQuerySet)):
    pass


class TimeModel(models.Model):
    objects: models.Manager = TimeModelManager()

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("created at"),
        help_text=_("instance created at"),
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("updated at"),
        help_text=_("latest update at"),
    )

    class Meta:
        abstract = True


# Time + SafeDelete
class TimeSafeDeleteModelManager(SafeDeleteManager):
    """adding auto_now functionality for updating a queryset

    bulk_update() does not call save() method nor it fires pre_save and post_save signals
    on instance ( generally produces only single update query )
    so for updating the updated_at we overwrite the update() method in QuerySet

    """

    def update(self, **kwargs):
        if "updated_at" not in kwargs:
            kwargs["updated_at"] = datetime.now()

        return super().update(**kwargs)


class TimeSafeDeleteModel(SafeDeleteModel):
    objects: models.Manager = TimeSafeDeleteModelManager()

    _safedelete_policy = SOFT_DELETE_CASCADE

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True
