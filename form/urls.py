from django.urls import path
from . import views

urlpatterns=[
    path('form/redirect', views.redirect_view, name='redirect'),
    path('', views.home, name="home"),
    path('form/', views.form, name="form"),
    path('form/<str:pk>', views.form, name="edit"),
    path('form/redirect-edit/<str:id>', views.editredirect, name="edit"),
    # path('edit-form/', views.editform, name="editform"),
    path('resumes', views.resumes, name="resumes"),
    path('resume/<str:pk>', views.resume, name="resume"),
    path('delete/<str:id>', views.delete, name='delete'),
]

# How can we redirect to home page when an incorrect url is entered