from django.shortcuts import render
from .models import StudentAlumni
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse

#Model Object - Single Student Data
def student_detail(request,pk):
    stu = StudentAlumni.objects.get(slNo=pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

#Query Set - All Student Data
def student_list(request):
    stu = StudentAlumni.objects.all()
    serializer = StudentSerializer(stu, many=True)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

