from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=20, verbose_name='일기 제목', help_text='일기 제목')
    created_at = models.DateTimeField(null=True, blank=True, auto_now_add=True, verbose_name='작성일', help_text='작성일')
    image = models.ImageField(null=True, blank=True, upload_to='images', verbose_name='일기 이미지', help_text='일기 이미지')
    content = models.TextField(verbose_name='일기 내용', help_text='일기 내용')


# 일기
# - 제목
# - 내용
# - 작성한 날짜
# - 이미지
