from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

#로그인 페이지 함수
@csrf_exempt
def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request,username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return render(request,'main.html')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request,'login.html')

#회원가입 페이지 함수
@csrf_exempt
def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            user = User.objects.create_user(
                username=request.POST["username"],password=request.POST["password1"],email=request.POST["email"])
            auth.login(request,user)
            return render(request,'login.html')
        return render(request,'signup.html')

    return render(request,'signup.html')

#로그아웃 함수
@csrf_exempt
def logout(request):
    auth.logout(request)
    return render(request,'login.html')