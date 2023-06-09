from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
def home(request):
    return render(request,'computer_temp/index.html')
def form(request):
    
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['Email']
        subject=request.POST['subject']
        message=request.POST['message']
        
        user=User.objects.create_user(username=name,email=email,subject=subject,message=message)
        user.save()
        print('get message')
        return redirect('/')
    else:
        return render(request,'computer_temp/form.html')
    
    


# Create your views here.
