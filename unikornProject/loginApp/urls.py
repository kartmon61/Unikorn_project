from django.urls import path
from .import views


urlpatterns = [
    #첫화면 login 페이지가 보이도록 설정
    path('',views.login,name='login'),
    path('create',views.create,name='create'),
]