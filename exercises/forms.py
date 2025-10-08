from django import forms
from .models import Exercise


class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['type', 'description', 'time', 'notes']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2}),
            'notes': forms.Textarea(attrs={'rows': 3})
        }