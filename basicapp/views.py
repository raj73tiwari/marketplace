from django.shortcuts import redirect, render
from django.http import HttpResponse
from . import models
from . import forms
# Create your views here.

def index(request):
    # print(request.user.product)

    all_prods=models.Product.objects.all()
    context={'all_prods':all_prods}
    return render(request,'basicapp/index.html',context)

def owner(request,id):
    return HttpResponse(id)

def add_prod(request):     
    new_form=forms.Prod_form(request.POST or None,request.FILES or None)
    if new_form.is_valid():
        prod=new_form.save(commit=False)
        prod.user = request.user
        prod.save()
        return redirect('basicapp:index')

    context={'form':new_form}
    return render(request,'basicapp/add_prod_form.html',context)

def update_prod(request,prod_id):
    prod= models.Product.objects.get(id=prod_id)
    new_form=forms.Prod_form(request.POST or None ,request.FILES or None,instance=prod)
    if new_form.is_valid():
        new_form.save()
        return redirect('basicapp:index')
    context={'form':new_form, 'prod':prod}  
    print(prod)
    return render(request,'basicapp/add_prod_form.html',context)

def del_prod(request,prod_id):
    prod= models.Product.objects.get(id=prod_id)
    print(prod)
    if prod:
        prod.delete()
    return redirect('basicapp:index')  
    
    


    
