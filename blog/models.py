from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    # 标题
    title = models.CharField(max_length=100)

    # 文章正文
    body = models.TextField()

    # 创建时间 修改时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 摘要 允许为空
    excerpt = models.CharField(max_length=200, blank=True)

    # 分类。与Category表关联. ForeignKey为一对多的关系
    category = models.ForeignKey(Category)

    # 标签。与Tag表关联。 ManyToManyField 为多对多关系。
    tags = models.ManyToManyField(Tag, blank=True)

    # 作者。与User关联。
    author = models.ForeignKey(User)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    class Meta:
        ordering = ['-created_time', 'title']


