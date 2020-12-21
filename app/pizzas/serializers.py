from rest_framework import serializers

from pizzas import models


class IngredientSerializer(serializers.ModelSerializer):
    """Serializador para el objeto Ingredient"""
    class Meta:
        model = models.Ingredient
        fields = ('id', 'name', 'get_category_display', 'category')
        read_only_fields = ('id', 'get_category_display')
        extra_kwargs = {
            'category': {'write_only': True},
        }


class PizzaSerializer(serializers.ModelSerializer):
    """Serializador para el objeto Pizza"""
    class Meta:
        model = models.Pizza
        fields = ('id', 'name', 'price', 'total_ingredients')
        read_only_fields = ('id', 'total_ingredients')


class PizzaDetailSerializer(PizzaSerializer):
    """Serializador para creación y actualización de una Pizza"""
    class Meta(PizzaSerializer.Meta):
        fields = ('id', 'name', 'price', 'is_active', 'ingredients')


class PizzaDetailInfoSerializer(PizzaDetailSerializer):
    """Serializador para visualización de una Pizza"""
    ingredients = IngredientSerializer(many=True, read_only=True)


class PizzaIngredientSerializer(PizzaSerializer):
    """Serializador para agregar y quitar ingredientes de una Pizza"""
    class Meta(PizzaSerializer.Meta):
        fields = ('ingredients',)


class PizzaIngredientSerializer2(serializers.Serializer):
    """Serializador para agregar y quitar ingredientes de una Pizza"""
    ingredient_ids = serializers.CharField(max_length=250)
