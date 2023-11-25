from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from query import settings
import time

from celery import shared_task

def send_email_to_client():
    subject="this email is from django server"
    message = "this is a test message from django email for testing Madhur!"
    from_email=settings.EMAIL_HOST_USER
    # recipient_list=["maheshwari.kush20@gmail.com"]
    recipient_list=["madhursinghnain@gmail.com"]

    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list
    )


# @shared_task(blind=True)
# def send_mail_func(self):
#     users = get_user_model().objects.all()
#     for user in users:
#         mail_subject = "Hi! Celery Testing"
#         message = " this the message "
#         print(user.email)
#         to_email = user.email
#         send_mail(
#             subject=mail_subject,
#             message=message,
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=[to_email],
#             fail_silently=True,

#         )
#     return "Done"
