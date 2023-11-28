from celery import shared_task
from datetime import datetime, timedelta
from .models import QueryPost, student,Likes, Certificate
from django.core.mail import send_mail
from query import settings

# @shared_task(bind=True)

# def test_func_2(self):
#     #operation
#     for i in range(10):
#         print(f"deepanshu great {i}")
#     return "Task 2 Done"

@shared_task(bind=True)
def test_func(self):
    # Get today's date
    current_date = datetime.now().date()

    # Retrieve posts from the database
    posts = QueryPost.objects.all()

    post_details_to_send = []

    # Check date for each post
    for post in posts:
        if hasattr(post, 'date'): 
            post_date = post.date

             # Check if the post date is 5 days older than the current date
            if current_date - post_date.date() >= timedelta(days=5):

                post_details_to_send.append(f"Post id {post.id} is {current_date - post_date.date()}  days old.")
                print(f"Post id {post.id} is {current_date - post_date.date()}  days old.")
    
    subject="this email is from django server"
    message = post_details_to_send
    from_email=settings.EMAIL_HOST_USER
    # recipient_list=["maheshwari.kush20@gmail.com"]
    recipient_list=["2207deepanshu@gmail.com"]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list
    )

    return "Task 2 Done"