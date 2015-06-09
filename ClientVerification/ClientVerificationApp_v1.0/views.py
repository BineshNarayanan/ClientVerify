from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from ClientVerificationApp.models import Clientmaster,Reasonmaster

# Create your views here.
def index(request):
	template = loader.get_template('ClientVerificationApp/index.html')
	context = RequestContext(request, {})
	return HttpResponse(template.render(context))

def getClientDetails(request):
	template = loader.get_template('ClientVerificationApp/index.html')
	accountId=request.POST.get('txtAccountId')
	client = Clientmaster.objects.get(accountid = accountId)
	reasons = Reasonmaster.objects.all()
	print client.accountname
	context = RequestContext(request, {'client':client,'reasons':enumerate(reasons,start=1)})
	return HttpResponse(template.render(context))