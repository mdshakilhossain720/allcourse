from django.urls import path
from . import views

urlpatterns = [
    path('form/',views.show_form,name='form'),
    path('student/',views.studentinfo,name='student'),
    path('success/',views.thenkyou),
    
]
