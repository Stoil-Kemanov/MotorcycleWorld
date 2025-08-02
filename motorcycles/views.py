from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView

from motorcycles.choices import CategorySearch
from motorcycles.forms import UniversalSearchForm, MotorcycleCreationForm, MotorcyclePartsCreationForm, \
    MotorcycleAccessoriesCreationForm
from motorcycles.models import Motorcycle, MotorcycleParts, MotorcycleAccessories


# PUBLIC VIEWS

class UniversalSearchView(TemplateView):
    # searches across motorcycles, parts and accessories

    template_name = 'motorcycles/search-results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        form = UniversalSearchForm(self.request.GET)
        motorcycles = Motorcycle.objects.none()
        parts = MotorcycleParts.objects.none()
        accessories = MotorcycleAccessories.objects.none()
        total_results = 0

        if form.is_valid():
            search = form.cleaned_data.get('search', '')
            category = form.cleaned_data.get('category', CategorySearch.ALL)
            min_price = form.cleaned_data.get('min_price')
            max_price = form.cleaned_data.get('max_price')

            if search or min_price or max_price:

                if category == CategorySearch.ALL or category == CategorySearch.MOTORCYCLES:
                    motorcycles = Motorcycle.objects.all()

                if category == CategorySearch.ALL or category == CategorySearch.PARTS:
                    parts = MotorcycleParts.objects.all()

                if category == CategorySearch.ALL or category == CategorySearch.ACCESSORIES:
                    accessories = MotorcycleAccessories.objects.all()

                if search:
                    motorcycles = motorcycles.filter(
                        Q(make__icontains=search) |
                        Q(model__icontains=search)
                    )
                    parts = parts.filter(
                        Q(name__icontains=search) |
                        Q(make__icontains=search) |
                        Q(description__icontains=search)
                    )
                    accessories = accessories.filter(
                        Q(name__icontains=search) |
                        Q(make__icontains=search) |
                        Q(description__icontains=search)
                    )

                if min_price:
                    motorcycles = motorcycles.filter(price__gte=min_price)
                    parts = parts.filter(price__gte=min_price)
                    accessories = accessories.filter(price__gte=min_price)

                if max_price:
                    motorcycles = motorcycles.filter(price__lte=max_price)
                    parts = parts.filter(price__lte=max_price)
                    accessories = accessories.filter(price__lte=max_price)

                total_results = motorcycles.count() + parts.count() + accessories.count()

        context.update({
            'form': form,
            'motorcycles': motorcycles[:10],
            'parts': parts[:10],
            'accessories': accessories[:10],
            'total_results': total_results,
            'search_performed': bool(
                self.request.GET.get('search') or self.request.GET.get('min_price') or self.request.GET.get(
                    'max_price')),
        })

        return context


class MotorcycleListView(ListView):
    model = Motorcycle
    template_name = 'motorcycles/motorcycle-list.html'
    context_object_name = 'motorcycles'
    paginate_by = 6


class MotorcycleDetailView(DetailView):
    model = Motorcycle
    template_name = 'motorcycles/motorcycle-detail.html'
    context_object_name = 'motorcycle'


class PartsListView(ListView):
    model = MotorcycleParts
    template_name = 'motorcycles/parts-list.html'
    context_object_name = 'parts'
    paginate_by = 9


class PartsDetailView(DetailView):
    model = MotorcycleParts
    template_name = 'motorcycles/parts-detail.html'
    context_object_name = 'part'


class AccessoriesListView(ListView):
    model = MotorcycleAccessories
    template_name = 'motorcycles/accessories-list.html'
    context_object_name = 'accessories'
    paginate_by = 9


class AccessoriesDetailView(DetailView):
    model = MotorcycleAccessories
    template_name = 'motorcycles/accessories-detail.html'
    context_object_name = 'accessory'


# ADMIN-ONLY VIEWS (Private)

def is_staff_user(user):
    return user.is_staff


class MotorcycleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Motorcycle
    form_class = MotorcycleCreationForm
    template_name = 'motorcycles/admin-motorcycle-create.html'
    success_url = reverse_lazy('motorcycle-list')

    def test_func(self):
        return is_staff_user(self.request.user)


class MotorcycleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Motorcycle
    form_class = MotorcycleCreationForm
    template_name = 'motorcycles/admin-motorcycle-edit.html'
    success_url = reverse_lazy('motorcycle-list')

    def test_func(self):
        return is_staff_user(self.request.user)


class MotorcycleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Motorcycle
    template_name = 'motorcycles/admin-motorcycle-delete.html'
    success_url = reverse_lazy('motorcycle-list')

    def test_func(self):
        return is_staff_user(self.request.user)


class PartsCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MotorcycleParts
    form_class = MotorcyclePartsCreationForm
    template_name = 'motorcycles/parts-create.html'
    success_url = reverse_lazy('parts-list')

    def test_func(self):
        return is_staff_user(self.request.user)


class PartsUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MotorcycleParts
    form_class = MotorcyclePartsCreationForm
    template_name = 'motorcycles/parts-edit.html'

    def get_success_url(self):
        return reverse_lazy('parts-detail', kwargs={'pk': self.object.pk})

    def test_func(self):
        return is_staff_user(self.request.user)


class PartsDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MotorcycleParts
    template_name = 'motorcycles/parts-delete.html'
    success_url = reverse_lazy('parts-list')

    def test_func(self):
        return is_staff_user(self.request.user)


class AccessoriesCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = MotorcycleAccessories
    form_class = MotorcycleAccessoriesCreationForm
    template_name = 'motorcycles/accessories-create.html'
    success_url = reverse_lazy('accessories-list')

    def test_func(self):
        return is_staff_user(self.request.user)


class AccessoriesUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = MotorcycleAccessories
    form_class = MotorcycleAccessoriesCreationForm
    template_name = 'motorcycles/accessories-edit.html'
    success_url = reverse_lazy('accessories-list')

    def test_func(self):
        return is_staff_user(self.request.user)


class AccessoriesDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = MotorcycleAccessories
    template_name = 'motorcycles/accessories-delete.html'
    success_url = reverse_lazy('accessories-list')

    def test_func(self):
        return is_staff_user(self.request.user)
