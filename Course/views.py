from rest_framework.generics import CreateAPIView
from .models import Course
from .serializers import CourseSerializer


class CreateCourseAPI(CreateAPIView):
    serializer_class = CourseSerializer
    queryset = Course
