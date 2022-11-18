from django.urls import path, re_path
from django.views.generic.base import RedirectView
from . import views

urlpatterns=[
    path('form/redirect', views.redirect_view, name='redirect'),
    path('form/', views.form, name="form"),
    path('form/<str:pk>', views.form, name="edit"),
    path('form/redirect-edit/<str:id>', views.editredirect, name="edit"),
    # path('edit-form/', views.editform, name="editform"),
    path('resumes', views.resumes, name="resumes"),
    path('resume/<str:pk>', views.resume, name="resume"),
    path('delete/<str:id>', views.delete, name='delete'),
    path('', views.home, name="home"),
    # re_path(r'^$', views.home),
]

# How can we redirect to home page when an incorrect url is entered