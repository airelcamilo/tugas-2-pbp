from django.shortcuts import render

# Create task
from . import forms

# Register user
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Login user
from django.contrib.auth import authenticate, login

# Logout user
from django.contrib.auth import logout
from .models import Task

# Restriksi halaman todolist
from django.contrib.auth.decorators import login_required


# Show todolist
@login_required(login_url='/todolist/login/')
def show_todolist(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'user' : request.user,
        'tasks' : tasks,
    }
    return render(request, 'todolist.html', context)

# Create task
@login_required(login_url='/todolist/login/')
def create_task(request):
    form = forms.CreateTask()

    if request.method == "POST":
        form = forms.CreateTask(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect('todolist:show_todolist')
            
    context = {'form':form}
    return render(request, 'create_task.html', context)

# Register user
def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

# Login user
def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('todolist:show_todolist')
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

# Logout user
def logout_user(request):
    logout(request)
    return redirect('todolist:login')

# Change status
def change_status(request, id):
    task = Task.objects.get(user=request.user, pk=id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

# Delete task
def delete_task(request, id):
    task = Task.objects.get(user=request.user, pk=id)
    task.delete()
    return redirect('todolist:show_todolist')