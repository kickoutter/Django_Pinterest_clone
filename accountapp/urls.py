# 하위 분기문 작성
# views.py에서 만든 helloworld를 보여주는 거
from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),

    # 가운데가 함수 들어와야할 자린데 class가 들어가서 class의 함수를 뱉어주는 .as_view() 사용
    path('create/', AccountCreateView.as_view(), name='create'),
]
