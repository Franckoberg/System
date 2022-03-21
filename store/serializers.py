from rest_framework import serializers
from store.models import Users


class UserSerialiser(serializers.ModelSerializer):
    class Meta:
        model = Users

        fields = [
            'id', 'first_name','last_name','email','username','password','phone','foto'
        ]