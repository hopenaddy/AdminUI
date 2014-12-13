from django.shortcuts import render, redirect
from django.contrib import auth
from django.core.urlresolvers import reverse
import logging
import uuid
from my_app.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


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
		else: 
			args["form"] = new_form		
	return render(request, 'login.html', args)			

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
			id=new_user.id
			add_token(id)
			if request.user.is_authenticated():
				logger.debug("%s creat user login= %s" % (request.user.username, new_user.username))
				return redirect(reverse('index'))
			logger.debug("%s was registrated" % new_user.username)
			auth.login(request, new_user)
			return redirect(reverse('index'))
		else:
			args['form']=new_form	
	return render(request, 'registration.html', args)