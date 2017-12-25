from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . import services
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.http import HttpResponseBadRequest
class NotesPage(generic.TemplateView):
	@csrf_exempt
	def get(self,request):
		notes = services.get_notes_all()
		return render(request,'base.html',{'notes':notes})


# @ajax_required
def autosaveAlert(request):
	if request.is_ajax():
		messages.info(request,"Autosaved")
		return render(request,"messages.html")
	return HttpResponseBadRequest()