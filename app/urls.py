from django.urls import path

from .views import homepage

app_name = 'app'

urlpatterns = [
  path('', homepage, name='homepage'),
  path('<str:name>/', homepage, name='homepage')
]
