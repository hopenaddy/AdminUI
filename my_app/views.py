from django.shortcuts import render, redirect
from my_app.models import Users
import uuid
from django.contrib import auth
from django.contrib.auth.decorators import login_required
import logging


logger=logging.getLogger(__name__)

def main_page(request):
    
    return redirect('index')

@login_required()
def index(request):
    users_list = Users.objects.all().order_by('id')
    context = {'users_list': users_list, 'username': auth.get_user(request).username}
    if "delete" in request.POST:
        user_id = request.POST['delete']
        Users.objects.filter(id=user_id).delete()
        logger.debug("%s delete user with id= %s" % (auth.get_user(request).username, user_id))
    return render(request, 'my_app/index.html', context)
    
def user_save(request, user):
    user.login = request.POST['login']
    user.fullname = request.POST['fullname']
    if not user.token: 
        user.token = uuid.uuid4()
        logger.debug("%s create user login= %s fullname= %s" % (auth.get_user(request).username, user.login, user.fullname))
    else:
        logger.debug("%s edit user login= %s fullname= %s" % (auth.get_user(request).username, user.login, user.fullname))        
    user.save()

def send_page(request, user):
    if "save" in request.POST:
        user_save(request, user)
        return redirect('index')
    return render(request, 'my_app/add.html', {'user': user, 'username': auth.get_user(request).username})

@login_required()
def add(request):
        user = Users()
        return send_page(request, user)

@login_required()    
def edit(request, id):
        user = Users.objects.get(id=id)
        return send_page(request, user)