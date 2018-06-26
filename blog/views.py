from django.shortcuts import render, get_object_or_404, redirect
from .models import Address
from django.utils import timezone
from .forms import AddressForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def address_list(request):
    address = Address.objects.filter(published_date__isnull=False).order_by('created_date')
    return render(request, 'blog/address_draft_list.html', {'address': address})

def address_detail(request, pk):
    address = get_object_or_404(Address, pk=pk)
    return render(request, 'blog/address_detail.html', {'address': address})

@login_required
def address_new(request):
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.name
            address.created_date = timezone.now()
            address.save()
            return redirect('address_detail', pk=address.pk)
    else:
        form = AddressForm()
    return render(request, 'blog/address_edit.html', {'form': form})

@login_required
def address_edit(request, pk):
    address = get_object_or_404(Address, pk=pk)
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.name
            address.created_date = timezone.now()
            address.save()
            return redirect('address_detail', pk=address.pk)
    else:
        form = AddressForm(instance=address)
    return render(request, 'blog/address_edit.html', {'form': form})

@login_required
def address_draft_list(request):
    address = Address.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/address_draft_list.html', {'address': address})

@login_required
def address_publish(request, pk):
    address = get_object_or_404(Address, pk=pk)
    address.publish()
    return redirect('address_detail', pk=pk)

@login_required
def address_remove(request, pk):
    address = get_object_or_404(Address, pk=pk)
    address.delete()
    return redirect('address_list')
