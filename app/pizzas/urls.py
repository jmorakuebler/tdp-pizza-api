from django.urls import path, include

from rest_framework.routers import DefaultRouter

from pizzas import views


app_name = 'pizzas'

router = DefaultRouter()
router.register('pizzas', views.PizzaViewSet)
router.register('ingredientes', views.IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
