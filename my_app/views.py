from django.shortcuts import render, redirect
from my_app.models import Users
import uuid
from django.contrib import auth

def main_page(request):
    return redirect('index')

def index(request):
    if request.user.is_authenticated():
        users_list = Users.objects.all().order_by('id')
        context = {'users_list': users_list, 'username': auth.get_user(request).username}
        if "delete" in request.POST:
            user_id = request.POST['delete']
            Users.objects.filter(id=user_id).delete()
        return render(request, 'my_app/index.html', context)
    return redirect('/auth/login/?next=%s' % request.path)

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

def add(request):
    if request.user.is_authenticated():
        user = Users()
        return send_page(request, user)
    return redirect('/auth/login/?next=%s' % request.path)
    
def edit(request, id):
    if request.user.is_authenticated():
        user = Users.objects.get(id=id)
        return send_page(request, user)
    return redirect('/auth/login/?next=%s' % request.path)
