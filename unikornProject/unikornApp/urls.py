from django.urls import path
from .import views


urlpatterns = [
    #메인 페이지
    path('main/',views.main,name='main'),
]