from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from clothing.forms import ClothingCreationForm
from clothing.models import Clothing


# PUBLIC VIEWS

class ClothingListView(ListView):
    model = Clothing
    template_name = 'clothing/clothing-list.html'
    context_object_name = 'clothings'
    paginate_by = 6


class ClothingDetailView(DetailView):
    model = Clothing
    template_name = 'clothing/clothing-detail.html'
    context_object_name = 'clothing'


# # ADMIN-ONLY VIEWS (Private)

class ClothingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'clothing.add_clothing'
    model = Clothing
    form_class = ClothingCreationForm
    template_name = 'clothing/clothing-create.html'
    success_url = reverse_lazy('clothing-list')


class ClothingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'clothing.change_clothing'
    model = Clothing
    form_class = ClothingCreationForm
    template_name = 'clothing/clothing-edit.html'

    def get_success_url(self):
        return reverse_lazy('clothing-detail', kwargs={'pk': self.object.pk})


class ClothingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'clothing.delete_clothing'
    model = Clothing
    template_name = 'clothing/clothing-delete.html'
    success_url = reverse_lazy('clothing-list')
