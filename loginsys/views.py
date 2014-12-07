from django.shortcuts import render, redirect
from django.contrib import auth
import logging
import uuid
from my_app.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User


logger=logging.getLogger(__name__)

def login(request):
	args ={}
	redirect_to = request.REQUEST.get('next', '/')
	new_form=AuthenticationForm(data=request.POST)
	args["form"] = new_form
	if "sing_in" in request.POST:
		if new_form.is_valid():
			auth.login(request, new_form.user_cache)
			print new_form.user_cache
			logger.debug("%s SignIn" % (auth.get_user(request).username))
			return redirect(redirect_to)	
	return render(request, 'login.html', args)			

def logout(request):
	logger.debug("%s Log Out" % (auth.get_user(request).username))
	auth.logout(request)
	return redirect('/users/')

def registration(request):
	args ={}
	args["form"] = UserCreationForm()
	if "registration" in request.POST:
		new_form=UserCreationForm(request.POST)
		if new_form.is_valid():
			new_form.save()
			logger.debug("created user login= %s" % new_form.cleaned_data['username'])
			new_form=auth.authenticate(username=new_form.cleaned_data['username'], password=new_form.cleaned_data['password2'])
			auth.login(request, new_form)
			id=User.objects.last().id
			profile = Profile()
			profile.user_id=id 
			profile.token = uuid.uuid4()
			profile.save()
			return redirect('/')
		else:
			args['form']=new_form	
	return render(request, 'registration.html', args)