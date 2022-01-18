from rest_framework import viewsets
from .models import TodoList, Todo, TodoListWithCount
from .serializers import TodoSerializer, TodoListSerializer, TodoListWithCountSerializer, TodoListWithTodosSerializer
from rest_framework.response import Serializer, Response
from django.shortcuts import get_object_or_404

class TodoListViewSet(viewsets.ModelViewSet):
    queryset = TodoList.objects.all()
    serializer_class = TodoListSerializer

    def list(self, request):
        queryset = TodoList.objects.all()
        todos = Todo.objects.all()
        data = []
        for list in queryset:
            done  = todos.filter(list_id=list.id, done=True).count()
            total = todos.filter(list_id=list.id).count()
            data.append(TodoListWithCount(list, done, total))

        serializer = TodoListWithCountSerializer(data, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = TodoList.objects.all()
        todo_list = get_object_or_404(queryset, pk=pk)

        todos = Todo.objects.filter(list_id=todo_list.id)
        todo_list.todos = todos

        serializer = TodoListWithTodosSerializer(todo_list)
        return Response(serializer.data)

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
