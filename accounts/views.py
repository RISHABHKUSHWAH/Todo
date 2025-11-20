
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username ,password = password)
        auth_login(request,user)
        return redirect('http://127.0.0.1:8000')
    return render(request,'login.html')    

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        if password == conpassword:
            obj = User(username =username ,password = password)
            obj.save()
        else:
            return HttpResponse("password and conf password are differnt")\

    return render(request,'register.html')

def user_logout(request):
    user = request.user #current user ,id,first name
    logout(request)
    return redirect("/")