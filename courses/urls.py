"""
URLs for courses.
"""
from django.urls import re_path  # pylint: disable=unused-import
from django.views.generic import TemplateView  # pylint: disable=unused-import
from .views import CourseListView

urlpatterns = [
    re_path(r'/courses/', CourseListView.as_view(), name="courses"),
]
