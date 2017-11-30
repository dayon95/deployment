import json
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import FormView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from data01.models import pd1_time
from data01.models import pd2
from datetime import datetime, timedelta
class HomeView(TemplateView):
    template_name='data01/index.html'


class AjaxTemplateMixin(object):

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(self, 'ajax_template_name'):
            split = self.template_name.split('.html')
            split[-1] = '_inner'
            split.append('.html')
            self.ajax_template_name = ''.join(split)
        if request.is_ajax():
            self.template_name = self.ajax_template_name
        return super(AjaxTemplateMixin, self).dispatch(request, *args, **kwargs)
class TestFormView(SuccessMessageMixin, AjaxTemplateMixin, FormView):
    template_name = 'data01/index.html'
    success_url = reverse_lazy('index')
    success_message = "Way to go!"

# Create your views here.

def test(request):
    return render(request,'data01/test.html',{})

def test_pd1_time(request):
    time=pd1_time.objects.exclude(title__exact='')
    return render(request,'data01/test_pd1_time.html',{'time':time})

def test_pd2(request):
    time=pd1_time.objects.exclude(title__exact='')
    return render(request,'data01/test_pd2.html',{'two':two})

#아래에 있는 함수는 PosterData의 when을 datafield로 변경된 후에 실행가능함.
def index_tutorial(request):
    #today, tomorrow, this_week에는 오늘, 내일, 이번주의 주 번호가 들어감
    #주 번호는 52주 중 몇번째 주인지 나타내는 번호임
    #이 세개 변수는 python의 datetime 모듈을 사용했음.
    today=datetime.today()
    tomorrow=today+timedelta(days=1)
    this_week=today.isocalendar()[1] #week number
    date_KOR=["월", "화", "수", "목", "금", "토", "일"]
    date=date_KOR[today.weekday()]
    #today_list, tomorrow_list, this_week_list에는 각각 오늘 내일 이번주 강연 데이터가 들어있음
    #각각 조건에 맞는 filter를 이용하였음.
    today_list=pd1_time.objects.filter(date__year=today.year, date__month=today.month, date__day=today.day)
    tomorrow_list=pd1_time.objects.filter(date__year=tomorrow.year, date__month=tomorrow.month, date__day=tomorrow.day)
    this_week_list=pd1_time.objects.filter(date__week=this_week)
    #return render(request,'data01/index.html',today_list)
    contents={'date':date, 'today_list':today_list,'tomorrow_list':tomorrow_list,'this_week_list':this_week_list}
    return render(request,'data01/index_tutorial.html',contents)
'''
def about(request):
    return render(request,'about site')
'''
def index(request):
    today=datetime.today()
    tomorrow=today+timedelta(days=1)
    this_week=today.isocalendar()[1]
    date_KOR=["월","화","수","목","금","토","일"]
    date=date_KOR[today.weekday()]
    #start date와 end date 사이 값에 today, tomorrow, this_week중 하나라도 포함되면 list에 포함시켜야함
    #테스트용으로 startdate만으로 비교해볼것.
    today_list=pd2.objects.filter(startdate__year=today.year, startdate__month=today.month, startdate__day=today.day)
    tomorrow_list=pd2.objects.filter(startdate__year=tomorrow.year, startdate__month=tomorrow.month, startdate__day=tomorrow.day)
    this_week_list=pd2.objects.filter(startdate__week=this_week)
    contents={'date':date, 'today_list':today_list,'tomorrow_list':tomorrow_list,'this_week_list':this_week_list}
    return render(request,'data01/index.html',contents)

'''
def category(request, kind):
    return render(request,'카테고리에 따른 포스터')
'''

def about(request):
    return render(request,'data01/about.html')
