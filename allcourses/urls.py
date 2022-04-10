from django.contrib.auth import views as auth_views
from django.conf import settings
from django.contrib import admin
from django.urls import path
from allcourses import views
from django.conf.urls.static import static
urlpatterns = [
    path('done',views.l_details,name="l_de"),
    path('<slug:slug>',views.lecture,name="de"),
]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)