from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld


def hello_world(request):

    if request.user.is_authenticated:

        if request.method == "POST":

            temp = request.POST.get('input')

            new_data = HelloWorld()
            new_data.text = temp
            new_data.save()

            return HttpResponseRedirect(reverse('accountapp:hello_world'))

        else:
            data_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html', context={'data_list': data_list})

    else:
        return HttpResponseRedirect(reverse('accountapp:login'))


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # 성공하면 hello_world로 가라!, # 만들고 추가하는거라 success~ 해줬음
    template_name = 'accountapp/create.html'

# DetailView
class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user' # 컨텍스트에서 볼 객체의 이름 설정?
    template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
    model = User # 기존 AccountCreateView와 동일한 모델 값을 사용해요.
    form_class = AccountCreationForm # form을 만들어 값을 전달하게 되요. (ID변경 막으려고, 커스터마이징한 Form을 새로 만들어 전달받아 사용.)
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world') # 성공적으로 프로필이 완성되면 메인화면으로 넘겨줍니다.
    template_name = 'accountapp/update.html' # template경로 값을 지정해줘요.

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))



class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().post(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('accountapp:login'))