from django.contrib import messages
from app.models import Profile, Record
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import View

class HomeView(View):
    def get(self, request):
        context = {
            "patients" : Profile.objects.all(),
        }
        return render(request, 'home/home.html', context)

class AnalyticsView(View):
    def get(self, request, id):
        context = {
            "profile" : Profile.objects.get(id=id)
        }
        return render(request, 'analytics/home.html', context)

class NewPatient(View):
    def get(self, request):
        return render(request, 'home/addpatient.html')

    def post(sefl, request):
        messages.info(request, 'New patient record has been added')
        return HttpResponseRedirect('/')