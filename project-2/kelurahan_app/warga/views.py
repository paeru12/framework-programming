from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Warga, Pengaduan
from .forms import PengaduanForm

class WargaListView(ListView):
    model = Warga

class WargaDetailView(DetailView):
    model = Warga

class PengaduanCreateView(CreateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'

    def form_valid(self, form):
        warga_id = self.kwargs['warga_id']
        form.instance.pelapor_id = warga_id
        form.instance.status = 'Belum Diproses'
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('warga-detail', kwargs={'pk': self.kwargs['warga_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['warga_id'] = self.kwargs['warga_id']
        return context
