from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User,auth
from  django.contrib import messages
from App1.models import user_profile,contactus,course,lecture
from .models import CART
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
@login_required()
def user_cart(request,slug):
    if request.method == 'POST':
        email=request.POST["email"]
        name=request.POST["name"]
        mycourse = request.POST["course"]
        TransectionID = request.POST["TransectionID"]
        Transection_Number = request.POST["Transection_Number"]

        carts = CART(user=request.user,email=email,name=name, mycourse=mycourse, TransectionID=TransectionID,
                     Transection_Number=Transection_Number)
        carts.save()
        email_subject = 'Course Payment Issue'
        message = "We Just Receive Your Requested Course Payment,We just Query and Contact you soon"
        from_email = settings.DEFAULT_FROM_EMAIL
        to_list = [carts.email]
        send_mail(email_subject, message, from_email, to_list, fail_silently=True)
        messages.info(request, 'Payment Request Successfull')
        return redirect('phome')
    else:
        mycart = course.objects.get(slug=slug)
        mycart.save()
        return render(request, "checkout.html", {"mycart": mycart})
