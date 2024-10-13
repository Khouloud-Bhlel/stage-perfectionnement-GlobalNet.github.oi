import folium
from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
from .forms import ServiceForm
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import *
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
# import view sets from the REST framework
from rest_framework import viewsets
from django.contrib.auth.decorators import login_required


def index(request):
    # Create Map Object
    m = folium.Map(location=[36.80969919046897, 10.178292643895002], zoom_start=11)

    # Add markers
    folium.Marker([36.88827509199517, 10.325250397827855], popup='GlobalNet Taieb Mhiri').add_to(m)
    folium.Marker([36.87056260487405, 10.247767629874073], popup='GlobalNet Elec plus ').add_to(m)
    folium.Marker([36.86041244142929, 10.275317068615673], popup='Globalnet El Wahat').add_to(m)
    folium.Marker([36.83261401968672, 10.325078922746998], popup='GlobalNet Sbi Kram').add_to(m)
    folium.Marker([36.82352451367367, 10.314742119738725], popup='Globalnet Habib Bourguiba').add_to(m)
    folium.Marker([36.85851629198035, 10.164454042677344], popup='Globalnet Avenue Hédi Nouira').add_to(m)
    folium.Marker([36.85802277955676, 10.194336973365857], popup='Globalnet Ariana').add_to(m)
    folium.Marker([36.83620965871203, 10.210091050603783], popup='Globalnet Siège Social').add_to(m)
    folium.Marker([36.83127248673149, 10.205097180288057], popup='2N-TT / 2N-GlobalNet / 2N-Ooredoo / 2N-Hexabyte / 2N-AmazonTV').add_to(m)
    folium.Marker([36.821439970231786, 10.193827342668579], popup='Globalnet Lotissement Ennassim Montplaisir ').add_to(m)
    folium.Marker([36.817230670108664, 10.181865505937651], popup='Globalnet 112 Av. de La Liberté').add_to(m)
    folium.Marker([36.76081859878098, 10.213838869667331], popup='Globalnet Ibn Sina').add_to(m)
    folium.Marker([36.741646415747425, 10.307189738000133], popup='Globalnet Boumhal Bassatine').add_to(m)
    folium.Marker([36.7202426422909, 10.232042457711284], popup='Globalnet El Mourouj ').add_to(m)
    folium.Marker([36.80623730155562, 10.114700958113426], popup='Globalnet denden').add_to(m)
    folium.Marker([36.69601938554935, 10.594399499846414], popup='Globalnet béni Khalled').add_to(m)
    folium.Marker([36.41803628922465, 10.199003247398595], popup='Globalnet Zaghouan').add_to(m)
    
    # Get HTML Representation of Map Object
    map_html = m._repr_html_()
    
    context = {
        'map_html':   map_html,
    }
    return render(request, 'base.html', context)

def display_map(request):
    # Extract the 'goto' parameter from the URL
    goto_service = request.GET.get('goto', '')

    # Create Map Object
    m = folium.Map(location=[36.80969919046897, 10.178292643895002], zoom_start=11)

    # Add markers based on the 'goto' parameter
    if goto_service == 'GlobalNet Taieb Mhiri':
        folium.Marker([36.88827509199517, 10.325250397827855], popup='GlobalNet Taieb Mhiri').add_to(m)
        m.fit_bounds([[36.88827509199517, 10.325250397827855]])  # Adjust zoom to fit this marker
    elif goto_service == 'GlobalNet Elec plus':
        folium.Marker([36.87056260487405, 10.247767629874073], popup='GlobalNet Elec plus ' ).add_to(m)
        m.fit_bounds([[36.87056260487405, 10.247767629874073]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet El Wahat':
        folium.Marker([36.86041244142929, 10.275317068615673], popup='Globalnet El Wahat').add_to(m)
        m.fit_bounds([[36.86041244142929, 10.275317068615673]])  # Adjust zoom to fit this marker
    elif goto_service == 'GlobalNet Sbi Kram':
        folium.Marker([36.83261401968672, 10.325078922746998], popup='GlobalNet Sbi Kram').add_to(m)
        m.fit_bounds([[36.83261401968672, 10.325078922746998]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet Habib Bourguiba':
        folium.Marker([36.82352451367367, 10.314742119738725], popup='Globalnet Habib Bourguiba').add_to(m)
        m.fit_bounds([[36.82352451367367, 10.314742119738725]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet Avenue Hédi Nouira':
        folium.Marker([36.85851629198035, 10.164454042677344], popup='Globalnet Avenue Hédi Nouira').add_to(m)
        m.fit_bounds([[36.85851629198035, 10.164454042677344]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet Ariana':
        folium.Marker([36.85802277955676, 10.194336973365857], popup='Globalnet Ariana').add_to(m)
        m.fit_bounds([[36.85802277955676, 10.194336973365857]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet Siège Social':
        folium.Marker([36.83620965871203, 10.210091050603783], popup='Globalnet Siège Social').add_to(m)
        m.fit_bounds([[36.83620965871203, 10.210091050603783]])  # Adjust zoom to fit this marker
    elif goto_service == '2N-TT / 2N-GlobalNet / 2N-Ooredoo / 2N-Hexabyte / 2N-AmazonTV':
        folium.Marker([36.83127248673149, 10.205097180288057], popup='2N-TT / 2N-GlobalNet / 2N-Ooredoo / 2N-Hexabyte / 2N-AmazonTV').add_to(m)
        m.fit_bounds([[36.83127248673149, 10.205097180288057]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet Lotissement Ennassim Montplaisir':
        folium.Marker([36.821439970231786, 10.193827342668579], popup='Globalnet Lotissement Ennassim Montplaisir ').add_to(m)
        m.fit_bounds([[36.821439970231786, 10.193827342668579]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet 112 Av. de La Liberté':
        folium.Marker([36.817230670108664, 10.181865505937651], popup='Globalnet 112 Av. de La Liberté').add_to(m)
        m.fit_bounds([[36.817230670108664, 10.181865505937651]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet Ibn Sina':
        folium.Marker([36.76081859878098, 10.213838869667331], popup='Globalnet Ibn Sina').add_to(m)
        m.fit_bounds([[36.76081859878098, 10.213838869667331]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet Boumhal Bassatine':
        folium.Marker([36.741646415747425, 10.307189738000133], popup='Globalnet Boumhal Bassatine').add_to(m)
        m.fit_bounds([[36.741646415747425, 10.307189738000133]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet El Mourouj ':
        folium.Marker([36.7202426422909, 10.232042457711284], popup='Globalnet El Mourouj ').add_to(m)
        m.fit_bounds([[36.7202426422909, 10.232042457711284]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet denden':
        folium.Marker([36.80623730155562, 10.114700958113426], popup='Globalnet denden').add_to(m)
        m.fit_bounds([[36.80623730155562, 10.114700958113426]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet béni Khalled':
        folium.Marker([36.69601938554935, 10.594399499846414], popup='Globalnet béni Khalled').add_to(m)
        m.fit_bounds([[36.69601938554935, 10.594399499846414]])  # Adjust zoom to fit this marker
    elif goto_service == 'Globalnet Zaghouan':
        folium.Marker([36.41803628922465, 10.199003247398595], popup='Globalnet Zaghouan').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    # Add other markers for different services...

    # Get HTML Representation of Map Object
    map_html = m._repr_html_()

    context = {
        'map_html': map_html,
    }
    return render(request, 'base.html', context) 

def service_and_map(request):
    # Create Map Object# Create Map Object
    m = folium.Map(location=[36.80969919046897, 10.178292643895002], zoom_start=11)

    # Add markers
    folium.Marker([36.88827509199517, 10.325250397827855], popup='GlobalNet Taieb Mhiri').add_to(m)
    folium.Marker([36.87056260487405, 10.247767629874073], popup='GlobalNet Elec plus ').add_to(m)
    folium.Marker([36.86041244142929, 10.275317068615673], popup='Globalnet El Wahat').add_to(m)
    folium.Marker([36.83261401968672, 10.325078922746998], popup='GlobalNet Sbi Kram').add_to(m)
    folium.Marker([36.82352451367367, 10.314742119738725], popup='Globalnet Habib Bourguiba').add_to(m)
    folium.Marker([36.85851629198035, 10.164454042677344], popup='Globalnet Avenue Hédi Nouira').add_to(m)
    folium.Marker([36.85802277955676, 10.194336973365857], popup='Globalnet Ariana').add_to(m)
    folium.Marker([36.83620965871203, 10.210091050603783], popup='Globalnet Siège Social').add_to(m)
    folium.Marker([36.83127248673149, 10.205097180288057], popup='2N-TT / 2N-GlobalNet / 2N-Ooredoo / 2N-Hexabyte / 2N-AmazonTV').add_to(m)
    folium.Marker([36.821439970231786, 10.193827342668579], popup='Globalnet Lotissement Ennassim Montplaisir ').add_to(m)
    folium.Marker([36.817230670108664, 10.181865505937651], popup='Globalnet 112 Av. de La Liberté').add_to(m)
    folium.Marker([36.76081859878098, 10.213838869667331], popup='Globalnet Ibn Sina').add_to(m)
    folium.Marker([36.741646415747425, 10.307189738000133], popup='Globalnet Boumhal Bassatine').add_to(m)
    folium.Marker([36.7202426422909, 10.232042457711284], popup='Globalnet El Mourouj ').add_to(m)
    folium.Marker([36.80623730155562, 10.114700958113426], popup='Globalnet denden').add_to(m)
    folium.Marker([36.69601938554935, 10.594399499846414], popup='Global net béni Khalled').add_to(m)
    folium.Marker([36.41803628922465, 10.199003247398595], popup='Global Zaghouan').add_to(m)
    # Get HTML Representation of Map Object
    map_html = m._repr_html_()

    # Get the list of services
    gouvernorat = request.GET.get('gouvernorat')
    localite = request.GET.get('ville')
    type_pdv = request.GET.get('pdv')

    services = Service.objects.all()

    if gouvernorat and gouvernorat != 'Gouvernorat':
        services = services.filter(gouvernorat=int(gouvernorat))

    if localite and localite != 'Localité':
        services = services.filter(localite=int(localite))

    if type_pdv and type_pdv != 'Type':
        services = services.filter(type=int(type_pdv))


    context = {
        'map_html': map_html,
        'services': services,
    }

    return render(request, 'base.html', context)

class ServiceListView(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    queryset = Service.objects.all()

class ServiceCreateView(CreateAPIView):
    serializer_class = ServiceSerializer

from django.shortcuts import render

def service_list(request):
    gouvernorat = request.GET.get('gouvernorat', 'Gouvernorat')
    localite = request.GET.get('localite', 'Localité')
    type_pdv = request.GET.get('pdv', 'Type')

    services = Service.objects.all()

    if gouvernorat != 'Gouvernorat':
        services = services.filter(gouvernorat=gouvernorat)

    if localite != 'Localité':
        services = services.filter(localite=localite)

    if type_pdv != 'Type':
        services = services.filter(type=type_pdv)

    context = {
        'services': services
    }

    return render(request, 'service_list.html', context)

from django.contrib.auth.decorators import user_passes_test

def is_admin_with_password(user):
    return user.is_authenticated and user.username == 'admin' and user.check_password('123')
from django.shortcuts import render
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(is_admin_with_password)
def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    return render(request, 'service_detail.html', {'service': service})

from django.views.decorators.csrf import csrf_exempt
@user_passes_test(is_admin_with_password)
@csrf_exempt
def service_add(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('data')
    else:
        form = ServiceForm()
    return render(request, 'service_add.html', {'form': form})
@user_passes_test(is_admin_with_password)
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('data')  # Redirection vers la page data.html après la modification
    else:
        form = ServiceForm(instance=service)
    return render(request, 'service_edit.html', {'form': form, 'service': service})
@user_passes_test(is_admin_with_password)
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    if request.method == 'POST':
        service.delete()
        return redirect('data')
    return render(request, 'service_delete.html', {'service': service})



from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout

def signup(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.user.is_authenticated:
        return redirect('base.html') # Redirect to the desired page after login
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('service_list') # Redirect to the desired page after login
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def signout(request):
    logout(request)
    return redirect('/')



from django.shortcuts import render, redirect
from .models import Client

from .my_captcha import FormWithCaptcha

def gestion_en_ligne(request):
    if request.method == 'POST':
        form = FormWithCaptcha(request.POST)
        if form.is_valid():
            produit_prix = {
                'Mensuel': 37.900,
                'Trimestriel': 113.700,
                'Semestriel': 227.400,
                'Annuel': 454.800,
            }
            paiement_option = request.POST.get('paiement')
            prix = produit_prix.get(paiement_option, 0)
            promo_checkbox_value = request.POST.get('promoCheckbox')  # Check if the promo checkbox is selected
            if promo_checkbox_value:
                prix += 1  # Add 1 to the total price if the promo checkbox is selected
            
            # Create an instance of the model Client with the form data
            client = Client(
                nom_client=request.POST.get('nomClient'),
                type_identifiant=request.POST.get('typeIdentifiant'),
                identifiant=request.POST.get('identifiant'),
                email_client=request.POST.get('emailClient'),
                gouvernorat=request.POST.get('gouvernorat'),
                adresse=request.POST.get('adresse'),
                code_postal=request.POST.get('codePostal'),
                gsm_client=request.POST.get('gsmClient'),
                deja_client=request.POST.get('dejaClient') == 'true',  # Convert the value to a boolean
                code_client_existant=request.POST.get('codeClientExistant'),
                cin_client_existant=request.POST.get('cinClientExistant'),
                nom_proprietaire_ligne=request.POST.get('nomProprietaireLigne'),
                numero_appel=request.POST.get('numeroAppel'),
                produit=request.POST.get('produit'),
                paiement=request.POST.get('paiement'),
                recuperer_modem=request.POST.get('recupererModem'),
                agence=request.POST.get('agence'),
                total_a_payer=prix,  # Assign the calculated total price to the total_a_payer field
            )
            
            client.save()
            
            # Redirect the user to another page or perform another action
            return redirect('success')

    else:
        # Display the form for step 4 with the captcha
        client_id = request.GET.get('client_id')
        if client_id:
            try:
                client = Client.objects.get(pk=client_id)
                form = FormWithCaptcha(instance=client)
            except Client.DoesNotExist:
                form = FormWithCaptcha()
        else:
            form = FormWithCaptcha()

    context = {
        'form': form,
        'selected_produit': request.POST.get('produit', '') if request.method == 'POST' else '',
    }
    return render(request, 'gestion_en_ligne.html', context)





from django.shortcuts import render, redirect
from .models import Client
@user_passes_test(is_admin_with_password)
def delete_client(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('result')


from django.shortcuts import render

def success(request):
    return render(request, 'success.html')


@user_passes_test(is_admin_with_password)
def simple(request):
    clients = Client.objects.all()

    context = {
        'clients': clients,
       
    }
    return render(request, 'simple.html', context)
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
@user_passes_test(is_admin_with_password)
def client_edit(request, id):
    client = get_object_or_404(Client, id=id)
    
    if request.method == 'POST':
        # Assuming you have a FormWithCaptcha for editing client details
        form = FormWithCaptcha(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('simple')  # Redirect to the appropriate view after successful edit
    
    else:
        # Assuming you have a FormWithCaptcha for editing client details
        form = FormWithCaptcha(instance=client)
    
    context = {
        'form': form,
    }
    return render(request, 'client_edit.html', context)

from django.shortcuts import render, get_object_or_404, redirect
from .models import Client
@user_passes_test(is_admin_with_password)
def client_delete(request, pk):
    client = get_object_or_404(Client, pk=pk)
    
    if request.method == 'POST':
        if request.POST.get('confirm_delete') == 'True':
            client.delete()
            return redirect('simple')  # Redirect to the appropriate view after successful delete
    
    context = {
        'client': client,
    }
    
    if 'confirm_delete' in request.POST:
        # Render the simple.html template with the Modal shown
        return render(request, 'simple.html', context)
    
    return render(request, 'client_delete.html', context)

from django.http import HttpResponseRedirect
@user_passes_test(is_admin_with_password)
def data(request):
    gouvernorat = request.GET.get('gouvernorat', 'Gouvernorat')
    localite = request.GET.get('localite', 'Localité')
    type_pdv = request.GET.get('pdv', 'Type')

    gouvernorat = request.GET.get('gouvernorat')
    localite = request.GET.get('ville')
    type_pdv = request.GET.get('pdv')

    services = Service.objects.all()

    if gouvernorat and gouvernorat != 'Gouvernorat':
        services = services.filter(gouvernorat=int(gouvernorat))

    if localite and localite != 'Localité':
        services = services.filter(localite=int(localite))

    if type_pdv and type_pdv != 'Type':
        services = services.filter(type=int(type_pdv))

    context = {
        'services': services
    }
    return render(request, 'data.html',context)

# views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Service
@user_passes_test(is_admin_with_password)
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)

    if request.method == 'POST':
        if request.POST.get('confirm_delete') == 'True':
            service.delete()
            return redirect('data')  # Redirect to the appropriate view after successful delete

    context = {
        'service': service,
    }

    if 'confirm_delete' in request.POST:
        # Render the service_delete.html template with the Modal shown
        return render(request, 'data.html', context)

    return render(request, 'service_delete.html', context)

# views.py


from django.shortcuts import render

def handle404(request, exception):
    return render(request, '404.html')



from django.shortcuts import render
from django.http import JsonResponse

def upload_files(request):
    if request.method == 'POST':
        # Handle the file upload here and save the files
        uploaded_files = request.FILES.getlist('file')
        for uploaded_file in uploaded_files:
            # Save the file or perform any other operation you need
            pass
        return JsonResponse({'message': 'Files uploaded successfully.'})
    return render(request, 'upload.html')

def drag(request):
    return render(request,'drag.html')
