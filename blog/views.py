from django.shortcuts import render, get_object_or_404, redirect
from .models import Address
from django.utils import timezone
from .forms import AddressForm
# Create your views here.

def address_list(request):
    address = Address.objects.order_by('created_date')
    return render(request, 'blog/address_list.html', {'address':address})

def address_detail(request, pk):
    address = get_object_or_404(Address, pk=pk)
    return render(request, 'blog/address_detail.html', {'address':address})

def address_new(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.name = request.user
            address.created_date = timezone.now()
            address.save()
            return redirect('address_detail', pk=address.pk)
    else:
        form = AddressForm()
    return render(request, 'blog/address_edit.html', {'form': form})

def address_edit(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.name = request.user
            address.created_date = timezone.now()
            address.save()
            return redirect('address_detail', pk=address.pk)
    else:
        form = AddressForm(instance=address)
    return render(request, 'blog/address_edit.html', {'form': form})