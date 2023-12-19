"""Model design for post tag"""

from django.db import models

from common.models import BaseModelWithUID


class Tag(BaseModelWithUID):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"
