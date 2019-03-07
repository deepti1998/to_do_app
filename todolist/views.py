import requests
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import ToDoList
# Create your views here.


def register(request):
    if request.method == 'POST':
        f = UserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')

    else:
        f = UserCreationForm()

    return render(request, 'registration/register.html', {'form': f})


@login_required
def create_task(request):
    template = loader.get_template('create_task.html')
    return HttpResponse(template.render())


@csrf_exempt
@login_required
def view_task(request):
    if request.method == 'POST':
        print(request.POST)
        title = request.POST['title']
        description = request.POST['description']
        datetime = request.POST['datetime']
        date_time = datetime.split('T')
        try:
            task = ToDoList.objects.get(title=title)
            task.title = title
            task.content = description
            task.due_date = date_time[0]
            task.due_time = date_time[1]
            status = request.POST['status']
            if status == 'Pending':
                task.completed = False
            else:
                task.completed = True
        except:
            task = ToDoList(title=title, content=description, due_date=date_time[0], due_time=date_time[1])
        task.save()
    titles = []
    contents = []
    creation_dates = []
    due_dates = []
    due_times = []
    status = []
    try:
        tasks = ToDoList.objects.all()
        print("jhb")
        for task in tasks:
            titles += [task.title]
            contents += [task.content]
            creation_dates += [task.creation_date]
            due_dates += [task.due_date]
            due_times += [task.due_time]
            status += [task.completed]
    except Exception as e:
        print(e)
        pass
    template = loader.get_template('view_task.html')
    data = zip(titles, contents, creation_dates, due_dates, due_times, status)
    return HttpResponse(template.render({
        'data': data
    }))


def delete_task(request, title):
    try:
        task = ToDoList.objects.filter(title = title)
        task.delete()
    except Exception as e:
        print(e)
    return redirect(view_task)


@login_required
def mark_as_completed(request, title):
    try:
        task = ToDoList.objects.get(title=title)
        task.completed = True
        task.save()
    except Exception as e:
        print(e)
    return redirect(view_task)


@login_required
@csrf_exempt
def update_task(request, title):
    try:
        task = ToDoList.objects.get(title=title)
        if request.method == 'POST':
            print("flknlk")
            title = request.POST['title']
            description = request.POST['description']
            datetime = request.POST['datetime']
            #  print(datetime)
            date_time = datetime.split('T')
            task.title = title
            task.content = description
            task.due_date = date_time[0]
            task.due_time = date_time[1]
            task.save()
            redirect(view_task)
        else:
            print("sfkjvnj")
            title = task.title
            content = task.content
            due_date = task.due_date
            due_time = task.due_time
            status = task.completed
            template = loader.get_template('update_task.html')
            return HttpResponse(template.render({
                'title': title,
                'content': content,
                'due_date': due_date,
                'due_time': due_time,
                'status': status
            }))
    except Exception as e:
        print(e)

