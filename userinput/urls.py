from django.urls import path
from . import views
# urls for required routes
urlpatterns = [
    path('', views.form_view, name='form'),
    path('input/', views.confirmation_view, name='confirmation'),
 ]
 