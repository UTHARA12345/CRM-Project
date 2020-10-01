"""enquiry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from enq.views import *

urlpatterns = [
    path('home',DashBoard.as_view(),name="home"),
    path('listenquiry',Enquiry_list.as_view(),name="listenquiry"),
    path('createenquiry',Enquiry_Create.as_view(),name="createenquiry"),
    path('detailenquiry/<str:pk>',EnquiryDetail.as_view(),name="detailenquiry"),
    path('updateenquiry/<str:pk>',EnquiryUpdate.as_view(),name="updateenquiry"),
    path('deleteenquiry/<str:pk>',EnquiryDelete.as_view(),name="deleteenquiry"),
    path('followup',FollowUp.as_view(),name="followup"),
    path('followupdetails/<str:pk>',FollowUpDetail.as_view(),name="followupdetails"),
    path('searchdate',SearchDate.as_view(),name="searchdate"),
    path('report/>',ReportUpdate.as_view(),name="report"),
    path('search',SearchName.as_view(),name="search"),
    path('searchname',Search,name="searchname"),

    path('addcourse',AddCourse.as_view(),name="addcourse"),
    path('courseupdate/<int:pk>',CourseUpdate.as_view(),name="courseupdate"),
    path('coursedelete/<int:pk>',CourseDelete.as_view(),name="coursedelete"),

    path('addbatch',AddBatch.as_view(),name="addbatch"),
    path('updatebatch/<int:pk>',BatchUpdate.as_view(),name="updatebatch"),
    path('deletebatch/<int:pk>',BatchDelete.as_view(),name="deletebatch"),
    path('batchreport/<int:pk>',BatchReport.as_view(),name="batchreport"),

    path('addcouncillor',AddCouncillor.as_view(),name="addcouncillor"),
    path('updatecouncillor/<int:pk>',CouncillorUpdate.as_view(),name="updatecouncillor"),
    path('deletecouncillor/<int:pk>',CouncillorDelete.as_view(),name="deletecouncillor"),

    path('newadmission/<str:pk>',NewAdmission.as_view(),name="newadmission"),
    path('payment/<str:pk>',PaymentDetails.as_view(),name="payment"),
    path('pay',Pay.as_view(),name="pay"),
    # path('admilist',Admission_list.as_view(),name="admilist"),

    path('',RegistrationPage.as_view(),name="registration"),
    path('login',LoginUser.as_view(),name="login"),
    path('logsout',logoutuser,name="logsout"),

    path('viewbatch',ViewBatch.as_view(),name="viewbatch"),
    path('viewbatchgo',ViewBatchOngoing.as_view(),name="viewbatchgo"),
]
