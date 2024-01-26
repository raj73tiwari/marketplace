from django.shortcuts import redirect, render, get_object_or_404
from . import models
from . import forms
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def index(request):
    all_prods=models.Product.objects.all()
    context={'all_prods':all_prods}
    return render(request,'basicapp/index.html',context)

@login_required
def my_prods(request):
    my_prods=request.user.products.all()
    context={'my_prods':my_prods}
    return render(request,'basicapp/my_products.html',context)

@login_required
def owner(request,id):
    owner=get_object_or_404(User, id=id)
    context={'owner':owner}
    return render(request,'basicapp/owner_profile.html',context)

@login_required
def add_prod(request):
    if request.method == 'POST':     
        new_form=forms.ProdForm(request.POST ,request.FILES )
        if new_form.is_valid():
            prod=new_form.save(commit=False)
            prod.user = request.user
            prod.save()
            messages.success(request,'Product Added Successfully !')
            return redirect('basicapp:myprods')
        else:
            print(new_form.errors)
            messages.error(request,'Please Enter Correct Data !')
    else:
        new_form=forms.ProdForm()
    context={'form':new_form}
    return render(request,'basicapp/add_prod_form.html',context)

@login_required
def update_prod(request,prod_id):
    prod = get_object_or_404(models.Product, id=prod_id)
    if request.user != prod.user:
        messages.error(request, 'You are not authorized to update this product.')
        return redirect('basicapp:myprods')
    if request.method == 'POST':
         form = forms.ProdForm(request.POST, request.FILES, instance=prod)
         if form.is_valid():
            form.save()
            messages.success(request,'Product Updated Successfully !')
            return redirect('basicapp:myprods')
         else:
            print(form.errors)
            messages.error(request,'Please Enter Correct Data !')
    else:
        form = forms.ProdForm(instance=prod)
    context={'form':form, 'prod':prod}  
    return render(request,'basicapp/update_prod_form.html',context)

@login_required
def del_prod(request,prod_id):
    prod = get_object_or_404(models.Product, id=prod_id)
    if request.user != prod.user:
        messages.error(request, 'You are not authorized to delete this product.')
        return redirect('basicapp:myprods')
    prod.delete()
    messages.success(request,'Product Deleted Successfully !')
    return redirect('basicapp:myprods')  
    



    


    
