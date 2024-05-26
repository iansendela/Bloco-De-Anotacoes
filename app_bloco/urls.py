from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('criar_bloco/', views.criar_bloco, name='novo_bloco'),
    path('criar_tema/', views.criar_tema, name='novo_tema'),
    path('detalhes/<int:bloco_id>/', views.ler_bloco, name='detalhes'),
    path('update_bloco/<int:bloco_id>/', views.editar_bloco, name='update_bloco'),
    path('update_tema/<int:tema_id>/', views.editar_tema, name='update_tema'),
    path('deletar_bloco/<int:bloco_id>/', views.deletar_bloco, name='deletar_bloco'),
    path('deletar_tema/<int:tema_id>/', views.deletar_tema, name='deletar_tema'),
    path('temas/', views.temas, name='temas'),
    path('blocos/', views.BlocosListView.as_view(), name='blocos'),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    
    
]