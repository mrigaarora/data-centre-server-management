from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import TableForm
from .models import Table

# Create your views here.


def search(request):
    if request.method == 'POST':
        form = TableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('search')  # Redirect to the same view to display the updated table
    else:
        form = TableForm()
    
    rows = Table.objects.all()
    if 'delete_id' in request.GET:
        delete_id = request.GET['delete_id']
        row = get_object_or_404(Table, id=delete_id)
        row.delete()
        return redirect('search')  # Redirect to the same view to display the updated table
    if 'edit_id' in request.GET:
        edit_id = request.GET['edit_id']
        row = get_object_or_404(Table, id=edit_id)
        if request.method == 'POST':
            edit_form = TableForm(request.POST, instance=row)
            if edit_form.is_valid():
                edit_form.save()
                return redirect('search')
        else:
            edit_form = TableForm(instance=row)
        return render(request, 'search.html', {'form': form, 'rows': rows, 'edit_form': edit_form, 'edit_id': edit_id})

    return render(request, 'search.html', {'form': form, 'rows': rows, 'edit_form': None, 'edit_id': None})



def apps(request):
    return render(request,'apps.html')

def index(request):
	if request.method=="POST":
		username=request.POST['username']
		password=request.POST['password']
		user=authenticate(request, username=username, password=password)
		if user is not None:
			login(request,user)
			return render(request,'search.html')
		else:
			messages.warning(request,("YOU'RE NOT AUTHORIZED"))
			return redirect('index')
            
			pass
	else:
		return render(request, 'index.html', {})
def com(request):
     return render(request,'com.html')





