from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt   #Skip the csrf middleware protection
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.sessions.models import Session

def home(request):
    #session = Session.objects.get(session_key=request.POST.get('sessionid'))

    return render(request, 'home.html', {'session': "este debería ser el session ID que me da david el inutil"})
