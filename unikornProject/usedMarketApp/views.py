from django.shortcuts import render

# Create your views here.
#중고장터 페이지 보여주는 함수
def usedMarket(request):
    return render(request,'usedMarket.html')