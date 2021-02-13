# Django
from django.shortcuts import render, redirect
from django.views.generic import View, ListView, CreateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

# Forms
from .forms import LoginForm, SnippetCreateForm


class LoginSnippetsView(View):
    """
        Class View para realizar el login del usuario
        en el sistema Snippets
    Args:
        View ([type]): [description]

    Returns:
        [type]: [description]
    """

    template_name ='login.html'

    def get(self, request, *args, **kwargs):
        form_class = LoginForm
        return render(request, 'login.html', {'form':form_class})

    def post(self, request, *args, **kwargs):
        msg = None

        email = request.POST['email']
        password = request.POST['password']
        usuario = User.objects.get(email=request.POST['email'])
        user = authenticate(username=usuario.username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            try:
                usuario = User.objects.get(email=request.POST['email'])
                if not usuario.check_password(password):
                    msg = "No has introducido correctamente la contraseña para el usuario."
            except User.DoesNotExist:
                msg = "No has introducido correctamente el nombre de usuario."

        return redirect('login')


class LogoutSnippetsView(View):
    """
        Realizamos el Logout del usuario.
        Una vez realizado el logout, volvemos a la
        pantalla de Login.
    Args:
        View ([Class View]): Vista genérica.
    """


    def get(self, request, *args, **kwargs):
        logout(request)
        form_class = LoginForm
        return redirect('login')


class IndexView(ListView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {})


def language(request):
    return render(request, 'index.html', {})


def user_snippets(request):
    return render(request, 'snippets/user_snippets.html', {})


def snippet(request):
    return render(request, 'snippets/snippet.html', {})


class SnippetCreateView(CreateView):
    template_name = 'snippets/snippet_add.html'

    def get(self, request, *args, **kwargs):
        form_class = SnippetCreateForm
        return render(request, 'snippets/snippet_add.html', {'form': form_class})

    def post(self, request, *args, **kwargs):
        form = BookCreateForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            return HttpResponseRedirect(reverse_lazy('books:detail', args=[book.id]))
        return render(request, 'books/book-create.html', {'form': form})


def snippet_edit(request):
    return render(request, 'snippets/snippet_add.html', {})


def snippet_delete(request):
    return render(request, 'snippets/user_snippets.html', {})
