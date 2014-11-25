from django.shortcuts import render, redirect
from my_app.models import Users
import uuid
from django.contrib import auth
from django.contrib.auth.decorators import login_required

def main_page(request):
    return redirect('index')

@login_required()
def index(request):
    users_list = Users.objects.all().order_by('id')
    context = {'users_list': users_list, 'username': auth.get_user(request).username}
    if "delete" in request.POST:
        user_id = request.POST['delete']
        Users.objects.filter(id=user_id).delete()
    return render(request, 'my_app/index.html', context)
    
def user_save(request, user):
    user.login = request.POST['login']
    user.fullname = request.POST['fullname']
    if not user.token: 
        user.token = uuid.uuid4()
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