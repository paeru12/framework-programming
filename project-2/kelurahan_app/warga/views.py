from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Warga, Pengaduan
from .forms import PengaduanForm

class WargaListView(ListView):
    model = Warga
    template_name = 'warga/warga_list.html'


class WargaDetailView(DetailView):
    model = Warga
    template_name = 'warga/warga_detail.html'


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


class PengaduanUpdateView(UpdateView):
    model = Pengaduan
    form_class = PengaduanForm
    template_name = 'warga/pengaduan_form.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['warga_id'] = self.object.pelapor.id
        return context
    
    def form_valid(self, form):
        if not form.instance.pelapor:
            form.instance.pelapor = self.object.pelapor
        return super().form_valid(form)

    def get_success_url(self):
        pelapor = self.object.pelapor
        if pelapor: 
            return reverse_lazy('warga-detail', kwargs={'pk': pelapor.pk})
        else:
            return reverse_lazy('warga-list')

class PengaduanDeleteView(DeleteView):
    model = Pengaduan
    template_name = 'warga/pengaduan_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('warga-detail', kwargs={'pk': self.object.pelapor.pk})
