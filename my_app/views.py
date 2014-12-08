from django.shortcuts import render, redirect
from my_app.models import *
import uuid
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import logging


logger=logging.getLogger(__name__)

def main_page(request):
    return redirect('index')

@login_required()
def index(request):
    user_list = User.objects.all().order_by('id')
    context = {'user_list': user_list, 'username': auth.get_user(request).username}
    if "delete" in request.POST:
        user_id = request.POST['delete']
        User.objects.filter(id=user_id).delete()
        logger.debug("%s delete user with id= %s" % (auth.get_user(request).username, user_id))
    return render(request, 'my_app/index.html', context)    

@login_required()    
def edit(request, id):
    user = User.objects.get(id=id)
    if "save" in request.POST:
        user.username = request.POST['login']
        user.first_name = request.POST['first']
        user.last_name = request.POST['last']
        logger.debug("%s edit user login= %s fullname= %s" % (auth.get_user(request).username, user.username, user.get_full_name()))
        user.save()
        return redirect('index')
    return render(request, 'my_app/add.html', {'user': user, 'username': auth.get_user(request).username})
        