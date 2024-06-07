from django.shortcuts import render
from.models import Student
from.forms import StudnetRegestion
from django.http import HttpResponseRedirect

# Create your views here.
def thenkyou(request):
   return render(request,'success.html')

def studentinfo(request):
    stu=Student.objects.all()
    return render(request, 'student.html',{'stu':stu}) 

def show_form(request):
    if request.method =='POST':
        fm=StudnetRegestion(request.POST)
        if fm.is_valid():
           
           first_name=fm.changed_data['first_name']
           last_name=fm.changed_data['last_name']
           email=fm.changed_data['email']
           batch=fm.changed_data['batch']
           password=fm.changed_data['password']
           return HttpResponseRedirect('/success/')


    else:
     frm=StudnetRegestion()
     frm.order_fields(field_order=['email','first_name','last_name','roll','password'])
    return render(request,'forms.html',{'form':frm})


