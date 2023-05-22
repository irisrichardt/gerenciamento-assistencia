from django.urls import path
from .views import tecnico_views

urlpatterns = [
    path('cadastrar_tecnico', tecnico_views.cadastrar_tecnico, name='cadastrar_tecnico'),
    path('listar_tecnicos', tecnico_views.listar_tecnicos, name='listar_tecnicos'),
]
