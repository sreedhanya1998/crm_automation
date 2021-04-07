"""parkingsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from crm_automation.views import Login,create_course,Logout,course_list,Detail_view,detail_list,course_view,course_edit,course_delete,coursedetail,about_course,Stu_reg,Stud_login,Registration_for,admission_list,admission,counsillorpage,Payment,Feepaymentlist,Finallist,studlogout
from django.contrib.auth.admin import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login',Login.as_view(),name="login"),
    path('create',create_course.as_view(),name="create"),
    path("logout",Logout.as_view(),name="logout"),
    path("list",course_list.as_view(),name="list"),
    path("detail",Detail_view.as_view(),name="detail"),
    path("detaillist",detail_list.as_view(),name="detaillist"),
    path("view/<int:pk>",course_view.as_view(),name="view"),
    path("edit/<int:pk>",course_edit.as_view(),name="edit"),
    path('delete/<int:pk>',course_delete.as_view(),name="delete"),
    path("detaillisting",coursedetail.as_view(),name="detaillisting"),
    path("about",about_course.as_view(),name="about"),
    path("stud",Stu_reg.as_view(),name="stud"),
    path("studlogin",Stud_login.as_view(),name="studlogin"),
    path("register",Registration_for.as_view(),name="register"),
    path("admitted/<str:enquiry_id>",admission.as_view(),name="admitted"),
    path("admitlist",admission_list.as_view(),name="admitlist"),
    path("counsil",counsillorpage.as_view(),name="counsil"),
    path("pay/<str:admission_no>",Payment.as_view(),name="pay"),
    path('paylist',Feepaymentlist.as_view(),name="paylist"),
    path("finallist",Finallist.as_view(),name="finallist"),
    path("studlogout",studlogout.as_view(),name="studlogout"),
    # path("deleting",admission_list_delete.as_view(),name="deleting")




]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
