from django.contrib import messages
from django.shortcuts import render,redirect
from .models import Todo

def home(request):
    return render(request,'home.html')

def create(request):
    if request.method == "POST":
        title = request.POST['title']
        memo = request.POST['memo']
        obj = Todo(title = title , memo = memo)
        obj.save()
        messages.success(request, 'Created')    
    return render(request,'create.html')

def Currenttodo(request):
    todo_data = Todo.objects.filter(is_complete = False)
    return render(request,'currenttodo.html',{'data':todo_data})

def Update(request,pk):
    if request.method == "POST":
        title = request.POST['title']
        memo = request.POST['memo']
        obj = Todo.objects.get(id=pk)  
        obj.title = title
        obj.memo = memo
        obj.save()
        messages.success(request, 'updated')   
        return redirect("http://127.0.0.1:8000/currenttodo/")
    obj = Todo.objects.filter(id=pk)    
    return render(request,'update.html',{'data':obj})    
    
def Complete(request,pk):
    data = Todo.objects.get(id=pk)
    data.is_complete = True
    data.save()
    messages.success(request, 'Todo is Completed')   
    return redirect("/")

def All_complete(request):
    data = Todo.objects.filter(is_complete = True)
    return render(request,"complete_todo.html",{'complete':data})   

    
def Delete(request,pk):
    data = Todo.objects.filter(id=pk)
    data.delete()
    return redirect("http://127.0.0.1:8000/all_complete/")    