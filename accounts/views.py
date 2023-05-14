from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib.auth.models import auth,User
from django.contrib import messages

# Create your views here.
#https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html

def login(request):
    if request.method== 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid username or password')
            return redirect('login')
    else:
        return render(request,'login.html')

def register(request):
	if request.method == 'POST':
		first_name=request.POST["fname"]
		last_name=request.POST["lname"]
		username=request.POST["username"]
		email=request.POST["email"]
		password1=request.POST["password1"]
		password2=request.POST["password2"]
		
		print(first_name,"  ",last_name,"  ",username,"  " ,email,"  ",password1)
		if password1==password2:
			if User.objects.filter(username=username).exists():
				messages.info(request,"username is already taken")
				return redirect('register')
			elif User.objects.filter(email=email):
				messages.info(request,"email is already taken")
				return redirect('register')
			else:
				user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
				user.save()
				print("user created")
				return redirect('login')
		else:
			messages.info(request,"Password not matching")
			return redirect('register')
	else:
		print("Error....................")
		return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')




