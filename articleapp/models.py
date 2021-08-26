from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    # writer == user
    # ForeginKey : user가 게시물을 하나만 쓰는게 아니라 1:N인 ForeignKey를 사용. (1:1이면 OneToOne)
    # on_delete=models.SET_NULL : user가 계정삭제해도 게시물은 사라지지않음. (반대로 CASCADE는 다 사라짐)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,
                                related_name='article', null=True, blank=True)

    title = models.CharField(max_length=200, null=True)

    # image는 media/profile/aritcle/ 경로에 업로드 한다.
    image = models.ImageField(upload_to='article/', null=False)
    content = models.TextField(null=True)

    # 자동으로 날짜 입력되게, 날짜정보
    created_at = models.DateField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)
