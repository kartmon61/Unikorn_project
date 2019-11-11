from django.shortcuts import render


# Create your views here.
#메인 페이지 보여주는 함수
def main(request):
    return render(request,'main.html')