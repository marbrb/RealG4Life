import pika
from core.models import Comments, User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt   #Skip the csrf middleware protection
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login, logout

#@login_required(login_url='/login/')
def home(request):
    #session = Session.objects.get(session_key=request.POST.get('sessionid'))

    return render(request, 'home.html', {'comments': ['perrito','david la zorra']})



def login_view(request):
    #user --- authenticate(user=user, password=pass) --- return a User object
    #login(request, user)
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)   #si las credenciales no sirven retorna None
    if user is not None:
        login(request, user)    # saves the user’s ID in the session
        return HttpResponse("Si sirvio gente")
    else:
        return HttpResponse("No sirvio gente")


def logout_view(request):
    """Para hacer logout el usuario debio entrar con la funcion login"""
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
