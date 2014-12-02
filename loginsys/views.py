from django.shortcuts import render, redirect
from django.contrib import auth
import logging
from django.contrib.auth.forms import AuthenticationForm


logger=logging.getLogger(__name__)

def login(request):
	args ={}
	args["form"]=AuthenticationForm()
	redirect_to = request.REQUEST.get('next', '/')
	new_form=AuthenticationForm(request.POST)
	if "sing_in" in request.POST:
		username = request.POST.get("username","")
		password = request.POST.get("password","")
		user_log = auth.authenticate(username=username, password=password)
		if user_log is not None:
			auth.login(request, user_log)
			logger.debug("%s SignIn" % (auth.get_user(request).username))
			return redirect(redirect_to) 
		else:
			args['login_error'] = "wrong name or password"
			return render(request, 'login.html', args)
	else:
		return render(request, 'login.html', args)			

def logout(request):
	logger.debug("%s Log Out" % (auth.get_user(request).username))
	auth.logout(request)
	return redirect('/users/')
