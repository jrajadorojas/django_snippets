from django import forms
from django.contrib.auth.models import User
from snippets.models import Snippet

# Models
from snippets.models import Language


TIPOS = (
    ('Publico', 'Público'),
    ('Privado', 'Privado'),
)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class SnippetCreateForm(forms.Form):
    Nombre = forms.CharField(widget=forms.TextInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': 'Nombre del Snippet',
                            'required':'required',
                            'id':'name',
                            'name':'name',
                            }
                    ))
    Descripcion = forms.CharField(widget=forms.TextInput(
                        attrs={
                            'class': 'form-control',
                            'placeholder': 'Descripcion',
                            'id':'description',
                            'name':'description',
                            }
                    ))
    Lenguaje = forms.ChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-control',
            'placeholder': 'Lenguajes',
            'id':'lenguajes',
            'name':'lenguajes',
            }
        ),
        choices=[(lan.name, lan.slug) for lan in Language.objects.all()])

    Tipo = forms.ChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-control',
            'placeholder': 'Tipo',
            'id':'tipo',
            'name':'tipo',
            }
        ),
        choices=TIPOS)


    snippet = forms.Textarea()

    class Meta:
        model = Snippet
        fields = ('name','description','snippet','lenguage','public')