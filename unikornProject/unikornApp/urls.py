from django.urls import path
from .import views


urlpatterns = [
    #첫화면 login 페이지가 보이도록 설정
    path('main/',views.main,name='main'),
]