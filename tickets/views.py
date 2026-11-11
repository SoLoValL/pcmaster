from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from .models import Ticket


def ticket_list(request):
    if request.user.is_authenticated:
        tickets = Ticket.objects.filter(client=request.user).order_by('-created_at')
    else:
        tickets = Ticket.objects.none()
    return render(request, 'tickets/ticket_list.html', {'tickets': tickets})


@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.client = request.user
            ticket.save()
            messages.success(request, 'Заявка отправлена!')
            return redirect('tickets:list')
    else:
        form = TicketForm()
    return render(request, 'tickets/ticket_form.html', {'form': form})


@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if ticket.client != request.user and not request.user.is_superuser:
        messages.error(request, 'Доступ запрещён')
        return redirect('tickets:list')
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})
