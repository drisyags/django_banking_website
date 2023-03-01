from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='home'),
    path('register',views.register,name='register'),
    path('signin',views.signin,name='signin'),
    path('form',views.form,name='form'),
    path('signout',views.signout,name='signout'),
    path('indcon',views.indcon,name='indcon')
    
]
