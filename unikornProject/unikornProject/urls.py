"""unikornProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #로그인 앱 url 연결
    path('',include('loginApp.urls')),
    #메인 앱 url 연결
    path('',include('unikornApp.urls')),
    #강의평가 앱 url 연결
    path('',include('lectureEvalApp.urls')),
    #리스트 형식 게시판 앱 url 연결
    path('listBoard/',include('listBoardApp.urls')),
    #중고장터 게시판 앱 url 연결
    path('',include('usedMarketApp.urls')),
    #ckeditor 라이브러리 추가
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)