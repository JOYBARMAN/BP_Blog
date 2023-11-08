from django.db import models

from common.models import BaseModelWithUID

# from sub_category.models import SubCategory

from versatileimagefield.fields import VersatileImageField


class Category(BaseModelWithUID):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(null=True, blank=True)
    photo = VersatileImageField(
        "category_image", upload_to="images/category/", blank=True
    )

    def __str__(self):
        return self.name

    @property
    def sub_categories(self):
        return [subcategory.name for subcategory in self.category.all()]
