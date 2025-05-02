from django.urls import path
from . import views

app_name = "decoder"

urlpatterns = [
    path('', views.index, name='index'),
    path('aim/', views.aim, name='aim'),
    path('theory/', views.theory, name='theory'),
    path('procedure/', views.procedure, name='procedure'),
    path('pretest/', views.pretest, name='pretest'),
    path('simulation/', views.simulation, name='simulation'),
    path('posttest/', views.posttest, name='posttest'),
    path('references/', views.references, name='references'),
   
   
]
