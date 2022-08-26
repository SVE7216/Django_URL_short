from django.urls import path

from . import views


urlpatterns = [
    path('', views.shortener_view, name='shortener'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('links/', views.links_list_view, name='links'),
    path('<str:pk>/', views.redirect_to_origin_url_view, name='redirect-to-origin'),
]
