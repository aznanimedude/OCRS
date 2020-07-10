from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView
from mysite.models import Course
# Create your views here.

class IndexView(TemplateView):
    template_name="mysite/index.html"

class CourseListView(ListView):
    model = Course

class CourseDetailView(DetailView):
    model = Course

class EnrollCourseView(TemplateView):
    pass
