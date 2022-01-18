from django.db import models


# klasa do serializacji obiektu
class TodoListWithCount():
    def __init__(self, list, done_amount, total):
        self.list = list
        self.done_amount = done_amount
        self.total = total

class TodoList(models.Model):
    name = models.CharField(max_length=70)
    description = models.CharField(max_length=255, blank=True)
    todos = []


class Todo(models.Model):
    name = models.CharField(max_length=70)
    done = models.BooleanField(default=False)
    list = models.ForeignKey(TodoList, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

