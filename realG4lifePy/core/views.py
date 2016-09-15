import pika
from core.models import Comment, User
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt   #Skip the csrf middleware protection
from django.http import HttpResponse, HttpResponseServerError, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate, login, logout
from core.forms import FormLogin

#@login_required(login_url='/login/')
def home(request):
    #session = Session.objects.get(session_key=request.POST.get('sessionid'))
    comments = Comment.objects.select_related().all()[0:100]
    return render(request, 'home.html', {'comments': comments})


def loginWithForm(request):
    if request.method == 'POST':
        form = FormLogin(request.POST)

        if form.is_valid():
            cd = form.cleaned_data  #diccionario de datos que se enviaron bin en el form
            username = cd['username']
            password = cd['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:

                return render(request, 'login.html', {'form': form})
        else:
            return render(request, 'login.html', {'form': form})

    elif request.method == 'GET':
        return render(request, 'login.html', {'form': FormLogin})





def logout_view(request):
    #request.user
    logout(request)  #session data for the current request is completely cleaned out
    return HttpResponseRedirect('/')
    #TODO: hacer un boton de logout





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
