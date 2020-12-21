from django.utils.translation import gettext_lazy as _

from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.serializers import ValidationError
from rest_framework.decorators import action
from rest_framework.response import Response

from pizzas import serializers
from pizzas import models
from pizzas.permissions import StaffOrSuperuserPermission


SAFE_ACTIONS = ['list', 'retrieve']


class PizzaViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    """ViewSet para listar, obtener, crear y actualizar el objeto Pizza"""
    queryset = models.Pizza.objects.all()

    def get_queryset(self):
        qs = self.queryset
        user = self.request.user
        if not user.is_staff and not user.is_superuser:
            qs = qs.filter(is_active=True)
        return qs

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return serializers.PizzaDetailInfoSerializer
        elif self.action in ('create', 'update'):
            return serializers.PizzaDetailSerializer
        elif self.action in ('add_ingredient', 'delete_ingredient'):
            return serializers.PizzaIngredientSerializer
        return serializers.PizzaSerializer

    def get_permissions(self):
        if self.action not in SAFE_ACTIONS:
            return (StaffOrSuperuserPermission(),)
        else:
            return (IsAuthenticated(),)

    @action(methods=['POST'], detail=True, url_path='ingredientes')
    def add_ingredient(self, request, pk=None):
        """
        Agrega ingredientes a una pizza. A diferencia de la accion 'update',
        solo es necesario enviar los ingredientes, sin utilizar la opción
        'partial'.
        """
        pizza = self.get_object()
        serializer = self.get_serializer(
            pizza,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class IngredientViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    """
    ViewSet para crear, obtener, actualizar y destruir el objeto Ingredient
    """
    serializer_class = serializers.IngredientSerializer
    permission_classes = (StaffOrSuperuserPermission,)
    queryset = models.Ingredient.objects.all()

    def perform_destroy(self, instance):
        if instance.pizza_set.count() > 0:
            msg = _("Ingrediente relacionado a Pizzas. No se puede eliminar")
            raise ValidationError(msg, code='validation')
        instance.delete()
