from django.urls import path
from .views import home, about,career,booking,contact,courier,courierServices,distributionTransportation,ecommerceLogistics,exportImport,globalFreightForwarding,googleDownload,warehouse,tracking,trackingPage

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('booking/', booking, name='booking'),
    path('career/', career, name='career'),
    path('contact/', contact, name='contact'),
    path('courier/', courier, name='courier'),
    path('courier-service/', courierServices, name='courier-service'),
    path('distribution-transportation/', distributionTransportation, name='distribution-transportation'),
    path('e-commerce-logistics/', ecommerceLogistics, name='e-commerce-logistics'),
    path('export-import/', exportImport, name='export-import'),
    path('global-freight-forwarding/', globalFreightForwarding, name='global-freight-forwarding'),
    path('google-down/', googleDownload, name='google-download'),
    path('warehouse/', warehouse, name='warehouse'),
    path('tracking/', tracking, name='tracking'),
    path('tracking-page/', trackingPage, name='tracking-page'),
]
