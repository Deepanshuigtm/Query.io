from celery import shared_task
from datetime import datetime, timedelta
from .models import QueryPost, student,Likes, Certificate

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

    # Check date for each post
    for post in posts:
        print(post.id)
        if hasattr(post, 'date'): 
            post_date = post.date

            # Check if the post date is 5 days older than the current date
            if current_date - post_date.date() >= timedelta(days=5):
                print(f"Post {post.id} is 5 days old or older.")

    return "Task 2 Done"