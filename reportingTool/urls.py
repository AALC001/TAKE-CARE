from django.urls import path
from . import views


urlpatterns = [
    path('', views.rpt_form, name="patient_insert"), # get and post req. for insert operation
    path('home/', views.home, name="home"),
    path('<int:id>/', views.rpt_form, name="patient_update"), # get and post req. for update operation
    path('delete/<int:id>/', views.rpt_delete, name="patient_delete"),
    path('list/', views.rpt_list, name="patient_list"), # get req. to retrieve and display all records
    path('register/', views.registerView, name="register"), # PATH Pour les comptes utilisateur
    path('report/', views.reportView, name="report"),
    #path('logout/', views.rpt_list, name="logout")
]
