from django import forms

class FormularioContacto(forms.Form):
    Nombre=forms.CharField(label='Nombre', required=True)
    Email=forms.EmailField(label='Email', required=True)
    Asunto=forms.CharField(label='Asunto', required=True)
    Mensaje=forms.CharField(label='Mensaje', widget=forms.Textarea)
    
    
    