from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from safedelete.models import SafeDeleteManager


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


class TimeSafeDeleteModel(models.Model):
    objects: models.Manager = TimeSafeDeleteModelManager()

    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True
