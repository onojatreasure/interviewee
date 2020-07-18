from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.interviewee_form,name='interviewee_insert'), # get and post req. for insert operation
    path('<int:id>/', views.interviewee_form,name='interviewee_update'), # get and post req. for update operation
    path('delete/<int:id>/',views.interviewee_delete,name='interviewee_delete'),
    path('list/',views.interviewee_list,name='interviewee_list') # get req. to retrieve and display all records
]