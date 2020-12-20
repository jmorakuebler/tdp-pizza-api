from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from users.serializers import DRFAuthTokenSerializer


class CreateDRFTokenView(ObtainAuthToken):
    """Crea un nuevo token para el usuario"""
    serializer_class = DRFAuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
