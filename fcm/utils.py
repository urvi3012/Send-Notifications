import sys
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string



def send_emails(user_name,pending_hrs,email,project_name):
    subject= 'Email Confirmation '
    from_email = settings.DEFAULT_EMAIL_FROM
    html_message = "hi, your mail is" + email + " This mail is system generated \nby Urvi"
    msg = EmailMultiAlternatives(subject, html_message, from_email,[email])
    msg.attach_alternative(html_message, "text/html")
    msg.send()
    print('mail sent')

