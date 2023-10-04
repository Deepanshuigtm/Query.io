from django.shortcuts import render
from datetime import date
from .models import student
from django.shortcuts import redirect

def startingpage(request):
    return render (request,"squery/index.html")

def querys(request):
    return render (request,"squery/query.html")
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


def register_admin (request):
    return render(request,"squery/register_admin.html")


def handlelogin(request):
     if request.method == 'POST':
        roll_number = request.POST.get('email')
        password = request.POST.get('password')
        print(roll_number,password)

        # Replace 'YourUserModel' with your actual user model
        user = student.objects.filter(Roll_number=roll_number, Password=password).first()

        if user:
            # Credentials are correct, redirect to query.html
            return redirect("querys")  # Change 'query_page' to the URL name for your query page
        message = "🙈 Incorrect credential"
        return  render (request,"squery/register_student.html",{"message":message} )