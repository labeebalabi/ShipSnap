from django.urls import path
from .views import *

urlpatterns=[
     path('cust',CustHome.as_view(),name='h'),
     path('about',AboutHome.as_view(),name='about'),
     path('ser',ServiceHome.as_view(),name='ser'),
     path('request',RequestView.as_view(),name='request'),
     path('ship/<int:id>',ShippingView.as_view(),name='ship'),
     path('bill/<int:pk>/',ShipBillView.as_view(),name='bill'),
     path('pay/<int:id>/',PaymentView.as_view(),name="pay"),
     path('order',OrderListView.as_view(),name='order'),
     path('delete/<int:id>',DeleteOrder,name='delete'),
     path('saves/<int:id>',SaveLaterView,name='savelater'),
     path('nextorder',NextOrderView.as_view(),name='fornext'),
     path('deletenext/<int:id>',DeleteNext,name='deletenext'),
     path('nextpay/<int:id>',continenext,name='coninue'),

     
     path("lgout",LgOutView.as_view(),name='lgout'),
   
   
]