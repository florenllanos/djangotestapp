from django import forms
from gesevent.models import Tematica


class TematicaForm(forms.ModelForm):
    class Meta:
        model = Tematica
        fields = '__all__'
