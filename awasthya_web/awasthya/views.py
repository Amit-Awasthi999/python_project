from django.shortcuts import render,redirect
from .models import product
from django.contrib import messages
from django.contrib.auth.models import User ,auth
# Create your views here.
def home(request):
    dests = product.objects.all()
    return render(request,'index.html',{'dests' : dests})

def login(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['psw']
        
        user = auth.authenticate(username=username , password = password)
        if user is not None:
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('/')
    else:
        return render(request,'index.html')



def createuser(request):
    if request.method == "POST":
        username = request.POST['signuser']
        email = request.POST['email']
        PN = request.POST['phonenum']
        password= request.POST['psw']
        repassword= request.POST['psw-repeat']
        if User.objects.filter(username=username).exists():
            print("user name is already taken")
        elif User.objects.filter(email = email).exists():
            print("Email is already taken")
        else:
            user = User.objects.create_user(username = username, email = email, first_name = PN, password = password )
            user.save()
            
   
    return render(request,'index.html')

def catlog(request):
  
    return render(request,'catlog.html')