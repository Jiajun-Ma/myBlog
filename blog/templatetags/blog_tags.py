from django import template
from ..models import Post, Category, Tag

register = template.Library()


@register.simple_tag()
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag()
def archives():
    '''
    这里 dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，
    且是 Python 的 date 对象，精确到月份，降序排列。
    created_time : Post 的创建时间，
    month : 精度，
    order='DESC' : 表明降序排列（即离当前越近的时间越排在前面）。
    '''
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.simple_tag()
def get_tags():
    return Tag.objects.all()

