
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
from django.contrib.auth import login as auth_login
from django.shortcuts import render,redirect,HttpResponse

# Create your views here.
def login(request):
    message = ""

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('/')  # redirect to home page
        else:
            message = "Invalid username or password"

    return render(request, 'login.html', {'message': message})

def register(request):
    message =''
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        conpassword = request.POST['conpassword']
        if password == conpassword:
            obj = User.objects.filter(username =username ,password = password)
            if obj is None:
                obj = User(username =username ,password = password)
                obj.save()
                print("in")
            else:
                message = "User is alredy registered...."
        else:
            message = "password and conf password are differnt"

    return render(request,'register.html',{"message":message})

def user_logout(request):
    user = request.user #current user ,id,first name
    logout(request)
    return redirect("/")