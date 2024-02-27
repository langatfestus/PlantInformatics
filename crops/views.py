from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Crop
from rest_framework import generics
from .serializer import CropSerializer

class CropList(generics.ListCreateAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class CropDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class CropListView(ListView):
    model = Crop
    template_name = 'crops/crop_list.html'
    context_object_name = 'all_crops_list'

class CropDetailView(DetailView):
    model = Crop
    template_name = 'crops/crop_detail.html'
    context_object_name = 'crop'

class CropCreateView(CreateView):
    model = Crop
    template_name = 'crops/crop_new.html'
    fields = ['name', 'description', 'planting_season', 'harvest_season', 'maturity_period', 'image']
    success_url = reverse_lazy('crop_list')

class CropUpdateView(UpdateView):
    model = Crop
    template_name = 'crops/crop_edit.html'
    fields = ['name', 'description', 'planting_season', 'harvest_season', 'maturity_period', 'image']

class CropDeleteView(DeleteView):
    model = Crop
    template_name = 'crops/crop_delete.html'
    success_url = reverse_lazy('crop_list')

def crop_list(request):
    crops = Crop.objects.all()
    return render(request, 'crops/crop_list.html', {'crops': crops})

def crop_detail(request, pk):
    crop = Crop.objects.get(id=pk)
    return render(request, 'crops/crop_detail.html', {'crop': crop})
