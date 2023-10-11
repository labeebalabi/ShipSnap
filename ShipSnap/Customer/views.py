from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,CreateView,FormView,DetailView,ListView
from django.contrib.auth import authenticate,login,logout
from django.contrib.sessions.models import Session
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse_lazy
from Account.models import *
from django.urls import reverse
from django.http import HttpResponseRedirect
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
def signin_required(fn):
    def inner(request,*args,**kwargs):
                if request.user.is_authenticated:
                    return fn(request,*args,**kwargs)
                else:
                     messages.error(request,"login first............")
                     return redirect('log')
                
    return inner

decs = [never_cache,signin_required]

@method_decorator(decs,name='dispatch')
class CustHome(TemplateView) :
    template_name="cust_home.html"

@method_decorator(decs,name='dispatch') 
class AboutHome(TemplateView):
    template_name="abouts.html"
@method_decorator(decs,name='dispatch')   
class ServiceHome(TemplateView):
    template_name="services.html"
    

@method_decorator(decs,name='dispatch')
class RequestView(View):
    def get(self,request):
        form=ProductForm()
        return render(request,"request.html",{'form':form})
    def post(self,request):
        form = ProductForm(data=request.POST)
        if form.is_valid():
            # form_data=form.cleaned_data
            x=form.cleaned_data['weight']
            y=form.cleaned_data['kilo_meter']
            z=form.cleaned_data['Goodscategory']
            print(x,y,z)
            p=0
            if z in d1.keys():
                print(d1[z])
                w=d1[z]
                p=w*x*y
                print(p)

            x=Product.objects.create(Goodscategory=z,weight=x,kilo_meter=y,price=p)
            # context={'id':x}
            return redirect('ship',id=x.id)
        return render(request,'request.html',{'form':form})


@method_decorator(decs,name='dispatch')
class ShippingView(CreateView):
    template_name = "shippingdata.html"
    model = ShipModel
    fields = ['fr_name', 'fr_phone', 'fr_landmark', 'fr_district', 'fr_addrss', 'to_name', 'to_phone', 'to_landmark', 'to_district', 'to_addrss']
    success_url = reverse_lazy('bill')

    def form_valid(self, form):
        product_id = self.kwargs['id']
        product = get_object_or_404(Product, id=product_id)
        form.instance.product = product

        # The following line automatically saves the form and creates the ShipModel instance
        self.object = form.save()

        # Store the ID in the session
        session_key = self.request.session.session_key
        if not session_key:
            self.request.session.save()

        # Store the ShipModel instance ID in the session
        self.request.session['new_shipmodel_id'] = self.object.id
        self.success_url = reverse_lazy('bill', kwargs={'pk': self.object.pk})

        return super().form_valid(form)

        
    # def get_success_url(self):
    #     # Use the ID of the created ShipModel instance to build the success URL
    #     ship_id = self.object.id
    #     return reverse_lazy('h') + f'?ship_id={ship_id}'
    
    #     # return render(request,'home.html',{'form':form_data})

@method_decorator(decs,name='dispatch')
class ShipBillView(DetailView):
    template_name="shipDetails.html"
    model=ShipModel
    context_object_name="shipdetail"

@method_decorator(decs,name='dispatch')    
class PaymentView(View):
    def get(self,request,id):
        # id=kwargs.get(id=id)
        obj=ShipModel.objects.get(id=id)
        # print(id.fr_name)
        return render(request,"payment.html",{'object':obj})
    def post(self,request,**kwargs):
        id=kwargs.get('id')
        ship=ShipModel.objects.get(id=id)
        usr=request.user
        order.objects.create(ship=ship,user=usr)
        messages.success(request,"Your Slot successfully Booked. We will pick item soon!.............")
        return redirect('h')
    
@method_decorator(decs,name='dispatch')
class OrderListView(ListView):
     template_name='myorder.html'
     queryset=order.objects.all()
     context_object_name='order'

def DeleteOrder(request,**kwargs):
    pid=kwargs.get('id')

    c=order.objects.get(id=pid)
    if c.Status=='Shipped':
        return redirect('order')
    else :
        c.delete()
        return redirect('order')
def SaveLaterView(request,**kwargs):
    shid=kwargs.get('id')
    ship=ShipModel.objects.get(id=shid)
    user=request.user
    save.objects.create(ship=ship,user=user)

    return redirect('fornext')

@method_decorator(decs,name='dispatch')
class NextOrderView(ListView):
    template_name='nextorder.html'
    queryset=save.objects.all()
    context_object_name='save'

def DeleteNext(request,**kwargs):
    pid=kwargs.get('id')
    save.objects.get(id=pid).delete()
    return redirect('fornext')


def continenext(request,**kwargs):
    id=kwargs.get('id')
    sv=save.objects.get(id=id)
    shid=sv.ship
    shid_id = shid.id  # Extract the ID or relevant attribute from shid

    # Use the 'reverse' function to generate the URL for 'pay' with the shid_id argument
    url = reverse('pay', args=[shid_id])

    sv.delete()

    # Redirect to the generated URL
    return HttpResponseRedirect(url)
@method_decorator(decs,name='dispatch')
class LgOutView(View):
    def get(self,request):
        logout(request) 
        return redirect("login")   

