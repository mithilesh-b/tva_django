from django.http import HttpResponse
from django.shortcuts import render, redirect

from django.contrib.auth.models import User
# django.contrib.auth.models built in package


#for messages framework
from django.contrib import messages

def signup_page(request):
    if request.method == "POST":
        username = request.POST.get("uname")
        firstname = request.POST.get("fname")
        lastname = request.POST.get("lname")
        password = request.POST.get("passw")
        con_password = request.POST.get("confirm_pass")
        Email = request.POST.get("email")
        
        if (password!=con_password):
            messages.error(request, "Password and confirm password should be same")
            return redirect('/')
        
        user_object = User.objects.create_user (username, Email, password)
        user_object.first_name = firstname
        user_object.last_name = lastname

        user_object.save()
        messages.success(request,"User Updated Successfully")
        return redirect('/')
          
    return render(request, 'signup.html')
   

def login_page(request):   
    return render(request, 'login.html')

