from django.db import models
from django.utils.translation import gettext_lazy as _


class Ingredient(models.Model):
    """Objeto que describe un ingrediente de Pizza"""
    CATEGORIES = (
        ('B', _("Básico")),
        ('P', _("Premium")),
    )
    name = models.CharField(max_length=255, verbose_name=_("Nombre"))
    category = models.CharField(
        max_length=1, choices=CATEGORIES, verbose_name=_("Categoría")
    )

    class Meta:
        verbose_name = _("Ingrediente")
        verbose_name_plural = _("Ingredientes")

    def __str__(self):
        return self.name


class Pizza(models.Model):
    """Objeto que describe una Pizza"""
    name = models.CharField(max_length=255, verbose_name=_("Nombre"))
    price = models.IntegerField(verbose_name=_("Precio"))
    is_active = models.BooleanField(
        default=False, verbose_name=_("Disponible")
    )
    ingredients = models.ManyToManyField('Ingredient')

    class Meta:
        verbose_name = _("Pizza")
        verbose_name_plural = _("Pizzas")

    def __str__(self):
        return self.name

    @property
    def total_ingredients(self):
        """Retorna la cantidad de ingredientes asociadas a una Pizza"""
        return self.ingredients.all().count()
    total_ingredients.fget.short_description = "Cant. Ingredientes"
