from django.urls import path
from fcm import views

# app_name = 'scrap_app'
urlpatterns =[
	path('notification/',views.caller_function, name='send_notification'),
	path('mails/',views.EmailView.as_view(),name='send_mail'),
]