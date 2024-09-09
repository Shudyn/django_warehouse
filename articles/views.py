from django.shortcuts import render
from django.shortcuts import redirect
from django.db import models
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib import messages
from .models import *
from .forms import *

def login(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = {'username': request.POST["username"], 'password':request.POST["password"]}
            user = authenticate(request, username=form['username'], password=form['password'])
            if user is None:
                form['errors'] = u'Неправильно введен логин или пароль'
                return render(request, 'login.html', {'form': form})
            else:
                auth_login(request, user)
                return redirect(archive)
        else:
            return render(request, 'login.html', {})
    else:
        return redirect(archive)

def logout_view(request):
    logout(request)
    return redirect(login)

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def no_access(request):
    return render(request, 'noaccess.html')

def client(request):
    objs = clients.objects.all()
    if request.method == "POST":
        form = NewClient(request.POST)
        if form["name"] and form["phone_number"]:
            if form.is_valid():
                form.save()
                return render(request, 'newclients.html', {'objs':objs})
            else:
                form['errors'] = u"Введено недостаточно данных"
                return render(request, 'newclients.html', {'objs':objs})
        else:
            return render(request, 'newclients.html', {'objs':objs})
    else:
        return render(request, 'newclients.html', {'objs':objs})
	    
def contracts(request):
    objs = Contracts.objects.all()
    if request.method == "POST":
        form = NewContract(request.POST)
        if form["operation_type"] and form["clients_client_id"]:
            if True:
                form.save()
                return render(request, 'newcontracts.html', {'objs':objs})
            else:
                form['errors'] = u"Введено недостаточно данных"
                return render(request, 'newcontracts.html', {'objs':objs})
        else:
            return render(request, 'newcontracts.html', {'objs':objs})
    else:
        return render(request, 'newcontracts.html', {'objs':objs})
    

def contrpaper(request, contract_id):
    display_entry = Contracts.objects.get(contract_id=contract_id)
    return render(request, 'newcontrpaper.html', {"contracts":display_entry})

def deliveries(request):
    objs = Deliveries.objects.all()
    return render(request, 'newdeliveries.html', {'objs':objs})

def finances(request):
    if request.user.is_staff:
        objs = Finances.objects.all()
        return render(request, 'newfinances.html', {'objs':objs})
    else:
        return render(request, 'noaccess.html')
    
def jobs(request):
    objs = Jobs.objects.all()
    return render(request, 'newjobs.html', {'objs':objs})

def operations(request):
    objs = OperationsJournal.objects.all()
    return render(request, 'newopjournal.html', {'objs':objs})

def registry(request):
    objs = Registry.objects.all()
    return render(request, 'newregistry.html', {'objs':objs})

def suppliers(request):
    objs = Suppliers.objects.all()
    return render(request, 'newsuppliers.html', {'objs':objs})

def valuables(request):
    objs = ValuablesData.objects.all()
    return render(request, 'newvaluables.html', {'objs':objs})

def worker(request):
    objs = Worker.objects.all()
    return render(request, 'newworker.html', {'objs':objs})

def edit_entry(request, client_id):
    display_entry = clients.objects.get(client_id=client_id)
    return render(request, 'newclients_edit.html', {"clients":display_entry})
              
def update_entry(request, client_id):
    update_entry = clients.objects.get(client_id=client_id)
    form = client_forms(request.POST, instance = update_entry)
    if form.is_valid:
        form.save()
        messages.success(request, "Запись успешно обновлена")
        return render(request, 'newclients_edit.html', {"clients":update_entry})

