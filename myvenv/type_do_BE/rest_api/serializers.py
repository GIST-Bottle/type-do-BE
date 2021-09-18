from rest_framework import serializers
from .models import Todo, Inprogress, Done

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'time', 'title', 'priority', 'category']

class InprogressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inprogress
        fields = ['id', 'time', 'title', 'priority', 'category']

class DoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Done
        fields = ['id', 'time', 'title', 'priority', 'category']

