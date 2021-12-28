from django.urls import path

from mainapp import views as mainapp_views

app_name = 'mainapp'

urlpatterns = [
    path('', mainapp_views.products, name = 'index'),
    path('<int:pk>/', mainapp_views.products, name='category'),
]


