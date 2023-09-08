from django.urls import path
from .views import resume_view


urlpatterns = [
    path('resumes', resume_view),
]
