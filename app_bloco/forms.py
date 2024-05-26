from django import forms
from .models import BlocoNota, Tema

class Criar_bloco(forms.ModelForm):
    class Meta:
        model = BlocoNota
        fields = ('titulo', 'assunto', 'tema', 'conclusao')


class Criar_Tema(forms.ModelForm):
    class Meta:
        model = Tema
        fields = ('tema',)
        
        
