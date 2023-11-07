from django.db import models

from common.models import BaseModelWithUID
from category.models import Category

from versatileimagefield.fields import VersatileImageField


class SubCategory(BaseModelWithUID):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="category"
    )
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    photo = VersatileImageField(
        "sub_category_image", upload_to="images/sub_category/", blank=True
    )

    def __str__(self):
        return f"Sub-category = {self.name}    |   Category = {self.category.name}"
