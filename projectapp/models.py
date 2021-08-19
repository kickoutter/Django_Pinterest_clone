from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    # 문자열을 되돌려줘야 할때 어떤 문자열을 되돌려주는지??
    def __str__(self):
        return self.name