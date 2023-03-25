from django.shortcuts import render, redirect

from dodo_app import models
from dodo_app.forms import TodoForm
from dodo_app.models import Todo


# Create your views here.
def home(request):
    return render(request,"home.html")

def index(request):
    return render(request,"index.html")

def indexx(request):
    return render(request,"indexx.html")

#create

def add(request):
    data = TodoForm

    if request.method == 'POST':
        data = TodoForm(request.POST)
        if data.is_valid:
            data.save()
            return redirect("getdata")
    return render(request,"view.html",{"data":data})

#view
def getdata(request):
    data = Todo.objects.all()
    print(data)
    return render(request,"getdata.html",{"data":data})


def update(request,Todo_id):

    todo = Todo.objects.get(id=Todo_id)
    form = TodoForm(instance=todo)
    if request.method == 'POST':
        form = TodoForm(request.POST,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("getdata")

    return render(request,"update.html",{'form':form})

def delete(request,Todo_id):
    wm=Todo.objects.get(id=Todo_id)
    wm.delete()
    return redirect("getdata")

