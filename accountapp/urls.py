# 하위 분기문 작성
# views.py에서 만든 helloworld를 보여주는 거
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = 'accountapp'

urlpatterns = [
    # path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),

    path('logout/', LogoutView.as_view(), name='logout'),

    # 가운데가 함수 들어와야할 자린데 class가 들어가서 class의 함수를 뱉어주는 .as_view() 사용 (Class Based View 사용 위해서 사용해야댐)
    path('create/', AccountCreateView.as_view(), name='create'),
    # DetailView여서 primary_key인 id인 주소를 넘겨주어야 거기로 라우팅을 연결할 수 있다. ex) accountapp/detail/1/
    path('detail/<int:pk>/', AccountDetailView.as_view(), name='detail'),

    path('update/<int:pk>/', AccountUpdateView.as_view(), name='update'),

    path('delete/<int:pk>/', AccountDeleteView.as_view(), name='delete'),

]
