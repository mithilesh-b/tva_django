
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate, login
from django.urls import reverse
from .models import Course, Video, StudyMaterial
from .forms import VideoForm, StudyMaterialForm
from .forms import CourseForm


def index(request):
    if request.method == "POST":
        sname = request.POST.get('name')
        semail = request.POST.get('email')
        sdesc = request.POST.get('desc')

        print(sname, semail, sdesc)
        print("Data, {}!".format(sname))
        print("Data, {}!".format(semail))

        contact = Contact(name=sname, email=semail, desc=sdesc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent')
        return render(request, 'index.html')

    # Add a default response in case of a GET request
    return render(request, 'index.html')  

    # if request.user.is_anonymous:
    #     return redirect("/login")
    # return render(request, 'index.html')

def about_page(request):
    return render(request, 'about.html')

def viewall (request):   #view the reviews in the index page
    # get all records from database
    review = Contact.objects.all()
    print(review)
    context = {"Contact": review}
    return render (request, 'index.html', context)


def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if user has entered correct credentials
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)  # Log the user in
            return redirect("/incourse")
            #return redirect(reverse('/incourse'))
        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')  # Use render instead of redirect

    # If the request method is not POST, render the login page
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")

def user_course(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request, 'incourse.html')



def add_course(request):  #add course by admin
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')  # Redirect to the index page or any other desired page
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})



def admin_page(request):
    courses = Course.objects.all()
    return render(request, 'admin_tva.html', {'courses': courses})

def upload_video(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('admin_tva')
    else:
        form = VideoForm(initial={'course': course})
    return render(request, 'upload_video.html', {'form': form, 'course': course})

def upload_material(request, course_id):
    course = Course.objects.get(pk=course_id)
    if request.method == 'POST':
        form = StudyMaterialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_tva')
    else:
        form = StudyMaterialForm(initial={'course': course})
    return render(request, 'upload_material.html', {'form': form, 'course': course})


