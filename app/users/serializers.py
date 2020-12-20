from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers


class DRFAuthTokenSerializer(serializers.Serializer):
    """Serializador para la autenticacion de DRF de usuarios"""
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Valida y autentica el usuario"""
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if not user:
            msg = _("No se pudo autenticar con las credenciales proveídas")
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = user
        return attrs
