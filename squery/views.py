from django.shortcuts import render
from datetime import date
from .models import QueryPost, student
from django.shortcuts import redirect
from .forms import PostForm
from django.utils import timezone
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# @login_required
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


# @ login_required()
def querys(request):
    posts = QueryPost.objects.all()
    context = {
        'posts': posts,
        'post_setting':True
    }

    return render (request,"squery/query.html",context)

@ login_required()
def handlelogout(request):
    logout(request)
    messages.info(request, "Logged Out Successfully.")
    return redirect('starting-page')

# @ login_required(login_url='/login/')
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
    return render(request,"squery/settings.html")
def register_admin (request):
    return render(request,"squery/register_admin.html")


def handlelogin(request):
    if request.method == 'POST':
        roll_number = request.POST.get('email')
        password = request.POST.get('password')
        print(roll_number,password)

        user = student.objects.filter(Roll_number=roll_number, Password=password).first()

        if user:
            return redirect("querys")  
        message = "🙈 Incorrect credential"
        return  render (request,"squery/register_student.html",{"message":message} )
    return render(request, "squery/register_student.html")



# loginusername = request.POST.get('email')
        # loginpassword = request.POST.get('password')
#         user = authenticate(request, username=loginusername,
#                             password=loginpassword)
#         if user is not None:
#             login(request, user)
#             messages.success(request, "Logged In Successfully  .")
#             return redirect('querys')