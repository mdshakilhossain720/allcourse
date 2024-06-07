from django.shortcuts import render
from.models import Student

# Create your views here.

def studentinfo(request):
    stu=Student.objects.all()
    return render(request, 'student.html',{'stu':stu}) 

