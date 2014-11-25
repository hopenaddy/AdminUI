from django.shortcuts import render, redirect
from models import Users, Tokens
from django.contrib import auth

def main_page(request):
    return redirect('index')

def index(request):
    users_list = Users.objects.all().order_by('id')
    tokens_list = Tokens.objects.all().order_by('id')
    context = {'users_list': users_list, 'tokens_list':tokens_list, 'username': auth.get_user(request).username}
    if "delete" in request.POST:
        user_id = request.POST['delete']
        Users.objects.filter(id=user_id).delete()
    return render(request, 'my_app/index.html', context)

def user_save(request, user, tokens):
    user.login = request.POST['login']
    user.fullname = request.POST['fullname']
    user.save()
    tokens.token = request.POST['token']
    tokens.user_id = Users.objects.get(login=request.POST['login']).id
    tokens.save()

def send_page(request, user, tokens):
    if "save" in request.POST:
        user_save(request, user, tokens)
        return redirect('index')
    return render(request, 'my_app/add.html', {'user': user, 'username': auth.get_user(request).username})

def add(request):
    user = Users()
    tokens=Tokens()
    return send_page(request, user, tokens)
    
def edit(request, id):
    user = Users.objects.get(id=id)
    tokens = Tokens.objects.get(id=id)
    return send_page(request, user, tokens)
