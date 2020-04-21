from django.urls import path
from .views import homepage,about,hyderabad,amritsar,bangalore,kochin,mumbai,pondi,varanasi,delhi,jak,goa,Booking,contact
app_name = 'travelapp'

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('hyderabad/', hyderabad, name='hyderabad'),
    path('amritsar/', amritsar, name='amritsar'),
    path('bangalore/', bangalore, name='bangalore'),
    path('kochin/', kochin, name='kochin'),
    path('mumbai/', mumbai, name='mumbai'),
    path('pondi/', pondi, name='pondi'),
    path('varanasi/', varanasi, name='varanasi'),
    path('delhi/', delhi, name='delhi'),
    path('goa/', goa, name='goa'),
    path('jak/', jak, name='jak'),
    path('book/', Booking, name='Booking'),

]