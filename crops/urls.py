# crops/urls.py
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import (
    CropListView,
    CropDetailView,
    CropCreateView,
    CropUpdateView,
    CropDeleteView,
    CropList, 
    CropDetail,  
)

urlpatterns = [
    path('crops/', CropListView.as_view(), name='crop_list'),
    path('crops/<int:pk>/', CropDetailView.as_view(), name='crop_detail'),
    path('crops/new/', CropCreateView.as_view(), name='crop_create'),
    path('crops/<int:pk>/edit/', CropUpdateView.as_view(), name='crop_edit'),
    path('crops/<int:pk>/delete/', CropDeleteView.as_view(), name='crop_delete'),
    # API URLs
    path('api/crops/', CropList.as_view(), name='api_crop_list'),
    path('api/crops/<int:pk>/', CropDetail.as_view(), name='api_crop_detail'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
