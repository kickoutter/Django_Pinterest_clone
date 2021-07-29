from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world') # 완료되면 오는 url
    template_name = 'profileapp/create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    # accountapp의 url페이지를 보면 url패턴에 pk가 있습니다. 이는 즉, 정적으로 넘어가게 되면 해당 페이지의 pk없이 가는 것이므로 문제가 되겠조?!
    # 동적으로 페이지를 넘기는 것이 바로 get_success_url 메소드
    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'

    def get_success_url(self):
        return reverse('accountapp:detail', kwargs={'pk': self.object.pk})