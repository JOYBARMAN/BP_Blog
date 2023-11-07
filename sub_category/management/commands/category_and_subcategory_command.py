import logging

from django.core.management.base import BaseCommand

from category.models import Category
from sub_category.models import SubCategory
from common.data.category_subcategory import categories_and_subcategory

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Category and Sub-Category management command"""

    def handle(self, *args, **options):
        logger.info("Running Category and Sub-Category management command")

        category_to_create = []
        sub_category_to_create = []

        for category_info in categories_and_subcategory:
            category = Category(name=category_info["name"])
            category_to_create.append(category)

            for sub_cat in category_info["subcategories"]:
                sub_category = SubCategory(category=category, name=sub_cat)
                sub_category_to_create.append(sub_category)

        # Bulk create Category instances
        Category.objects.bulk_create(category_to_create)

        # Bulk create SubCategory instances
        SubCategory.objects.bulk_create(sub_category_to_create)

        logger.info("Category and Sub-Category data created successfully")
