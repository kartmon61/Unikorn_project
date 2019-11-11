from django.shortcuts import render

# Create your views here.

#로그인 페이지 보여주는 함수
def login(request):
    return render(request,'login.html')

def create(request):
    return render(request,'create.html')