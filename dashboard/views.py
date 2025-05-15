from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login
from authentication.models import RoleChoices,Profile
from .forms import CreateUserForm,TaskForm
from .models import Task,AssignedUsers
from django.shortcuts import get_object_or_404


# Create your views here.

def admin(request):
    if not request.user.role == 'admin' or not request.user.is_superuser:
        return redirect('admin_login')
    tasks=Task.objects.all()
    try:
        admin_users=AssignedUsers.objects.get(admin=request.user).users.all()
    except:
        admin_users=None
    for task in tasks:
        print(task.uuid, 'tast',request.user)
    return render(request,'admin_dashboard.html',{'tasks':tasks,'admin_users':admin_users,'total_users':admin_users.count() if admin_users else 0,'total_tasks':tasks.count() if tasks else 0})


def super_admin(request):
    if not request.user.is_superuser:
        return redirect('admin_login')
    admin_users=Profile.objects.filter(role=RoleChoices.ADMIN)
    return render(request,'super_admin_dashboard.html',{'admin_users':admin_users})


def login_view(request):
    username=request.POST.get('username')
    password=request.POST.get('password')

    if not username or not password:
        return render(request,'login.html')
    
    user=authenticate(username=username,password=password)

    if user is not None:
        login(request,user)
        if user.role == RoleChoices.ADMIN and not user.is_superuser:
            return redirect('admin_dashboard')
        elif user.is_superuser:
            return redirect('super_admin')
        return redirect('dashboard')

    return render(request,'login.html')


def admin_logout(request):
    return redirect('admin_login')


def assign_users(request,admin_id):
    if not request.user.is_superuser:
        return redirect('admin_login')
    users=Profile.objects.filter(role=RoleChoices.USER)
    if request.method == 'POST':
        data=request.POST.get('selected_users')
        assinged_user=AssignedUsers.objects.filter(admin__id=admin_id)
        if assinged_user.exists():
            assinged_user=assinged_user.first()
        else:
            assinged_user=AssignedUsers.objects.create(admin_id=admin_id)
        
        for user_id in data:
            user=Profile.objects.get(id=user_id)
            assinged_user.users.add(user)
            assinged_user.save()
        users=Profile.objects.filter(role=RoleChoices.USER)

        return redirect('super_admin')
    return render(request,'assign_users.html',{'admin_id':admin_id,'users':users})


def assign_task(request,task_id):
    if request.method == 'POST':
        task=get_object_or_404(Task,uuid=task_id)
        user=get_object_or_404(Profile,id=request.POST.get('user_id'))
        task.assigned_to=user
        task.save()
    return redirect('admin_dashboard')


## manage users 
def list_users(request):
    if request.user.is_superuser:
        users=Profile.objects.filter(role=RoleChoices.USER)
    else:
        users=AssignedUsers.objects.get(admin=request.user).users.all()
    return render(request,'list_users.html',{'users':users})


def add_user(request):
    if not request.user.is_superuser:
        return redirect('admin_login')
    if request.method == 'POST':
        data=request.POST.copy()
        data['role']=RoleChoices.USER
        form = CreateUserForm(data)
        if form.is_valid():
            form.save()
            return redirect('list_users')
    else:
        form = CreateUserForm()
    return render(request,'add_user.html',{'form':form})


def view_user(request,user_id):
    if not request.user.is_superuser:
        return redirect('admin_login')
    user=Profile.objects.get(id=user_id)
    return render(request,'view_user.html',{'user':user})


def update_user(request,user_id):
    user=Profile.objects.get(id=user_id)
    if request.method == 'POST':
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.username=request.POST.get('username')
        if request.POST.get('password'):
            user.set_password(request.POST.get('password'))
        user.save()
        return redirect('list_users')
      
    return render(request,'update_user.html',{'user':user})

def delete_user(request,user_id):
    user=Profile.objects.get(id=user_id)
    user.delete()
    return redirect('list_users')

## manage admin 

def create_admin(request):
    if request.method == 'POST':
        data=request.POST.copy()
        data['role']=RoleChoices.ADMIN
        form = CreateUserForm(data)
        if form.is_valid():
            form.save()
            return redirect('super_admin')

    return render(request,'create_admin.html')


def update_admin(request,user_id):
    user=Profile.objects.get(id=user_id)
    print(request.method,'asdfafd')
    if request.method == 'POST':
        user.first_name=request.POST.get('first_name')
        user.last_name=request.POST.get('last_name')
        user.username=request.POST.get('username')
        if request.POST.get('password'):
            user.set_password(request.POST.get('password'))
        user.save()
        return redirect('super_admin')
      
    return render(request,'update_admin.html',{'user':user})


def delete_admin(request,user_id):
    user=Profile.objects.get(id=user_id)
    user.delete()
    return redirect('super_admin')


def promote_user(request,user_id):
    user=Profile.objects.get(id=user_id)
    user.role=RoleChoices.ADMIN
    user.save()
    return redirect('list_users')

def demote_user(request,user_id):
    user=Profile.objects.get(id=user_id)
    user.role=RoleChoices.USER
    user.save()
    return redirect('super_admin')


## Tasks

def create_task(request):
    if request.method == 'POST':
        data=request.POST.copy()
        data['created_by']=request.user
        form = TaskForm(data)
        if form.is_valid():
            form.save()
            return redirect('admin_dashboard')
        else:
            print(form.errors)
    else:
        form = TaskForm()
    return render(request,'create_task.html',{'form':form})


def delete_task(request,task_id):
    task=Task.objects.get(uuid=task_id)
    task.delete()
    return redirect('admin_dashboard')

def view_task(request,task_id):
    task=Task.objects.get(uuid=task_id)
    return render(request,'view_task.html',{'task':task})


def update_task(request,task_id):
    task=Task.objects.get(uuid=task_id)
    if request.method == 'POST':
        task.title=request.POST.get('title')
        task.description=request.POST.get('description')
        task.due_date=request.POST.get('due_date')
        task.save()
        return redirect('admin_dashboard')
    return render(request,'update_task.html',{'task':task})


## Task Report 

def view_report(request,task_id):
    task=Task.objects.get(uuid=task_id)
    return render(request,'report.html',{'task':task})