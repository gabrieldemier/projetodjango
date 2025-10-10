from django.urls import path
from . import views  # ← importa diretamente da pasta da app

urlpatterns = [
    path('', views.lista_produtos, name='lista_produtos'),
]
