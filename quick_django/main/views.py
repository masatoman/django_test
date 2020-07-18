from django.shortcuts import render
from django.http import HttpResponse

def temp(request):
    context = {
            'msg': 'hallow temp'
            }
    return render(request, 'main/temp.html', context)

# リクエスト情報を受け取る
def index(request):
    # レスポンスを生成する
    return HttpResponse('hollow world!')

# Create your views here.
