from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from services.forms import ServiceCreationForm
from services.models import Service


# PUBLIC VIEWS

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service-list.html'
    context_object_name = 'services'
    paginate_by = 6


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service-detail.html'
    context_object_name = 'service'


# # ADMIN-ONLY VIEWS (Private)

class ServiceCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'services.add_service'
    model = Service
    form_class = ServiceCreationForm
    template_name = 'services/service-create.html'
    success_url = reverse_lazy('service-list')


class ServiceUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'services.change_service'
    model = Service
    form_class = ServiceCreationForm
    template_name = 'services/service-edit.html'

    def get_success_url(self):
        return reverse_lazy('service-detail', kwargs={'pk': self.object.pk})


class ServiceDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'services.delete_service'
    model = Service
    template_name = 'services/service-delete.html'
    success_url = reverse_lazy('service-list')
