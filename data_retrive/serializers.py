from rest_framework import serializers
from .models import user_details
class fetch(serializers.ModelSerializer):
    class Meta:
        model=user_details
        fields=["id","name","mark","college"]

