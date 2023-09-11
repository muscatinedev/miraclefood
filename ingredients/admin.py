from django.contrib import admin

from ingredients.models import Category, Ingredient


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    def get_ordering(self, request):
        return ['id']  # sort case insensitive

admin.site.register(Category, CategoryAdmin)

class IngredientAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'category']
    search_fields = ['name']
    def get_ordering(self, request):
        return ['name']  # sort case insensitive


admin.site.register(Ingredient, IngredientAdmin)