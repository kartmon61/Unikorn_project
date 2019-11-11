from django.urls import path
from .import views


urlpatterns = [
    #첫화면 login 페이지가 보이도록 설정
    path('',views.login,name='login'),
    #회원가입 페이지
    path('signup/',views.signup,name='signup'),
    #로그아웃
    path('logout/',views.logout, name='logout'),
]