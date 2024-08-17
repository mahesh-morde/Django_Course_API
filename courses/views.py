from rest_framework import generics
from .models import Course, CourseInstance
from .serializers import CourseSerializer, CourseInstanceSerializer

# List and Create Courses
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# Retrieve and Delete Course Details
class CourseDetailView(generics.RetrieveDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

# List and Create Course Instances for a Specific Year and Semester
class CourseInstanceListCreateView(generics.ListCreateAPIView):
    serializer_class = CourseInstanceSerializer

    def get_queryset(self):
        # This is used for listing instances by year and semester
        year = self.kwargs.get('year')
        semester = self.kwargs.get('semester')
        if year and semester:
            return CourseInstance.objects.filter(year=year, semester=semester)
        return CourseInstance.objects.all()  # Default to returning all instances

    def create(self, request, *args, **kwargs):
        # Create method handles POST requests to create a new instance
        return super().create(request, *args, **kwargs)

# Retrieve and Delete a Specific Course Instance
class CourseInstanceDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        pk = self.kwargs['pk']
        return CourseInstance.objects.get(pk=pk, year=year, semester=semester)
