from rest_framework import serializers
from .models import Course, CourseInstance

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class CourseInstanceSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)  # Include course details in the instance response

    class Meta:
        model = CourseInstance
        fields = '__all__'
