from django import template
from frontend.models.category import Category

register = template.Library()


@register.filter
def get_all_category(value):
    return Category.objects.all()
