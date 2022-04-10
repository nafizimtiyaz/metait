from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from App1 import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('home',views.phome,name="phome"),
    path('student/registration',views.registration,name="regi"),
    path('student/signup',views.singup,name="signup"),
    path('student/logout', views.logout, name="out"),
    path('account/email/change/password',views.changePass,name="changePass"),
    path('user/profile',views.student_profile,name="profile"),
    path('python-compiler',views.compiler,name="compiler"),
    path('activate/<uid>/<token>/', views.activate, name="activate"),
    path('profile/update',views.profile,name="m_profile"),
    path('contact-us',views.contact,name="contact"),
    path('course',views.all_courses,name="allcourse"),
    path('course/<slug:slug>',views.single,name="single"),
    path('all/',include("cart.urls")),
    path('quiz/<slug:slug>', views.quiz_quiz, name='quiz'),
    path('details',include("Leacture_Details.urls")),
    path('test/',include("allcourses.urls")),
    path('all/course-details',views.t_course,name="t_course"),
    path('start-learning/<slug:slug>',views.t_single,name="d_single"),
    path('details/<title>',views.main_course_single,name="main"),
    path('account/reset/password', views.ResetPassword.as_view(), name="PassReset"),
    path('accounts/password_reset/done/',views.ResetDone.as_view(),name = "password_reset_done"),
    path('accounts/reset/<uidb64>/<token>/',views.ResetConfirm.as_view(),name= "password_reset_confirm"),
    path('accounts/reset/done/',views.ResetComplete.as_view(),name="password_reset_complete"),
    path('search',views.search,name="search"),
    path('javascript-compiler',views.compiler_javascript,name="javascript"),
    path('html-compiler',views.compiler_html,name="html"),
]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)