from django.contrib import admin

from pizzas import models


@admin.register(models.Pizza)
class PizzaAdmin(admin.ModelAdmin):
    """Clase personalizada para el objeto Pizza en Django Admin Site"""
    list_display = ('name', 'price', 'is_active', 'total_ingredients')


admin.site.register(models.Ingredient)
