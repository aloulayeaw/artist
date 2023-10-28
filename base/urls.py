
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('effectuer-transaction/', views.effectuer_transaction, name='effectuer_transaction'),
    path('precommander/', views.paiement, name='payment'),
    path('payment/', views.payment_form_view, name='payment_form'),
    path('get_itunes_data/', views.get_itunes_data, name='get_itunes_data'),
    path('contact/', views.contact, name='contact_form'),
    #path('about', views.about, name='about'),
    #path('cartographie', views.cartographie, name='cartographie'),
]
