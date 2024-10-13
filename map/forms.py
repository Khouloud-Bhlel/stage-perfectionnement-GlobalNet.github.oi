from django import forms
from .models import Service

# ServiceForm
class ServiceForm(forms.ModelForm):
    gouvernorat = forms.ChoiceField(
        choices=Service.gouvernorat_choices,
        widget=forms.Select(attrs={'class': 'custom-color'})
    )
    localite = forms.ChoiceField(
        choices=Service.localite_choices,
        widget=forms.Select(attrs={'class': 'custom-color'})
    )
    type = forms.ChoiceField(
        choices=Service.type_choices,
        widget=forms.Select(attrs={'class': 'custom-color'})
    )

    def clean_telephone(self):
        telephone = self.cleaned_data['telephone']
        if len(telephone) != 8 or not telephone.isdigit():
            raise forms.ValidationError('Le numéro de téléphone doit comporter 8 chiffres et ne doit contenir que des chiffres.')
        return telephone

    def clean(self):
        cleaned_data = super().clean()
        titre = cleaned_data.get('titre')
        address = cleaned_data.get('address')
        telephone = cleaned_data.get('telephone')
        hours = cleaned_data.get('hours')
        gouvernorat = cleaned_data.get('gouvernorat')
        localite = cleaned_data.get('localite')
        type = cleaned_data.get('type')
        popup_name=cleaned_data.get('popup_name')

        if not titre or not address or not telephone or not hours or not popup_name or  gouvernorat == '0' or localite == '0' or type == '0':
            #raise forms.ValidationError('Veuillez remplir tous les champs obligatoires.')
            return cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            field = self.fields[field_name]
            field.widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Service
        fields = ('titre', 'address', 'telephone', 'hours', 'gouvernorat', 'localite', 'type','popup_name')
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'custom-color'}),
            'address': forms.TextInput(attrs={'class': 'custom-color'}),
            'telephone': forms.TextInput(attrs={'class': 'custom-color'}),
            'hours': forms.TextInput(attrs={'class': 'custom-color'}),
            'popup_name': forms.TextInput(attrs={'class': 'custom-color'}),
        }

