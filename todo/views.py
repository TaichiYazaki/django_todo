from django.shortcuts import redirect, render

from todo.TodoForm import TodoForm
from todo.models import Todo


# Create your views here.


# def index(request):
#     # if request.method == 'POST':
#     #     form = TodoForm(request.POST)
#     #     form.save()
#     # else:
#     form = TodoForm()
#     # todo_lists = Todo.objects.all()
#     # context = {"todo_lists": todo_lists}
#     return render(request, 'todo.html', {'form': form})

def index(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        form.save()
        return redirect('/')
    form = TodoForm()
    todo_lists = Todo.objects.all()
    context = {
        "todo_lists": todo_lists,
        'form': form
        }
    return render(request, 'todo.html', context)


def delete(request):
    todo_id = request.POST['id']
    Todo.objects.get(id=todo_id).delete()
    return redirect('/')
