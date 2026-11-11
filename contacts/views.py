from django.shortcuts import render
from django.contrib import messages
from .forms import ContactForm


def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Сообщение отправлено! Мы свяжемся с вами.')
            return redirect('contacts:index')
    else:
        form = ContactForm()
    return render(request, 'contacts/contact.html', {'form': form})
