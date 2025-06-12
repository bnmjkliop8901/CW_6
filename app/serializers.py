from app.models import Task,User
from rest_framework import serializers

class TaskSerializers(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['user']
        

class UserSerializers(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'groups']
        extra_kwargs = {'email': {'required': True, 'allow_blank': False}}

    def create(self, validated_data):
        groups_data = validated_data.pop('groups', [])
        user = User.objects.create_user(**validated_data)  

        if groups_data:
            user.groups.set(groups_data)

        return user