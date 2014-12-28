import uuid
import logging
from my_app.models import *
from django.contrib import auth
from loginsys.views import add_token
from my_app.forms import PermissionForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required


logger=logging.getLogger(__name__)

def main_page(request):
    return redirect('index')

@login_required()
def index(request):
    user_list = User.objects.all().order_by('id')
    context = {'user_list': user_list}
    if "delete" in request.POST and request.POST['delete'] != "1":
        user_id = request.POST['delete']
        if request.user.has_perm('auth.delete_user') or int(user_id) == request.user.id:
            User.objects.filter(id=user_id).delete()
            logger.debug("%s delete user with id= %s" % (auth.get_user(request).username, user_id))      
    return render(request, 'my_app/index.html', context)  

@login_required() 
def edit(request, id):
    check_perm = request.user.has_perm('auth.change_user')
    if check_perm or request.user.id==int(id):
        user = User.objects.get(id=id)
        if "del" in request.POST:
            logger.debug("%s lost token - %s" % (user.username, Profile.objects.get(id=request.POST["del"]).token))
            Profile.objects.filter(id=request.POST["del"]).delete()
        if "add" in request.POST:
            add_token(id)
            logger.debug("%s got new token" % (user.username))
        if "save" in request.POST:
            user.username = request.POST['login']
            user.first_name = request.POST['first']
            user.last_name = request.POST['last']
            logger.debug("%s edit user login= %s fullname= %s" % (auth.get_user(request).username, user.username, user.get_full_name()))
            user.save()
            return redirect('index')
        return render(request, 'my_app/add.html', {'user': user, 'username': auth.get_user(request).username})
    return redirect('index') 

@permission_required("auth.change_permission")        
def permission(request, id):
    user = User.objects.get(id=id)
    args = {}
    args['this_name'] = user.username
    initial={'change_permission':False, 'change_user':False, 'add_user':False, 'delete_user':False}
    for i in initial:
        initial[i] = user.has_perm('auth.' + i)  
    args['form'] = PermissionForm(initial)
    if "save" in request.POST:
        user.user_permissions.clear()
        for a in request.POST:
            if Permission.objects.filter(codename=str(a)):
                user.user_permissions.add(Permission.objects.get(codename=str(a)))
        logger.debug("%s changed permissions for %s" % (auth.get_user(request).username, user.username))
        return redirect('index') 
    return render(request, 'my_app/permission.html', args)        