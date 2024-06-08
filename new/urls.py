from django.urls import path,register_converter
from . import views,conver
register_converter(conver.FourDigitYearConverter,'yyyy')

urlpatterns = [
    path('usercr/',views.usercreationform,name='usercr'),
     path('session/<yyyy:year>/',views.usercreationform,name='usercr'),

]
