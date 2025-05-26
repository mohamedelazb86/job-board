from django.urls import path
from . import views

app_name='job'

urlpatterns = [
    path('',views.job_list,name='job-list'),
    path('add_job/<str:slug>',views.add_job,name='add-job'),
    path('eng',views.eng,name='eng'),
    path('<slug:slug>',views.job_detail,name='job-detail'),
    

]

