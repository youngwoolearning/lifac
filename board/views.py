from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("안녕하세요. 리터러시팩토리 웹사이트 게시판을 준비중입니다!")
