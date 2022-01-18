from rest_framework import serializers
from .models import TodoList, Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'done', 'list']



class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ['id', 'name', 'description']


class TodoListWithCountSerializer(serializers.Serializer):
    list = TodoListSerializer()
    done_amount = serializers.IntegerField()
    total = serializers.IntegerField()


class TodoListWithTodosSerializer(serializers.ModelSerializer):
    todos = TodoSerializer(many=True)

    class Meta:
        model = TodoList
        fields = ['id', 'name', 'description', 'todos']




