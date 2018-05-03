from django import forms
from .models import Registrado

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre","email"]

    def clean_email(self):
        email= self.cleaned_data.get("email")
        if not "edu" in email:
            raise forms.ValidationError("Utiliza un correo determinado")
        return email

class ContactForm(forms.Form):
    nombre = forms.CharField()
    email= forms.EmailField()
    mensaje=forms.CharField(widget=forms.Textarea)
