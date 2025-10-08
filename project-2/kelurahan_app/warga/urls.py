from django.urls import path
from .views import (
    WargaListView,
    WargaDetailView,
    PengaduanCreateView,
    PengaduanUpdateView,
    PengaduanDeleteView,
)

urlpatterns = [
    path('', WargaListView.as_view(), name='warga-list'),
    path('<int:pk>/', WargaDetailView.as_view(), name='warga-detail'),

    # URL pengaduan
    path('pengaduan/tambah/<int:warga_id>/', PengaduanCreateView.as_view(), name='pengaduan-tambah'),
    path('pengaduan/<int:pk>/edit/', PengaduanUpdateView.as_view(), name='pengaduan-edit'),
    path('pengaduan/<int:pk>/hapus/', PengaduanDeleteView.as_view(), name='pengaduan-hapus'),
]
