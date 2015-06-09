from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from django.db import transaction
from ClientVerificationApp.models import Clientmaster
from ClientVerificationApp.models import Reasonmaster,Clientresponse,Clientresponsereasons,Callreminders,Terminationinitiationqueue

import datetime

#import date

# Create your views here.
def index(request):
	template = loader.get_template('ClientVerificationApp/index.html')
	context = RequestContext(request, {'loadblank':'Y'})	
	return HttpResponse(template.render(context))

def getClientDetails(request):
	template = loader.get_template('ClientVerificationApp/index.html')
	accountId=request.POST.get('txtAccountId')
	client = Clientmaster.objects.get(accountid = accountId)
	reasonswoy = Reasonmaster.objects.filter(reasonCategory='WOY')
	reasonswon = Reasonmaster.objects.filter(reasonCategory='WON')	
	print client.accountname
	context = RequestContext(request, {'accountId':accountId, 'client':client,'reasonswoy':enumerate(reasonswoy,start=1),'reasonswon':enumerate(reasonswon,start=1)})
	return HttpResponse(template.render(context))

def saveClientResponse(request):
	template = loader.get_template('ClientVerificationApp/index.html')
	accountId = request.POST.get('hdnAccountId')
	
	clientAccountId = Clientmaster.objects.get(accountid=accountId)
	
	needReminder = request.POST.get('needReminder')
	websiteOperational = request.POST.get('websiteOperational')
	callAnswered = request.POST.get('callAnswered')
	wishToContinue = request.POST.get('wishToContinue')
	
	if wishToContinue is None:
		wishToContinue = '';

	appointmentTime = request.POST.get('appointmentTime')
	if appointmentTime == '':
		appointmentTime = None
	#appointmentTime = datetime.datetime.now()
	additionalEmail = request.POST.get('additionalEmail')
	additionalPhone1 = request.POST.get('additionalPhone1')
	additionalPhone2 = request.POST.get('additionalPhone2')
	responseDate = datetime.datetime.now()
	print responseDate
	createDate = datetime.datetime.now()
	print createDate
	updateDate = datetime.datetime.now()
	print updateDate
	
	newReason1 = request.POST.get('txtNewReason1Woy')
	newReason2 = request.POST.get('txtNewReason2Woy')
	if websiteOperational == '0':
		newReason1 = request.POST.get('txtNewReason1Won')
		newReason2 = request.POST.get('txtNewReason2Won')
	
	selected_reasons = request.POST.getlist('reasons')
	
	with transaction.atomic():
		#reasonCategory=(websiteOperational == '1') ? 'WOY' : 'WON'
		if newReason1 != '': 
			reasonMaster = Reasonmaster(reason=newReason1,reasonCategory='WOY')
			reasonMaster.save();
			selected_reasons.append(reasonMaster.id);
		
		#reasonCategory=(websiteOperational == '1') ? 'WOY' : 'WON'
		if newReason2 != '': 
			reasonMaster = Reasonmaster(reason=newReason2,reasonCategory='WOY')
			reasonMaster.save();
			selected_reasons.append(reasonMaster.id);
		
		clientResponse = Clientresponse(clientmaster_accountid=clientAccountId,iswebsiteworking=websiteOperational,iscallpicked=callAnswered,isonreminder=needReminder, wishtocontinue=wishToContinue,appointmenttime=appointmentTime,
			additionalemailid=additionalEmail,additionalphone1=additionalPhone1,additioanlphone2=additionalPhone2,responsedate=responseDate,createdate=createDate,updatedate=updateDate)
		clientResponse.save();
		print clientResponse.id
		
		if needReminder == "1":
			reminderDate = request.POST.get('reminderDate')
			print "reminderDate::"+reminderDate 
			if reminderDate == '':
				reminderDate = None
			callreminders = Callreminders(clientmaster_accountid=clientAccountId,date=reminderDate)
			callreminders.save()
		
		for reason in selected_reasons:
			clientresponsereasons = Clientresponsereasons(clientmaster_accountid=clientAccountId,reasonmaster=Reasonmaster.objects.get(id=reason))
			clientresponsereasons.save()
			print clientresponsereasons.id
		
		if wishToContinue == '0':
			terminationinitiationqueue = Terminationinitiationqueue(clientmaster_accountid=clientAccountId,createdate=createDate,updatedate=createDate);
			terminationinitiationqueue.save()
			
	context = RequestContext(request, {'clientaccountid':clientAccountId.accountid,'datasaved':'Y'})			
	#return index(request)
	return HttpResponse(template.render(context))