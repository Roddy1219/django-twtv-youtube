from django.shortcuts import render
from django.views.generic.base import View
import datetime


# Create your views here.

class IndexView(View):
    def get(self, request, tvno='0'):
        tv_list = [
            {'name': '中视新闻', 'tvcode': '3e1q8LorZ2U'},
            {'name': '民视新闻', 'tvcode': 'XxJKnDLYZz4'},
            {'name': '三立新闻', 'tvcode': '15IKxpj1gQA'},
        ]

        now = datetime.datetime.now()
        tvno = tvno
        tv = tv_list[int(tvno)]
        tv_number = int(tvno)
        return render(request, 'index.html', locals())
