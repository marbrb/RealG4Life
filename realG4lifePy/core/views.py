from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt   #Skip the csrf middleware protection
from django.http import HttpResponse, HttpResponseServerError
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from core.models import User
import pika
from django.contrib.auth.views import login, logout

@login_required(login_url='/login/')
def home(request):
    #session = Session.objects.get(session_key=request.POST.get('sessionid'))

    return render(request, 'home.html', {'session': "proximamente gente."})



def login(request):
    pass

def logout(request):
    #logout(request)
    return HttpResponseRedirect('/')




@csrf_exempt    #ignorara la proteccion csrf
def node_api(request):
    try:
        #Get user from session ID
        session = Session.objects.all.get(session_key=request.POST.get('sessionid'))
        userID  = session.get_decoded().get('_auth_user_id')
        user = User.objects.get(id=userID)

        # Comments.objects.create(user=user)

        temp_comment = request.POST.get('comment')

        #RabbitMQ
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))

        #create recipient queue
        channel.queue_declare(queue='culo')

        #send message to 'culo' recipient
        channel.basic_publish(exchange='', routing_key='culo', body=temp_comment)

        connection.close()

        return HttpResponse("Todo nice gente.")

    except:
        return HttpResponseServerError(str(e))
