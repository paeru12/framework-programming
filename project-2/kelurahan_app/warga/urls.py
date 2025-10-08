from django.urls import path
from .views import WargaListView, WargaDetailView, PengaduanCreateView

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),
    path('pengaduan/tambah/<int:warga_id>/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
]