from django import forms
from .models import Ticket


class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['device_type', 'problem', 'preferred_at', 'address']
        widgets = {
            'device_type': forms.Select(attrs={'class': 'form-control'}),
            'problem': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Опишите проблему...'}),
            'preferred_at': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Адрес для выезда'}),
        }
