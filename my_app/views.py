from django.shortcuts import render, redirect
from my_app.models import *
from loginsys.views import add_token
from django.core.urlresolvers import reverse
import uuid
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
import logging


logger=logging.getLogger(__name__)

def main_page(request):
    return redirect('index')

@login_required()
def index(request):
    user_list = User.objects.all().order_by('id')
    context = {'user_list': user_list, 'username': auth.get_user(request).username}
    return render(request, 'my_app/index.html', context)

@login_required()
@permission_required("auth.delete_user")
def delete(request, id):
    User.objects.filter(id=id).delete()
    logger.debug("%s delete user with id= %s" % (auth.get_user(request).username, id))
    return redirect(reverse('index'))     

@login_required() 
def edit(request, id):
    if request.user.has_perm('auth.change_user') or request.user.id==int(id):
        user = User.objects.get(id=id)
        if "del" in request.POST:
            Profile.objects.filter(id=request.POST["del"]).delete()
        if "add" in request.POST:
            add_token(id)
        if "save" in request.POST:
            user.username = request.POST['login']
            user.first_name = request.POST['first']
            user.last_name = request.POST['last']
            logger.debug("%s edit user login= %s fullname= %s" % (auth.get_user(request).username, user.username, user.get_full_name()))
            user.save()
            return redirect('index')
        return render(request, 'my_app/add.html', {'user': user, 'username': auth.get_user(request).username})
    return redirect('/auth/login/?next=%s' % request.path)    
        