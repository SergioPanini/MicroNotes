from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page),
    path('register/', views.register_user),
    path('signin/', views.signin),
    path('signout/', views.signout),
    path('test/', views.test),
    path('notes/', views.show_notes),
    path('createnote/', views.create_note),
]