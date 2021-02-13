from django.urls import path

from snippets import views
from snippets.views import IndexView, LoginSnippetsView, LogoutSnippetsView, SnippetCreateView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginSnippetsView.as_view(), name='login'),
    path('logout/', LogoutSnippetsView.as_view(), name='logout'),
    path('snippets/python/', views.language, name='language'),
    path('snippets/user/juancito/', views.user_snippets, name='user_snippets'),
    path('snippets/snippet/', views.snippet, name='snippet'),
    path('snippets/add/', SnippetCreateView.as_view(), name='snippet_add'),
    path('snippets/edit/', views.snippet_edit, name='snippet_edit'),
    path('snippets/delete/', views.snippet_delete, name='snippet_delete'),
]