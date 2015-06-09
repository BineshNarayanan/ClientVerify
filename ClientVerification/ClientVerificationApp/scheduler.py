import sys,os
import datetime
sys.path.append('D:\\Binesh\\MyPythonProjects\\ClientVerification')
os.environ['DJANGO_SETTINGS_MODULE'] ='ClientVerification.settings'

import django
from django.core.mail import send_mail
from ClientVerification import settings
from ClientVerificationApp.models import Callreminders,Clientmaster


callReminders = Callreminders.objects.filter(date=datetime.datetime.now())
print callReminders

for callReminder in callReminders:
	print callReminder.clientmaster_accountid
	client = Clientmaster.objects.get(accountname = callReminder.clientmaster_accountid)
	subject = "Reminder to call Client : " + client.accountname
	message = "Reminder\n\n The number to be called is " + client.phone + ".\n\nRegards, Admin."
	disclaimer = "\n\nDISCLAIMER : This is an auto-generated mail. Please do not reply to this mail."
	send_mail(subject, message+disclaimer, 'reminder@ebs.in',['binesh.narayanan@morningstar.com','nandakishor.samant@morningstar.com'], fail_silently=False)
	
print "success"