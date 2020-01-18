from django import forms
from .models import ankidb

class StoreMemories(forms.ModelForm):
    class Meta:
        model = ankidb
        fields = ['database_loci',
    'domain_theme',
    'primary_key',
    'first_point_to_remember',
    'second_point_to_remember',
    'third_point_to_remember',
    'fourth_point_to_remember',
    'fiveth_point_to_remember',
    'sixth_point_to_remember',
    'seventh_point_to_remember',
    'eighth_point_to_remember']
