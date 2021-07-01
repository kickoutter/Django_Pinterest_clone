# 하위 분기문 작성
# views.py에서 만든 helloworld를 보여주는 거
from django.urls import path

from accountapp.views import hello_world

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]
