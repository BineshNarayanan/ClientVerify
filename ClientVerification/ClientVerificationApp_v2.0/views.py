from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext, loader
from ClientVerificationApp.models import Clientmaster
from ClientVerificationApp.models import Reasonmaster

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
	
	context = RequestContext(request, {'client':client,'reasonswoy':enumerate(reasonswoy,start=1),'reasonswon':enumerate(reasonswon,start=1)})
	return HttpResponse(template.render(context))