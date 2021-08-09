from django.shortcuts import render

# Create your views here.
from django.urls import reverse
from django.views.generic import CreateView

from commentapp.forms import CommentCreationForm
from commentapp.models import Comment


class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentCreationForm
    template_name = 'commentapp/create.html'

    def form_valid(self, form):
        form.instance.writer = self.request.user
        form.instance.article_id = self.request.POST.get('article_pk')
        return super().form_valid(form)

    # CreateView나 UpdateView, DeleteView를 사용하면 특정 기능을 한 뒤 어떤 페이지로 이동할 것인지 정해주는 success_url 속성이 있다.
    # 이때 url parameter를 사용한 특정 페이지로 이동할때는 get_success_url 메소드를 사용
    # 출처: https://jamanbbo.tistory.com/20 [자기계발하는 쏭이]
    def get_success_url(self):
        return reverse('articleapp:detail', kwargs={'pk': self.object.article.pk})