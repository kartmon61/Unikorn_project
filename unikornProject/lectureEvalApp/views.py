from django.shortcuts import render

# Create your views here.
#강의평가 페이지 보여주는 함수
def lectureEval(request):
    return render(request,'lectureEval.html')