from django import forms
from .models import User

class EntryForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'title', 'hometown']
        widgets = {'age': forms.NumberInput(attrs={'min': 0})}
