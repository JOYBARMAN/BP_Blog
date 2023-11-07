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
        exits_category = []
        new_category = []

        for category_info in categories_and_subcategory:
            # Check if a category with the specified name already exists
            existing_category = Category.objects.filter(
                name=category_info["name"]
            ).exists()
            if not existing_category:
                category = Category(name=category_info["name"])
                category_to_create.append(category)
                new_category.append(name=category_info["name"])

                for sub_cat in category_info["subcategories"]:
                    sub_category = SubCategory(category=category, name=sub_cat)
                    sub_category_to_create.append(sub_category)
            else:
                exits_category.append(category_info["name"])

        # Bulk create Category instances
        Category.objects.bulk_create(category_to_create)

        # Bulk create SubCategory instances if creating Categories was successful
        SubCategory.objects.bulk_create(sub_category_to_create)

        logger.info("Category and Sub-Category data created successfully.")
        logger.warning(f"\n\nAlready exists this category {exits_category}")
        logger.info(f"\n\nNewly added this category {new_category}")
