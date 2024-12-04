from django.db import models
from django.conf import settings
from django.utils import timezone

"""
Django 模型
Django 里的模型是一种特殊的对象 — — 它保存在 数据库 中。 数据库是数据的集合。 
这是您存储有关用户、 您的博客文章等信息的地方。
"""

# 一篇博客文章模型
class Post(models.Model):
    """博客文章的属性：作者，标题，内容，发布日期等等"""
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()


    def __str__(self):
        return self.title



