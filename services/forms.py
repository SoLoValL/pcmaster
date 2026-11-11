from django import forms
from .models import Service, Skill


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ['title', 'description', 'device_type', 'price', 'duration_hours', 'is_published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название услуги'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Описание'}),
            'device_type': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'duration_hours': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.5'}),
            'is_published': forms.CheckboxInput(),
        }
