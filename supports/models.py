from tkinter import CASCADE
from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Faq(models.Model):
    image = models.ImageField(verbose_name='내용', null = True, blank=True)
    content = models.TextField(verbose_name='질문')
    created_at = models.DateTimeField(verbose_name='생성일시', auto_now_add=True)
    view_count = models.IntegerField(verbose_name='조회수',default=0)
    creator = models.ForeignKey(to = User, on_delete=models.CASCADE, null=True, blank=True)




#카테고리 사용법을 도저히 모르겠습니다. ㅠ