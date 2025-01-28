from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from .models import Student, Teacher, Parent
from .serializers import StudentSerializer, TeacherSerializer, ParentSerializer

# class StudentListCreate(generics.ListCreateAPIView):
#     queryset = Student.object.all()
#     serializer_class = StudentSerializer
#     # delete all the students
#     def delete(self, request,*args, **kwargs):
#         Student.objects.all().delete()
#         return Response (status=status.HTTP_204_NO_CONTENT)

# # access individual Student, update and delete the student
# class StudentRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Student.object.all()
#     serializer_class = StudentSerializer
#     look_up = 'pk'





class StudentAPIView(APIView):
    def get(self, request, pk=None):
        """Handle GET requests. Fetch a single student or all students."""
        if pk:
            # Get a specific student by primary key
            try:
                student = Student.objects.get(pk=pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data)
            except Student.DoesNotExist:
                return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            # Get all students
            students = Student.objects.all()
            serializer = StudentSerializer(students, many=True)
            return Response(serializer.data)

    def post(self, request):
        """Handle POST requests to create a new student."""
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handle PUT requests to update an existing student."""
        try:
            student = Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        """Handle DELETE requests to remove a student."""
        try:
            student = Student.objects.get(pk=pk)
            student.delete()
            return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
