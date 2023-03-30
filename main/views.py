from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("안녕하세요. 리터러시팩토리 웹사이트를 준비하고 있습니다!")
