import json
import uuid
import logging
from my_app.models import *
from django.contrib import auth
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


logger=logging.getLogger(__name__)

def add_token(id):
	profile = Profile()
	profile.user_id=id 
	profile.token = uuid.uuid4()
	profile.save()

def login(request):
	args ={}
	redirect_to = request.REQUEST.get('next', '/')
	args["form"] = AuthenticationForm()
	if "sing_in" in request.POST:
		new_form=AuthenticationForm(data=request.POST)
		if new_form.is_valid():
			auth.login(request, new_form.user_cache)
			logger.debug("%s SignIn" % (auth.get_user(request).username))
			return redirect(redirect_to)
		args["form"] = new_form		
	return render(request, 'login.html', args)
		
@csrf_exempt
def get_data(request):
	return send_user(request.user)

def send_user(user):
	tokens = user.prof.values_list('token', flat=True)
	data = {
		'id' : user.id,
		'username' : user.username,
		'fullname' : user.get_full_name(),
		'token' : tokens
		}
	return HttpResponse(json.dumps(data), content_type = "application/json")

@csrf_exempt
def authorize(request):
    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        return send_user(user)
    else:
        return HttpResponse("None")			

@csrf_exempt
def auth_check(request):
	if request.user.is_authenticated():
	    return HttpResponse("OK")
	else:
		return HttpResponse("None")

def logout(request):
	logger.debug("%s Log Out" % (auth.get_user(request).username))
	auth.logout(request)
	return redirect(reverse('index'))

def registration(request):
	args ={}
	args["form"] = UserCreationForm()
	if "registration" in request.POST:
		new_form=UserCreationForm(request.POST)
		if new_form.is_valid():
			new_form.save()
			new_user=auth.authenticate(username=new_form.cleaned_data['username'], password=new_form.cleaned_data['password2'])
			if request.user.is_authenticated():
				logger.debug("%s creat user login= %s" % (request.user.username, new_user.username))
				return redirect(reverse('index'))
			logger.debug("%s was registrated" % new_user.username)
			auth.login(request, new_user)
			return redirect(reverse('index'))
		args['form']=new_form	
	return render(request, 'registration.html', args)
