from django.contrib import admin

from sub_category.models import SubCategory


@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")

    search_fields = ("category__name", "name")

    def category(self, obj):
        return obj.category.name

    category.short_description = "Category"
