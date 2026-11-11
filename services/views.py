from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Service


def service_list(request):
    services = Service.objects.filter(is_published=True).order_by('-created_at')
    return render(request, 'services/service_list.html', {'services': services})


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk, is_published=True)
    return render(request, 'services/service_detail.html', {'service': service})


@login_required
def service_create(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Услуга создана!')
            return redirect('services:list')
    else:
        form = ServiceForm()
    return render(request, 'services/service_form.html', {'form': form})
