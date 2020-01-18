from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('Objective1/', views.Objective1, name='Objective1'),
    path('Objective2/', views.Objective2, name='Objective2'),
    path('Objective3/', views.Objective3, name='Objective3'),
    path('Objective4/', views.Objective4, name='Objective4'),
    path('Objective5/', views.Objective5, name='Objective5'),
    path('DBFO/', views.DBFO, name='DBFO'),
]
