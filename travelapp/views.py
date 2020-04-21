from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect,HttpResponse
  
from django.contrib.auth.decorators import login_required

# Create your views here.
def homepage(request):
    #return HttpResponse("Home page")
    return render(request, 'index.html')

def about(request):
    #return HttpResponse("Home page")
    return render(request, 'about.html')
    

def contact(request):
    #return HttpResponse("Home page")
    return render(request, 'contact.html')

@login_required
def hyderabad(request):
    #return HttpResponse("Home page")
    return render(request, 'hyderabad.html')

@login_required
def amritsar(request):
    #return HttpResponse("Home page")
    return render(request, 'amritsar.html')

@login_required
def bangalore(request):
    #return HttpResponse("Home page")
    return render(request, 'bangalore.html')

@login_required
def kochin(request):
    #return HttpResponse("Home page")
    return render(request, 'kochin.html')

@login_required
def mumbai(request):
    #return HttpResponse("Home page")
    return render(request, 'mumbai.html')

@login_required
def pondi(request):
    #return HttpResponse("Home page")
    return render(request, 'pondi.html')

@login_required
def varanasi(request):
    #return HttpResponse("Home page")
    return render(request, 'varanasi.html')

@login_required
def goa(request):
    #return HttpResponse("Home page")
    return render(request, 'goa.html')

@login_required
def delhi(request):
    #return HttpResponse("Home page")
    return render(request, 'delhi.html')

@login_required
def jak(request):
    #return HttpResponse("Home page")
    return render(request, 'jak.html')


@login_required
def Booking(request):
    if request.method == 'POST':

        return render(request, 'bill.html')
    else:
        return render(request, 'book.html')