from django.urls import path
from .import views


urlpatterns = [
    # /lecture url에 강의평가 페이지가 보이도록 설정
    path('lecture/',views.lectureEval,name='lecture'),
]