from django.urls import path
from . import views


app_name = 'shortner'

urlpatterns = [
    path('', views.home, name='home'),

    path('signup/', views.signup_user, name='signup'),
    path('login/', views.login_user, name='login'),

    path('create/', views.create, name='create'),
    path('go/<str:url>', views.go, name='go'),
    path('list/', views.list, name='list'),
]