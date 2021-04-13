from django.shortcuts import render

# Create your views here.
from fcm_django.models import FCMDevice


#from settings import FCM_SERVER_KEY

from django.shortcuts import render,redirect,get_object_or_404
from django.views import generic
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import render_to_string


from .utils import send_emails

from django.views import generic


def caller_function(request):

	data = {
		"name": "HORN OK PLEASE!",
		"days": 3,
		"country": "United States"
		}
	send_notification(user_ids=["1","2","3"],
		title="It's now or never: Horn Ok is back!",
		message="Book now to get 50% off!",
		data=data)

	return HttpResponse("hi")


def send_notification(user_ids,title, message, data):
	print(user_ids)
	try:
		device = FCMDevice.objects.filter(user__in=user_ids).first()
		result = device.send_message(title=title,body=message,data=data,sound=True)
	# print("hi")
		return result
	except:
		pass

mail = ['prishanileshjain@gmail.com', 'starkinc98@gmail.com']

class EmailView(generic.View):
	def get(self,request):
		for i in mail:
			send_emails(user_name='Palash',pending_hrs=10,email=i,project_name='p')
		return HttpResponse("Emails sent")	
