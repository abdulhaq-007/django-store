from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
        'messages':forms.Textarea(attrs={'rows':9, 'cols':30, 'placeholder': 'Enter Message', 'class': 'form-control w-100'}),
        'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
        'email': forms.TextInput(attrs={'placeholder': 'Enter your email', 'class': 'form-control'})
        }