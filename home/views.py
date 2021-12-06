from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from . models import Tasks
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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

@login_required(login_url='/login')
def details(request):
    allTasks = Tasks.objects.all()
    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)



@login_required(login_url='/login')
def deleteTask(request, task_id):
    taskToDelete = Tasks.objects.get(id=task_id)
    taskToDelete.delete()
    return HttpResponseRedirect('/tasks/')


def login_user(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        return render(request, 'login_user.html')
    elif request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            message = "Invalid Credentials"
            return render(request, 'login_user.html', {
                                                        'message': message
                                                      })


def logout_user(request):
    logout(request)
    return HttpResponseRedirect('/')


def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')

    if request.method == 'GET':
        return render(request, 'register.html')     
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        checkUsername = User.objects.filter(username=username)
        if checkUsername:
            message = "Username already taken. Please choose some order username"
            return render(request, 'register.html', {
                                                        'message':message                                            
                                                    })
        else:
            user = User.objects.create_user(username, email, password)
            user.save()
            login(request, user)
            return HttpResponseRedirect('/')