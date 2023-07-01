from mainapp.models import Student,School
from mainapp.api.serializers import StudentSerializer,SchoolSerializer
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

