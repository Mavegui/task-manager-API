from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    
    user = serializers.ReadOnlyField(source='user.username')
    
    class Meta:
        model = Task
        
        fields = [
            'id',
            'user',
            'title',
            'description',
            'priority',
            'completed',
            'created_at',
            'updated_at'
        ]
        
        read_only_fields = ['id', 'created_at', 'updated_at']
        
    def validate_title(self, value: str) -> str:
        value_title = value.strip()
        if not value_title:
            raise serializers.ValidationError("O campo título não pode ser somente espaços em branco.")
        if len(value_title) < 6:
            raise serializers.ValidationError("O campo título deve ter pelo menos 6 caracteres.")
        return value_title
    
    def validate_description(self, value: str) -> str:
        value_description = value.strip()
        if not value_description:
            raise serializers.ValidationError("O campo descrição não pode ser somente espaços em branco.")
        if len(value_description) < 10:
            raise serializers.ValidationError("O campo descrição deve no mínimo 10 caracteres.")
        return value_description
    
    def validate(self, data: dict) -> dict:
        
        is_creating = self.instance is None
        
        if is_creating and data.get('completed') is True:
            raise serializers.ValidationError({
                "completed": "Uma nova tarefa não pode ser criada como concluída."
            })
        
        priority = data.get('priority')
        description = data.get('description')
        
        if priority == Task.Priority.HIGH and len(description.strip()) < 20:
            raise serializers.ValidationError({
                "description": "Tarefas com prioridade ALTA exigem uma descrição maior e mais detalhada."
            })
            
        return data
    
class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True, required=True)
    password_confirm = serializers.CharField(write_only=True, required=True)
    
    email = serializers.EmailField(
        required=True, 
        validators=[UniqueValidator(queryset=User.objects.all(), message="Este e-mail já está registrado.")]
    )
         
    class Meta:
        model = User 
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password_confirm']
    
    def validate(self, attrs):
        if attrs["password"] != attrs["password_confirm"]:
            raise serializers.ValidationError(
                {"password_confirm": "As senhas não coincidem."}
            )
        
        try:
            user_temp = User(username=attrs.get("username"))
            validate_password(password=attrs["password"], user=user_temp)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError({"password": list(e.messages)})
            
        return attrs
        
    def create(self, validated_data):
        validated_data.pop("password_confirm")
        
        user = User.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        return user