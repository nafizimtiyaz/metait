from django import template
import math

from App1.models import course,lecture
from allcourses.models import enroll

register = template.Library()
@register.simple_tag
def lcount():
    return lecture.objects.count()


@register.simple_tag
def is_enrolled(request,course):
    if not request.user.is_authenticated:
        return False
        # i you are enrooled in this course you can watch every video
    user = request.user
    try:
        user_course = enroll.objects.get(user=user, course=course)
        return True
    except:
        return False