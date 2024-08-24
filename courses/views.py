from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
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
        # List instances by year and semester
        year = self.kwargs.get('year')
        semester = self.kwargs.get('semester')
        if year and semester:
            return CourseInstance.objects.filter(year=year, semester=semester)
        return CourseInstance.objects.all()

    def perform_create(self, serializer):
        # Allow course details to be passed via request data (if necessary)
        course_id = self.request.data.get('course')
        course = Course.objects.get(id=course_id)
        serializer.save(course=course)

# Retrieve and Delete a Specific Course Instance
class CourseInstanceDetailView(generics.RetrieveDestroyAPIView):
    serializer_class = CourseInstanceSerializer

    def get_object(self):
        year = self.kwargs['year']
        semester = self.kwargs['semester']
        pk = self.kwargs['pk']
        try:
            return CourseInstance.objects.get(pk=pk, year=year, semester=semester)
        except CourseInstance.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance is None:
            return Response([], status=status.HTTP_200_OK)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

# Retrieve all instances
class AllCourseInstanceListView(generics.ListAPIView):
    queryset = CourseInstance.objects.all()
    serializer_class = CourseInstanceSerializer
