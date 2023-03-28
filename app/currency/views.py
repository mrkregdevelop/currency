from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from currency.models import Rate, ContactUs
from currency.forms import RateForm


class RateListView(ListView):
    template_name = 'rates_list.html'
    queryset = Rate.objects.all().select_related('source')


class RateDetailView(DetailView):
    queryset = Rate.objects.all()
    template_name = 'rates_details.html'


class RateCreateView(CreateView):
    form_class = RateForm
    template_name = 'rates_create.html'
    success_url = reverse_lazy('currency:rate-list')


class RateUpdateView(UpdateView):
    form_class = RateForm
    template_name = 'rates_update.html'
    success_url = reverse_lazy('currency:rate-list')
    queryset = Rate.objects.all()


class RateDeleteView(DeleteView):
    queryset = Rate.objects.all()
    template_name = 'rates_delete.html'
    success_url = reverse_lazy('currency:rate-list')


class ContactUsCreateView(CreateView):
    template_name = 'contactus_create.html'
    success_url = reverse_lazy('index')
    model = ContactUs
    fields = (
        'name',
        'email',
        'subject',
        'message'
    )

    def _send_mail(self):
        subject = 'User ContactUs'
        recipient = settings.DEFAULT_FROM_EMAIL
        message = f'''
            Request from: {self.object.name}. 
            Reply to email: {self.object.email}. 
            Subject: {self.object.subject}, 
            Body: {self.object.message}
        '''
        from currency.tasks import send_mail
        # send_mail.delay(subject, message)
        # send_mail.apply_async(args=[subject, message])
        '''
        0 - 8.59 | 9.00 - 19.00 | 19.01 23.59
           9.00  |    send      | 9.00 next day
        '''
        from datetime import datetime, timedelta
        send_mail.apply_async(
            kwargs={'subject': subject, 'message': message},
            # countdown=20
            # eta=datetime(2023, 3, 28, 20, 49, 0)
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)
        self._send_mail()
        return redirect
