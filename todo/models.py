from django.db import models

# Create your models here.


class Todo(models.Model):
    title = models.CharField('Todoリストの作成', max_length=128)

    def __str__(self):
        return self.title
