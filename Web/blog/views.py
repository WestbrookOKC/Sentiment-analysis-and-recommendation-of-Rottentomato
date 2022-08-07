import json

from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Movie

# 首页
def index(request):
    return render(request,"index.html")

# 电影信息
def movie(request):
    movie_list = Movie.objects.all()
    context = {'data': movie_list}
    print(movie_list)
    return render(request, "movielist.html", context)

def to_movie(request):
    if request.method == 'POST':
        user = request.POST.get('user')
        print(user)
        movie_list = Movie.objects.filter(user=user).all()
        print(movie_list)

        ken = []
        ken2 = []
        for movie in movie_list:
            # print(movie.recommend)
            # ken_str = json.dumps()
            # print(type(ken_str))
            # print(ken_str)
            ken_json = json.loads(movie.recommend)
            # print(type(ken_json))
            print(ken_json['Rear Window'])
            ken.append(ken_json)
            # con = {'Rear_window':movie.recommend[0]}
        # context = {'data': movie_list, 'ken': ken}
        # print(context['ken'])
        print(ken)
        for k in ken:
            ken2.append({'Rear_window':k['Rear Window'],'Alien':k['Alien'],'Coco':k['Coco']})
            # print(k['Rear Window'])
        print(ken2)
        context = {'data': movie_list, 'ken': ken2}
        return render(request,"movie.html",context)
