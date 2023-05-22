from django.urls import path
from .views import tecnico_views

urlpatterns = [
    path('cadastrar_tecnico', tecnico_views.cadastrar_tecnico, name='cadastrar_tecnico'),
    path('listar_tecnicos', tecnico_views.listar_tecnicos, name='listar_tecnicos'),
    path('listar_tecnico/<int:id>', tecnico_views.listar_tecnico_id, name='listar_tecnico_id'),
    path('editar_tecnico/<int:id>', tecnico_views.editar_tecnico, name='editar_tecnico'),

]
