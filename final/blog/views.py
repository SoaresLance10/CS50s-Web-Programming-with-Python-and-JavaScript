from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import User, Poster, Posts, Followinfo, Comment, Like, All_listing
from datetime import datetime 

# Create your views here.
def index(request):
    return render(request, "blog/layout.html")
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "blog/login.html", {"message": "Invalid username and/or password."})
    else:
        return render(request, "blog/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        p_head=Poster()
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "blog/register.html", {"message": "Passwords must match."})

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "blog/register.html", {"message": "Username already taken."})
        login(request, user)
        p_head.name = username
        p_head.save()
        return HttpResponseRedirect(reverse("e_profile", {"username": username}))
    else:
        return render(request, "blog/register.html")

def edit_profile(request, username):
    if request.method == "POST":
        p = Poster.objects.get(name=username)
        p.age = request.POST["age"]
        p.gender = request.POST["gender"]
        p.ttyle = request.POST["ttpye"]
        p.description - request.POST["desc"]

        p.save()
        return HttpResponseRedirect(reverse("profile", {"username": username}))
    else:
        p = Poster.objects.get(name=username)
        return render(request, "blog/editprofile.html", {"username": username, "age": p.age, "gender": p.gender, "ttype": p.ttype, "desc": p.description})

def profile(request, username):
    return render(request, "blog/profile.html", {"username": username, "age": p.age, "gender": p.gender, "ttype": p.ttype, "desc": p.description})

def new_post(request, username):
    return HttpResponse("hi")
