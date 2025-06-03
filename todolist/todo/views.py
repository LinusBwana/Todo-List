from ast import If
from django.shortcuts import get_object_or_404, redirect, render
from .forms import TaskForm
from .models import Task
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html', {})

@login_required
def new_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('todo:display_tasks')          
    else:
        form = TaskForm()
    return render(request,'forms.html', {'form': form})

@login_required
def display_tasks(request):
    tasks = Task.objects.all()
    return render(request, 'base.html', {'tasks': tasks})

@login_required
def edit_task(request, task_id):
    # try:
    #     task = Task.objects.get(id=task_id)
    # except Task.DoesNotExist:
    #     raise Http404("Task not found")

    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        
        if form.is_valid():
            form.save()
            return redirect('todo:display_tasks')
        
    else:
        form = TaskForm(instance = task)

    return render(request, 'edit.html', {'form': form})

@login_required
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('todo:display_tasks')

    return render(request, 'confirm_delete.html', {'task': task})

def confirm_delete(request):
    return render(request, 'confirm_delete.html')

def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username =  form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('todo:display_tasks')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def user_logout(requst):
    logout(requst)
    return redirect('todo:user_login')


def user_signup(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('todo:display_tasks')
        else:
            return render(request, 'signup.html', {'form':form})

    else:
        form = UserRegisterForm()
    
    return render(request, 'signup.html', {'form':form})


