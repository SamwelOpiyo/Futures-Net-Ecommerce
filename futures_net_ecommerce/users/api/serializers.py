from rest_framework import serializers

from futures_net_ecommerce.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "name"]
