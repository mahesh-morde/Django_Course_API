from django.urls import path
from .views import (
    CourseListCreateView, CourseDetailView,
    CourseInstanceListCreateView, CourseInstanceDetailView, 
    AllCourseInstanceListView
)

urlpatterns = [
    # Course operations
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),

    # Instance operations
    path('instances/', AllCourseInstanceListView.as_view(), name='all-instance-list'),  # List all instances
    path('instances/create/', CourseInstanceListCreateView.as_view(), name='instance-create'),  # Create instance
    path('instances/<int:year>/<int:semester>/', CourseInstanceListCreateView.as_view(), name='instance-list'),  # List by year and semester
    path('instances/<int:year>/<int:semester>/<int:pk>/', CourseInstanceDetailView.as_view(), name='instance-detail'),  # Retrieve/delete specific instance
]

