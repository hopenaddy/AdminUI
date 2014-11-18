from django.shortcuts import render, redirect
from django.contrib import auth

def login(request):
	args ={}
	if "sing_in" in request.POST:
		username = request.POST.get("username","")
		password = request.POST.get("password","")
		user_log = auth.authenticate(username=username, password=password)
		if user_log is not None:
			auth.login(request, user_log)
			return redirect('/users/') 
		else:
			args['login_error'] = "wrong name or password"
			return render(request, 'login.html', args)
	else:
		return render(request, 'login.html')			

def logout(request):
	auth.logout(request)
	return redirect('/users/')				