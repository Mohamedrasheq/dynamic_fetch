from rest_framework import serializers
from .models import user_details
from .models import student
class fetch(serializers.ModelSerializer):
    class Meta:
        model=user_details
        fields=["id","name","mark","college"]

class student_fetch(serializers.ModelSerializer):
    class Meta:
        model=student
        fields=["id","name","courses"]

