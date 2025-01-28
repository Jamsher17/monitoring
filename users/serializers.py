from rest_framework import serializers
from .models import Student, Teacher, Parent

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'username', 'fname', 'lname', 'middle_name', 'dob', 'phone_num', 'email', 'is_staff', 'created_date', 'updated_date']



class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'



class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'