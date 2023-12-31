from django.db import models
from django.urls import reverse


class Category(models.Model):
    """
    model for ingredinet that belong to a category
    """
    name = models.CharField(max_length=60, unique=True)

    class meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Nutritionals(models.Model):
    """
    data extension for ingredient one to one relationship
    """
    calories = models.FloatField()
    carbohydrates = models.FloatField()
    proteins = models.FloatField()
    fat = models.FloatField()
    starch = models.FloatField()


class IngredientImp():
    name = ""
    category = ""
    calories = 0.0
    carbohydrates = 0.0
    proteins = 0.0
    fat = 0.0
    starch = 0.0


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutritional = models.OneToOneField(Nutritionals, on_delete=models.CASCADE, null=True, blank=True, related_name='nutritional')

    class meta:
        ordering = ["name"]

    def get_absolute_url(self):
        return reverse("ingredient-detail", kwargs={'pk': self.id})

    def __str__(self):
        return self.name

    @property
    def get_giacenza(self):
        return 1000
