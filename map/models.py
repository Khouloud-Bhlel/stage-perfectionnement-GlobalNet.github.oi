from django.db import models
from django.contrib.postgres.fields import JSONField
from django.views.decorators.csrf import csrf_exempt

class Service(models.Model):
    gouvernorat_choices = [
        ('Gouvernorat', 'Gouvernorat'),
        ('ARIANA', 'ARIANA'),
        ('BEJA', 'BEJA'),
        ('BEN AROUS', 'BEN AROUS'),
        ('BIZERTE', 'BIZERTE'),
        ('GABES', 'GABES'),
        ('GAFSA', 'GAFSA'),
        ('JENDOUBA', 'JENDOUBA'),
        ('KAIROUAN', 'KAIROUAN'),
        ('KASSERINE', 'KASSERINE'),
        ('KEBILI', 'KEBILI'),
        ('KEF', 'KEF'),
        ('MAHDIA', 'MAHDIA'),
        ('MANOUBA', 'MANOUBA'),
        ('MEDENINE', 'MEDENINE'),
        ('MONASTIR', 'MONASTIR'),
        ('NABEUL', 'NABEUL'),
        ('SFAX', 'SFAX'),
        ('SIDI BOUZID', 'SIDI BOUZID'),
        ('SILIANA', 'SILIANA'),
        ('SOUSSE', 'SOUSSE'),
        ('TATAOUINE', 'TATAOUINE'),
        ('TOZEUR', 'TOZEUR'),
        ('TUNIS', 'TUNIS'),
        ('ZAGHOUAN', 'ZAGHOUAN'),
    ]

    localite_choices = [
        ('Localité', 'Localité'),
        ('ARIANA', 'ARIANA'),
        ('BORJ LOUZIR', 'BORJ LOUZIR'),
        ('CITE ETTADAMAN', 'CITE ETTADAMAN'),
        ('EL MENZAH 6', 'EL MENZAH 6'),
        ('ENNASR', 'ENNASR'),
        ('NKHILET', 'NKHILET'),
    ]

    type_choices = [
        ('Type', 'Type'),
        ('Agence', 'Agence'),
        ('Revendeur', 'Revendeur'),
    ]

    titre = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    telephone = models.CharField(max_length=20)
    hours = models.CharField(max_length=100, verbose_name='Horaire')
    gouvernorat = models.CharField(max_length=100, choices=gouvernorat_choices, default='Gouvernorat')
    localite = models.CharField(max_length=100, choices=localite_choices, default='Localité')
    type = models.CharField(max_length=100, choices=type_choices, default='Type')
    popup_name = models.CharField(max_length=100)

    def __str__(self):
        return self.titre
from django.db import models

class Client(models.Model):
    GOUVERNORAT_CHOICES = [
        ('Gouvernorat', 'Gouvernorat'),
        ('ARIANA', 'ARIANA'),
        ('BEJA', 'BEJA'),
        ('BEN AROUS', 'BEN AROUS'),
        ('BIZERTE', 'BIZERTE'),
        ('GABES', 'GABES'),
        ('GAFSA', 'GAFSA'),
        ('JENDOUBA', 'JENDOUBA'),
        ('KAIROUAN', 'KAIROUAN'),
        ('KASSERINE', 'KASSERINE'),
        ('KEBILI', 'KEBILI'),
        ('KEF', 'KEF'),
        ('MAHDIA', 'MAHDIA'),
        ('MANOUBA', 'MANOUBA'),
        ('MEDENINE', 'MEDENINE'),
        ('MONASTIR', 'MONASTIR'),
        ('NABEUL', 'NABEUL'),
        ('SFAX', 'SFAX'),
        ('SIDI BOUZID', 'SIDI BOUZID'),
        ('SILIANA', 'SILIANA'),
        ('SOUSSE', 'SOUSSE'),
        ('TATAOUINE', 'TATAOUINE'),
        ('TOZEUR', 'TOZEUR'),
        ('TUNIS', 'TUNIS'),
        ('ZAGHOUAN', 'ZAGHOUAN'),
    ]
    DEJA_CLIENT_CHOICES = [
        (True, 'Oui'),
        (False, 'Non'),
    ]
    TYPE_IDENTIFIANT=[
        ('CIN', 'CIN'),
        ('Carte Sejour', 'Carte Sejour'),
        ('Passeport', 'Passeport'),
    ]
    PRODUIT_CHOICES = [
        ('UNO VDSL 20M', 'UNO VDSL 20M'),
        ('UNO VDSL 30M', 'UNO VDSL 30M'),
        ('UNO VDSL 50M', 'UNO VDSL 50M'),
        ('UNO VDSL 100M', 'UNO VDSL 100M'),
    ]
    PAIEMENT_CHOICES = [
        ('Mensuel', 'Mensuel'),
        ('Trimestriel', 'Trimestriel'),
        ('Semestriel', 'Semestriel'),
        ('Annuel', 'Annuel'),
    ]
    AGENCE_CHOICES = [
        ('Agence Ariana', 'Agence Ariana'),
        ('Agence Av. de la République', 'Agence Av. de la République'),
        ('Agence El Menzah', 'Agence El Menzah'),
        ('Agence Ennasr', 'Agence Ennasr'),
        ('Agence Kheireddine Pacha', 'Agence Kheireddine Pacha'),
        ('Agence Lac 1', 'Agence Lac 1'),
        ('Agence Lac 2', 'Agence Lac 2'),
        ('Agence Nabeul', 'Agence Nabeul'),
        ('Agence Sousse', 'Agence Sousse'),
        ('Agence Tunis Belvédère', 'Agence Tunis Belvédère'),
        ('Agence Tunis Centre Ville', 'Agence Tunis Centre Ville'),
        ('Agence Tunis El Menzah 9', 'Agence Tunis El Menzah 9'),
        ('Agence Tunis Lafayette', 'Agence Tunis Lafayette'),
        ('Agence Tunis Lac', 'Agence Tunis Lac'),
        ('Agence Tunis Le Kram', 'Agence Tunis Le Kram'),
        ('Agence Tunis Les Berges du Lac', 'Agence Tunis Les Berges du Lac'),
        ('Agence Tunis Médina', 'Agence Tunis Médina'),
        ('Agence Tunis Montplaisir', 'Agence Tunis Montplaisir'),
        ('Agence Tunis Mutuelle Ville', 'Agence Tunis Mutuelle Ville'),
        ('Agence Tunis Route de la Marsa', 'Agence Tunis Route de la Marsa'),
        ('Agence Tunis Zone Industrielle', 'Agence Tunis Zone Industrielle'),
    ]

    nom_client = models.CharField(max_length=100)
    type_identifiant = models.CharField(max_length=100, choices=TYPE_IDENTIFIANT, default='typeIdentifiant')
    identifiant = models.CharField(max_length=100)
    email_client = models.EmailField()
    gouvernorat = models.CharField(max_length=100, choices=GOUVERNORAT_CHOICES, default='Gouvernorat')
    adresse = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    gsm_client = models.CharField(max_length=20)
    deja_client = models.BooleanField(default=False)  # Add a field to indicate if the user is an existing client
    code_client_existant = models.CharField(max_length=100, blank=True, null=True)  # Add code_client_existant field
    cin_client_existant = models.CharField(max_length=100, blank=True, null=True)  # Add cin_client_existant field
    
    nom_proprietaire_ligne = models.CharField(max_length=100)
    numero_appel = models.CharField(max_length=100)
    produit = models.CharField(max_length=100, choices=PRODUIT_CHOICES, null=True)
    paiement = models.CharField(max_length=100, choices=PAIEMENT_CHOICES, null=True)

    recuperer_modem = models.CharField(max_length=100)
    agence = models.CharField(max_length=100, choices=AGENCE_CHOICES, null=True)
    total_a_payer = models.FloatField(null=True, blank=True)


# models.py

from django.shortcuts import render
import folium
@csrf_exempt
def display_map(request):
    # You can get the 'goto' parameter from the URL using request.GET.get('goto')
    service_name = request.GET.get('goto')
    
    # Create Map Object
    m = folium.Map(location=[36.80969919046897, 10.178292643895002], zoom_start=11)

    # Add marker for the selected service_name
    if service_name == 'GlobalNet Taieb Mhiri':
        folium.Marker([36.88827509199517, 10.325250397827855], popup='GlobalNet Taieb Mhiri').add_to(m)
        m.fit_bounds([[36.88827509199517, 10.325250397827855]])  # Adjust zoom to fit this marker

    elif service_name == 'GlobalNet Elec plus':
        folium.Marker([36.87056260487405, 10.247767629874073], popup='GlobalNet Elec plus ').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet El Wahat':
        folium.Marker([36.86041244142929, 10.275317068615673], popup='Globalnet El Wahat').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'GlobalNet Sbi Kram ':
        folium.Marker([36.83261401968672, 10.325078922746998], popup='GlobalNet Sbi Kram').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet Habib Bourguiba':
        folium.Marker([36.82352451367367, 10.314742119738725], popup='Globalnet Habib Bourguiba').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet Avenue Hédi Nouira':
        folium.Marker([36.85851629198035, 10.164454042677344], popup='Globalnet Avenue Hédi Nouira').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet Ariana':
        folium.Marker([36.85802277955676, 10.194336973365857], popup='Globalnet Ariana').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet Siège Social':
        folium.Marker([36.83620965871203, 10.210091050603783], popup='Globalnet Siège Social').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == '2N-TT / 2N-GlobalNet / 2N-Ooredoo / 2N-Hexabyte / 2N-AmazonTV':
        folium.Marker([36.83127248673149, 10.205097180288057], popup='2N-TT / 2N-GlobalNet / 2N-Ooredoo / 2N-Hexabyte / 2N-AmazonTV').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet Lotissement Ennassim Montplaisir':
        folium.Marker([36.821439970231786, 10.193827342668579], popup='Globalnet Lotissement Ennassim Montplaisir ').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet 112 Av. de La Liberté':
        folium.Marker([36.817230670108664, 10.181865505937651], popup='Globalnet 112 Av. de La Liberté').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet Ibn Sina':
        folium.Marker([36.76081859878098, 10.213838869667331], popup='Globalnet Ibn Sina').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet Boumhal Bassatine':
        folium.Marker([36.741646415747425, 10.307189738000133], popup='Globalnet Boumhal Bassatine').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet El Mourouj ':
        folium.Marker([36.7202426422909, 10.232042457711284], popup='Globalnet El Mourouj ').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet denden':
        folium.Marker([36.80623730155562, 10.114700958113426], popup='Globalnet denden').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet béni Khalled':
        folium.Marker([36.69601938554935, 10.594399499846414], popup='Global net béni Khalled').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker
    elif service_name == 'Globalnet Zaghouan':
        folium.Marker([36.41803628922465, 10.199003247398595], popup='Global Zaghouan').add_to(m)
        m.fit_bounds([[36.41803628922465, 10.199003247398595]])  # Adjust zoom to fit this marker

    # Add other markers if needed for other service names

    # Get HTML Representation of Map Object
    map_html = m._repr_html_()
    
    context = {
        'map_html': map_html,
    }
    return render(request, 'base.html', context)
