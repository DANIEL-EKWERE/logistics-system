from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'index.html' )

def about(request):
    return render(request,'about.html' )

def booking(request):
    return render(request,'booking.html' )

def career(request):
    return render(request,'career.html' )

def contact(request):
    return render(request,'contact.html' )

def courier(request):
    return render(request,'courier.html' )

def courierServices(request):
    return render(request,'courier-services.html' )

def distributionTransportation(request):
    return render(request,'distribution-transportation.html' )

def ecommerceLogistics(request):
    return render(request,'e-commerce-logistics.html' )

def exportImport(request):
    return render(request,'export-import.html' )

def globalFreightForwarding(request):
    return render(request,'global-freight-forwarding.html' )

def googleDownload(request):
    return render(request,'google-download.html' )

def warehouse(request):
    return render(request,'warehouse.html' )

def tracking(request):
    return render(request,'tracking.html' )

def trackingPage(request):
    return render(request,'tracking-page.html' )

