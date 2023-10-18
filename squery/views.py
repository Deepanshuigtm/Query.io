from django.shortcuts import render
from datetime import date
from .models import QueryPost, student,Likes
from django.shortcuts import redirect,get_object_or_404
from .forms import PostForm
from django.utils import timezone
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User

import numpy as np
import pandas as pd

import matplotlib
matplotlib.use('Agg')  # Use the Agg backend (non-interactive, suitable for server-side use)
import matplotlib.pyplot as plt

@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user  # Assuming you have user authentication
            post.save()
            print("here2")
            messages.success(request, "Query Posed Successfully 🥳")
            return redirect('querys')  # Redirect to a page showing all posts
        else:
            posts = QueryPost.objects.all()
            context = {
                'posts': posts,
                
            }
            messages.success(request, "Enter valid Details / Image Format  ⚠️")
            return render(request, 'squery/query.html',context)
    else:
        print("here1")
        form = PostForm()
    
    return render(request, 'squery/query.html', {'form': form})

def startingpage(request):
    return render (request,"squery/index.html")


@ login_required()
def querys(request):
    posts = QueryPost.objects.all()
    context = {
        'posts': posts,
        'username':request.user
    }

    return render (request,"squery/query.html",context)

@ login_required()
def handlelogout(request):
    logout(request)
    messages.info(request, "Logged Out Successfully.")
    return redirect('starting-page')

@ login_required(login_url='/login/')
def faq(request):
    return render(request,"squery/FAQ.html")

def register_parent (request):
    return render(request,"squery/register_parent.html")

def register_student (request):
    # student = StudentsDetail.objects.get(id=1)
    # context = {
    #     'student': student,
    # }
    return render(request,"squery/register_student.html")

def adminDashboard (request):

    posts = QueryPost.objects.filter(likes__gt=0)
    user = User.objects.all()

    context = {
        'posts': posts,
        'user':user
    }
    return render(request,"squery/settings.html", context)

def register_admin (request):
    return render(request,"squery/register_admin.html")


def handlelogin(request):
    if request.method == 'POST':
        roll_number = request.POST.get('email')
        password = request.POST.get('password')
        print(roll_number,password)

        user = User.objects.filter(username=roll_number, password=password).first()

        if user:
            messages.success(request, "Logged in")
            login(request,user)
            return redirect("querys")
        message = "🙈 Incorrect credential"
        return  render (request,"squery/register_student.html",{"message":message} )
    return render(request, "squery/register_student.html")


def parent(request):
    return render(request,"squery/parent.html")


def like(request, post_id):
    user = request.user  # Get the current user
    print(user.username)

    # Get the post or return a 404 response if it doesn't exist
    post = get_object_or_404(QueryPost, id=post_id)

    # Check if the user has already liked the post
    liked = Likes.objects.filter(user=user, post=post).exists()

    if not liked:
        print('doing like')
        # If the user hasn't liked the post, create a Like object
        Likes.objects.create(user=user, post=post)
        post.likes += 1  # Increase the likes count
    else:
        # If the user has already liked the post, remove the Like object
        Likes.objects.filter(user=user, post=post).delete()
        post.likes -= 1  # Decrease the likes count

    post.save()

    return HttpResponseRedirect(reverse('querys'))

# def like(request, post_id):
#     print("helloooo")
#     user = request.user
#     post = QueryPost.objects.get(id=post_id)
#     current_likes = post.likes
#     liked = Likes.objects.filter(user=user,post=post).count()

#     if not liked:
#         liked = Likes.objects.create(user=user, post=post)
#         current_likes = current_likes + 1
#     else:
#         liked = Likes.objects.filter(user=user, post=post).delete
#         current_likes = current_likes - 1
    
#     post.likes = current_likes
#     post.save()

#     return HttpResponseRedirect(reverse('starting-page', args=[post_id]))
    # return render(request,"squery/parent.html")


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username)

        if user.exists():
            messages.error(request, "Username already taken  ⚠️")
            return redirect('signup')

        user = User.objects.create(
            username = username,
            password = password
        )
        # user.set_password(password)
        user.save()
        messages.success(request, "Account created Sucessfuly 🥳")
        return redirect('querys')
    return render (request,"squery/signup.html")

def post_details(request, post_id):
    
    user = request.user  # Get the current user

    # Get the post or return a 404 response if it doesn't exist
    post = get_object_or_404(QueryPost, id=post_id)

    context = {
        'post': post,
        'username':request.user
    }

    return render(request,"squery/post_details.html", context)

def parent_graph(request):
    import os

    file_path = os.path.join(os.path.dirname(__file__), 'marks.csv')
    dataset = pd.read_csv(file_path)
    # dataset = dataset.drop("Sec A (140)", axis=1)
    # dataset = dataset.drop("Sec B", axis=1)

    marks = dataset.iloc[0, 1:].values
    rollnumber = rollnumber = dataset.iloc[0, 0:].values

    column_names = dataset.columns[1:].to_numpy()
    print(len(column_names))
    print(len(marks))
    print(marks)
    print(column_names)

    # marks = dataset['Final Mark'].values
    # rollnumber = dataset['Class Roll'].values

    plt.scatter(marks, column_names,label="Marks", color="blue", marker="o")
    
    # plt.xlabel("Roll Number")
    # plt.ylabel("Marks")
    plt.title("Scatter Plot of Roll Numbers vs. Marks")
    plt.legend()

    plot_image_path = os.path.join("static", "scatter_plot.png")
    plt.savefig(plot_image_path)
    plt.close()

    return render(request,"squery/parent_graph.html")

@login_required()
def rewards(request):

    posts = QueryPost.objects.all()
    context = {
        'posts': posts,
        'username':request.user,
    }

    return render(request,"squery/rewardform.html",context)

def admin_rewards(request,user_id):
    print(user_id)
    posts = QueryPost.objects.filter(user_id=user_id)
    
    print(posts)
    context = {
        'posts': posts,
        'username':request.user
    }

    return render(request,"squery/studentreward.html",context)