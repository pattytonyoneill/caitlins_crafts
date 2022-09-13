from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
        Form to allow users to sign-up for contact
    """
    class Meta:
        model = Contact
        fields = "__all__"
