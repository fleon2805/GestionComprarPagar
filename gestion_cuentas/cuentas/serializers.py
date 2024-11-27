from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Cliente, Proveedor, Factura
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import Notificacion

Usuario = get_user_model()

# Serializer para el modelo Usuario
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'rol']

# Serializer para el modelo Cliente
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '_all_'

# Serializer para el modelo Proveedor
class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '_all_'

# Serializer para el modelo Factura
class FacturaSerializer(serializers.ModelSerializer):
    cliente_nombre = serializers.ReadOnlyField(source='cliente.nombre')
    proveedor_nombre = serializers.ReadOnlyField(source='proveedor.nombre')

    class Meta:
        model = Factura
        fields = '_all_'

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agregar datos personalizados al token
        token['username'] = user.username
        token['role'] = user.rol  # Asegúrate de que el modelo Usuario tiene el campo 'rol'

        return token

class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '_all_'