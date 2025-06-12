from app.models import Task, People
from rest_framework import serializers

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class PeopleSerializers(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = '__all__'

def create(self, validated_data):
    groups_data = validated_data.pop('groups', [])  # Extract groups before creating People
    user = People.objects.create(**validated_data)  # ✅ Create user first
    
    if groups_data:
        user.groups.set(groups_data)  # ✅ Correct way to assign many-to-many relationships
    
    return user
