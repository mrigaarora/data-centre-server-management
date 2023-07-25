from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
# Create your views here.

def index(request):
      if request.method=="POST":
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(request, username=username, password=password)
            if user is not None:
                  login(request,user)
                  return redirect('search')
            else:
                 messages.warning(request,("YOU'RE NOT AUTHORIZED"))
                 return redirect('index')
                 pass
      else:
            return render(request, 'index.html', {})


def search(request):

    rows = Rack.objects.all()
    form = RacksForm()
    
    if 'delete_id' in request.GET:
        delete_id = request.GET['delete_id']
        row = get_object_or_404(Rack, id=delete_id)
        row.delete()
        return redirect('search')  # Redirect to the same view to display the updated table
    
    if 'edit_id' in request.GET:
        edit_id = request.GET['edit_id']
        rack = get_object_or_404(Rack, id=edit_id)
        if request.method == 'POST':
            form = RacksForm(request.POST, instance=rack)
            if form.is_valid():
                form.save()
                return redirect('search')
            
    if request.method == 'POST':
        form = RacksForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search')  # Redirect to the same view to display the updated table
  

            
    return render(request, 'search.html', {'rows': rows,'form':form})




def com(request):
    rows = Company.objects.all()
    form=CompanyForm()

    if 'delete_id' in request.GET:
        delete_id = request.GET['delete_id']
        row = get_object_or_404(Company, company=delete_id)
        row.delete()
        return redirect('com')  # Redirect to the same view to display the updated table
    
    
    
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('com')  # Redirect to the same view to display the updated table
    return render(request, 'com.html', {'rows': rows,'form':form})

def comedit(request):
    if 'edit_id' in request.GET:
        edit_id = request.GET['edit_id']
        comp = get_object_or_404(Company, company=edit_id)
        form = CompanyForm(instance=comp)
        if request.method == 'POST':
            form = CompanyForm(request.POST, instance=comp)
            print(form)
            if form.is_valid():
                print(form.is_valid())
                form.save()
                return redirect('com')


def apps(request):
    company = request.GET.get('company')  # Get the value of the 'company' parameter from the URL
    servers = Server.objects.filter(server_make=company) if company else Server.objects.all()
    form=ServerForm()
    if 'delete_id' in request.GET:
        delete_id = request.GET['delete_id']
        server = get_object_or_404(Server, id=delete_id)
        server.delete()
        return render(request, 'apps.html', {'servers': servers,'form':form})  # Redirect to the same view to display the updated table
    if request.method == 'POST':
        form = ServerForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'apps.html', {'servers': servers,'form':form})  # Redirect to the same view to display the updated table
    return render(request, 'apps.html', {'servers': servers,'form':form})

def edit(request, edit_id):
    
    server = get_object_or_404(Server, id=edit_id)
    if request.method == 'POST':
        form = ServerForm(request.POST, instance=server)
        if form.is_valid():
            form.save()
            return redirect('apps')
    else:
        form = ServerForm(instance=server)
    
    context = {'form': form, 'server': server}
    return render(request, 'edit.html', context)
