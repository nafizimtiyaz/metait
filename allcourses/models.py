from django.db import models
from ckeditor.fields import RichTextField
from App1.models import User,course
from django.db.models.signals import pre_save
from django.dispatch import receiver
from App1.slug_url import unique_slug_generator

class course_details(models.Model):
    course=models.ForeignKey(course,on_delete=models.CASCADE)
    title=models.CharField(max_length=100,null=True)
    slug = models.SlugField(max_length=250, null=True, unique=False, blank=True)
    lecture_body= RichTextField(blank= True)
    lecture_imgae=models.ImageField(upload_to="all_courses")
    lecture_title1 = models.CharField(max_length=100, null=True, blank=True)
    lecture_body1 = models.TextField(max_length=10000, null=True, blank=True)
    lecture_imgae1 = models.ImageField(upload_to="all_courses", null=True, blank=True)
    video_link = models.CharField(max_length=1000, null=True, blank=True)
    link_height= models.IntegerField(blank=True)
    video =models.FileField(upload_to="video",blank=True)
    video_height = models.CharField(max_length=100, blank=True)


    def __str__(self):
        return f'{self.course} | {self.title}'

@receiver(pre_save, sender=course_details)
def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


class enroll(models.Model):
    enrolled_course = models.ForeignKey(course, on_delete=models.CASCADE)
    enrolled_student = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.enrolled_student} | {self.enrolled_course}'
