from django.shortcuts import render
from .models import enroll,course_details
from App1.models import course
from django.contrib.auth.decorators import login_required


@login_required()
def l_details(request):
    enrolled_student = request.user
    enrol = enroll.objects.filter(enrolled_student=enrolled_student)
    return render(request,"profile.html",{"enrol":enrol})

@login_required()
def lecture(request,slug):
    obj=course_details.objects.get(course_id=slug)
    obj.save()
    return render(request,"details.html",{"obj":obj})