from django.urls import path
from mysite import views

app_name='mysite'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('courses/',views.CourseListView.as_view(),name='courses'),
    path('courses/<int:pk>/',views.CourseDetailView.as_view(),name="course_detail"),
]
