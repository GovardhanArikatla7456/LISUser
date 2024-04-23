from django import forms
from .models import User
# form that takes the properties from model "user"
class EntryForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['name', 'age', 'title', 'hometown']
        widgets = {'age': forms.NumberInput(attrs={'min': 0})}
