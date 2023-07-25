from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import *
from .models import *
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import JsonResponse

def check_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        # Replace 'your_password_here' with the actual password to check against
        if password == 'cpcb@2023':
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Incorrect password.'})
        
# Create your views here.
@user_passes_test(lambda u: u.is_staff)  # Only allow staff members to access this view
def create_superuser(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            messages.success(request, f'Superuser {user.username} has been created successfully!')
            return redirect("index")
    else:
        form = UserCreationForm()

    return render(request, 'create_superuser.html', {'form': form})

def index(request):
      if request.method=="POST":
            print("hello")
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

@login_required
def search(request):

    #DELETE/EDIT/ADD RACK ON NAVBAR
    racks=Rack.objects.all()
    rack_form = RacksForm()
    if 'edit_R' in request.GET:
        print("hello")
        edit_id = request.GET.get('edit_R')
       
        rack = get_object_or_404(Rack, id=edit_id)
        print(rack)
    
        if request.method == 'POST':
            if 'edit_R' in request.GET:
                rack_form = RacksForm(request.POST, instance=rack)
                print(rack)
                if rack_form.is_valid():
                    rack_form.save()
                    return redirect('search')
        else:
            rack_form = RacksForm(instance=rack)


    if 'add_rack' in request.GET:
        if request.method == 'POST':
            rack_form = RacksForm(request.POST)
            if rack_form.is_valid():
                rack_form.save()
                return redirect('search')
            
        else:
            rack_form = RacksForm()

    if 'delete_R' in request.GET:
        delete_id = request.GET.get('delete_R')
        row = get_object_or_404(Rack, id=delete_id)
        print("Deleting row:", row)  # Debug print statement
        row.delete()
        return redirect('search')

    

    #DELETE/EDIT/ADD COMPANY ON NAVBAR
    companies=Company.objects.all()
    company_form = CompanyForm()
    if 'edit_C' in request.GET:
        edit_id = request.GET['edit_C']
        comp = get_object_or_404(Company, id=edit_id)
       
        if request.method == 'POST':
            company_form = CompanyForm(request.POST, instance=comp)
            if company_form.is_valid():
                company_form.save() 
            return redirect('com')
    if 'add_company' in request.GET:
        if request.method == 'POST':
            company_form = CompanyForm(request.POST)
            if company_form.is_valid():
                company_form.save()
                return redirect('com')
    if 'delete_C' in request.GET:
        delete_id = request.GET['delete_C']
        comp = get_object_or_404(Company, id=delete_id)
        comp.delete()
        return redirect('com')
            
    #DELETE/EDIT/ADD SERVER ON NAVBAR       
    navservers=Server.objects.all()
    server_form = ServerForm()
    if request.method == 'POST':
        server_form = ServerForm(request.POST, request.FILES)
        if server_form.is_valid():
            server_form.save()
            return redirect('apps')
        
    if 'delete_S' in request.GET:
        delete_id = request.GET['delete_S']
        server = get_object_or_404(Server, id=delete_id)
        server.delete()
        return redirect('apps')
    

    #LOGOUT
    if 'logout' in request.GET:
        logout(request)
        return redirect('index') 
    
    rows = Rack.objects.all()
    form = RacksForm()
    
    #DELETE ON PAGE
    if 'delete_id' in request.GET:
        delete_id = request.GET['delete_id']
        row = get_object_or_404(Rack, id=delete_id)
        row.delete()
        return redirect('search')  #Redirect to the same view to display the updated table
    
    #EDIT ON PAGE
    if 'edit_id' in request.GET:
        edit_id = request.GET['edit_id']
        rack = get_object_or_404(Rack, id=edit_id)
        form = RacksForm(instance=rack)  #Pre-populate the form with existing data

    #ADD ON PAGE
    if request.method == 'POST':
        if 'edit_id' in request.GET:  #If an edit_id is present in the URL, handle the form submission for editing
            edit_id = request.GET['edit_id']
            rack = get_object_or_404(Rack, id=edit_id)
            form = RacksForm(request.POST, instance=rack)
        else:  # Otherwise, handle the form submission for adding a new row
            form = RacksForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('search')  #Redirect to the same view to display the updated table
    
   


    return render(request, 'search.html',  {
    'rows': rows,
    'form': form,
    'rack_form': rack_form,
    'racks': racks,
    'company_form': company_form,
    'companies': companies,'navservers':navservers,'server_form':server_form })





def com(request):
    #DELETE/EDIT/ADD RACK ON NAVBAR
    racks=Rack.objects.all()
    rack_form = RacksForm()
    if 'edit_R' in request.GET:
        edit_id = request.GET.get('edit_R')
        rack = get_object_or_404(Rack, id=edit_id)
    
        if request.method == 'POST':
            if 'edit_R' in request.GET:
                rack_form = RacksForm(request.POST, instance=rack)
                if rack_form.is_valid():
                    rack_form.save()
                    return redirect('search')
        else:
            rack_form = RacksForm(instance=rack)


    if 'add_rack' in request.GET:
        if request.method == 'POST':
            rack_form = RacksForm(request.POST)
            if rack_form.is_valid():
                rack_form.save()
                return redirect('search')
            
        else:
            rack_form = RacksForm()

    if 'delete_R' in request.GET:
        delete_id = request.GET.get('delete_R')
        row = get_object_or_404(Rack, id=delete_id)
        print("Deleting row:", row)  # Debug print statement
        row.delete()
        return redirect('search')

    #DELETE/EDIT/ADD COMPANY ON NAVBAR
    companies=Company.objects.all()
    company_form = CompanyForm()
    if 'edit_C' in request.GET:
        edit_id = request.GET['edit_C']
        comp = get_object_or_404(Company, id=edit_id)
       
        if request.method == 'POST':
            company_form = CompanyForm(request.POST, instance=comp)
            if company_form.is_valid():
                company_form.save() 
            return redirect('com')

    if 'add_company' in request.GET:
        if request.method == 'POST':
            company_form = CompanyForm(request.POST)
            if company_form.is_valid():
                company_form.save()
                return redirect('com')
    if 'delete_C' in request.GET:
        delete_id = request.GET['delete_C']
        comp = get_object_or_404(Company, id=delete_id)
        comp.delete()
        return redirect('com')
            
    #DELETE/EDIT/ADD SERVER ON NAVBAR       
    navservers=Server.objects.all()
    server_form = ServerForm()
    if request.method == 'POST':
        server_form = ServerForm(request.POST, request.FILES)
        if server_form.is_valid():
            server_form.save()
            return redirect('apps')
        
    if 'delete_S' in request.GET:
        delete_id = request.GET['delete_S']
        server = get_object_or_404(Server, id=delete_id)
        server.delete()
        return redirect('apps')
    

    rack_id = request.GET.get('rack', None)
    form=CompanyForm()
    
    
    #DELETE ON PAGE
    if 'delete_id' in request.GET:
        delete_id = request.GET['delete_id']
        try:
            row = Company.objects.get(id=delete_id)
            
            if rack_id and rack_id != 'None':
                if rack_id:
                    row.racks.remove(rack_id)  # Remove the rack from the company's racks field
                    row.save() # Save the modified company instance
                else:
                    pass # If the company is not associated with the specified rack, do nothing
            else:
                # If no rack is specified, delete the entire company row
                row.delete()
        
        except (ValueError, ObjectDoesNotExist):
            pass
        if rack_id:
            redirect_url = reverse('com') + '?rack=' + rack_id
        else:
            redirect_url = reverse('com')
            
        return redirect(redirect_url)  # Redirect to the same view to display the updated table
    #EDIT ON PAGE
    if 'edit_id' in request.GET:
        edit_id = request.GET['edit_id']
        comp = get_object_or_404(Company, id=edit_id)
        form = CompanyForm(instance=comp)
        if request.method == 'POST':
            form = CompanyForm(request.POST, instance=comp)
            if form.is_valid():
                form.save()
                
            if rack_id:
                redirect_url = reverse('com') + '?rack=' + str(rack_id)
            else:
                redirect_url = reverse('com')
            
            return redirect(redirect_url)
     #ADD ON PAGE       
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('com')  # Redirect to the same view to display the updated table
    
    rows = Company.objects.filter(racks=rack_id) if rack_id else Company.objects.all()
    
    
    current_rack = None
    if rack_id:
        current_rack = get_object_or_404(Rack, id=rack_id)

    return render(request, 'com.html',  {
    'rows': rows,
    'form': form,
    'rack_form': rack_form,
    'racks': racks,
    'company_form': company_form,
    'companies': companies,'navservers':navservers,'server_form':server_form, 'current_rack':current_rack,'rack_id':rack_id})

    





def apps(request):
    #DELETE/EDIT/ADD RACK ON NAVBAR
    racks=Rack.objects.all()
    rack_form = RacksForm()
    if 'edit_R' in request.GET:
        print("hello")
        edit_id = request.GET.get('edit_R')
       
        rack = get_object_or_404(Rack, id=edit_id)
        print(rack)
    
        if request.method == 'POST':
            if 'edit_R' in request.GET:
                rack_form = RacksForm(request.POST, instance=rack)
                print(rack)
                if rack_form.is_valid():
                    rack_form.save()
                    return redirect('search')
        else:
            rack_form = RacksForm(instance=rack)


    if 'add_rack' in request.GET:
        if request.method == 'POST':
            rack_form = RacksForm(request.POST)
            if rack_form.is_valid():
                rack_form.save()
                return redirect('search')
            
        else:
            rack_form = RacksForm()

    if 'delete_R' in request.GET:
        delete_id = request.GET.get('delete_R')
        row = get_object_or_404(Rack, id=delete_id)
        print("Deleting row:", row)  # Debug print statement
        row.delete()
        return redirect('search')

    

    #DELETE/EDIT/ADD COMPANY ON NAVBAR
    companies=Company.objects.all()
    company_form = CompanyForm()
    if 'edit_C' in request.GET:
        edit_id = request.GET['edit_C']
        comp = get_object_or_404(Company, id=edit_id)
       
        if request.method == 'POST':
            company_form = CompanyForm(request.POST, instance=comp)
            if company_form.is_valid():
                company_form.save() 
            return redirect('com')
    if 'add_company' in request.GET:
        if request.method == 'POST':
            company_form = CompanyForm(request.POST)
            if company_form.is_valid():
                company_form.save()
                return redirect('com')
    if 'delete_C' in request.GET:
        delete_id = request.GET['delete_C']
        comp = get_object_or_404(Company, id=delete_id)
        comp.delete()
        return redirect('com')
            
    #DELETE/EDIT/ADD SERVER ON NAVBAR       
    navservers=Server.objects.all()
    server_form = ServerForm()
    if request.method == 'POST':
        server_form = ServerForm(request.POST, request.FILES)
        if server_form.is_valid():
            server_form.save()
            return redirect('apps')
        
    if 'delete_S' in request.GET:
        delete_id = request.GET['delete_S']
        server = get_object_or_404(Server, id=delete_id)
        server.delete()
        return redirect('apps')
    

    

    form = ServerForm()
    rack_id = request.GET.get('rack',None)
    company_name = request.GET.get('company', None)

    servers = Server.objects.all()

    if rack_id and rack_id != 'None':
        try:
            servers = servers.filter(rack_no__id=int(rack_id))
        except (ValueError, ObjectDoesNotExist):
            pass

    if company_name:
        servers = servers.filter(server_make=company_name)


   

    if 'delete_id' in request.GET:
        delete_id = request.GET['delete_id']
        server = get_object_or_404(Server, id=delete_id)
        server.delete()
        return redirect('apps')
    
    if request.method == 'POST':
        form = ServerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('apps') # Redirect to the same view to display the updated table
    current_rack = None
    if rack_id is not None and rack_id.isnumeric():
        current_rack = get_object_or_404(Rack, id=rack_id)

    # Fetch the Company object corresponding to the company_id
    current_company = None
    if company_name:
        current_company = get_object_or_404(Company, id=company_name)


    return render(request, 'apps.html', {'servers': servers, 'form': form,'rack_form':rack_form,'racks':racks,'company_form': company_form,
    'companies': companies, 'navservers':navservers,'server_form':server_form,'current_rack':current_rack,'current_company':current_company  })




def edit(request, edit_id):
    
    server = get_object_or_404(Server, id=edit_id)
    if request.method == 'POST':
        form = ServerForm(request.POST,request.FILES, instance=server)
        if form.is_valid():
            form.save()
            
            return redirect('apps')
    else:
        form = ServerForm(instance=server)
    
    context = {'form': form, 'server': server}
    return render(request, 'edit.html', context)






def searchbar(request):
    form = ServerForm()
    servers = None
   
    
    if request.method == 'GET':
        search = request.GET.get('search')
        
        if search:
            servers = Server.objects.filter(
                Q(applications_installed__icontains=search)|
                Q(portals_running__icontains=search)|
                Q(specification__icontains=search)|
                Q(ip_address__contains=search) | 
                Q(server_model__icontains=search)| 
                Q(server_serial_no__icontains=search)| 
                Q(warranty_amc_status__icontains=search)| 
                Q(ownership__display_name__icontains=search)| 
                Q(server_model__icontains=search)|
                Q(server_make__company__icontains=search) |  
                Q(rack_no__Rack__icontains=search)|
                Q(num_of_vms__contains=search)
            )
    
    
    return render(request, 'apps.html', {'servers': servers, 'form': form, 'search_query': search})

