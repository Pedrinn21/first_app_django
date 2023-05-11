from django.urls import path
from . import views

urlpatterns = [
   path('home/', views.home, name='home'),
   
   path('produto/', views.home_produto, name='home_produto'),
   path('insert_produto/', views.insertproduto, name='insert_produto'),
   path('editar/<int:id>/', views.editarproduto, name='editar'),
   path('apagar/<int:id>/', views.apagarproduto, name='apagar'),

   path('tipoproduto/', views.home_tipoproduto, name='home_tipoproduto'),
   path('insert_tipoproduto/', views.insert_tipoproduto, name='insert_tipoproduto'),
   
]