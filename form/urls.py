from django.urls import path
from . import views

urlpatterns=[
    path('form/redirect', views.redirect_view, name='redirect'),
    path('', views.home, name="home"),
    path('form/', views.form, name="form"),
    path('resumes', views.resumes, name="resumes"),
    path('resume/<str:pk>', views.resume, name="resume"),
    path('delete/<int:id>', views.delete, name='delete'),
]