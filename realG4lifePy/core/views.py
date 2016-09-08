from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt   #Skip the csrf middleware protection
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.sessions.models import Session

def home(request):
    #session = Session.objects.get(session_key=request.POST.get('sessionid'))

    return render(request, 'home.html', {'session': "proximamente gente."})


@csrf_exempt    #ignorara la proteccion csrf
def node_api(request):
    session = Session.objects.all.get(session)
