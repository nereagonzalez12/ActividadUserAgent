from django import forms

class CreaTableroForm(forms.Form):
    filas = forms.IntegerField(label='Filas',min_value=1, max_value=20, required= True, initial=2)
    columnas = forms.IntegerField(label='Columnas', min_value=1, max_value=15, required=True, initial=2)
