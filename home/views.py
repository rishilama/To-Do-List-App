from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from . models import Tasks


# Create your views here.
def home(request):
    context = {'success' : False}
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        todo = Tasks(title = title, description = description)
        todo.save()
        context = {'success' : True}
    return render(request, 'home.html', context)


def details(request):
    allTasks = Tasks.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)



def deleteTask(request, task_id):
    taskToDelete = Tasks.objects.get(id=task_id)
    taskToDelete.delete()
    return HttpResponseRedirect('/tasks/')