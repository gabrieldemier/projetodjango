from django.urls import path
from . import views

app_name = 'alunos'

urlpatterns = [
    path('', views.lista_alunos, name='lista_alunos'),
    path('novo/', views.criar_aluno, name='criar_aluno'),
    path('<int:pk>/', views.detalhe_aluno, name='aluno_detalhe'),
    path('<int:pk>/editar/', views.editar_aluno, name='aluno_form'),  # Update
    path('<int:pk>/excluir/', views.excluir_aluno, name='excluir_aluno'),  # Delete
]
