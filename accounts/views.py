from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, TemplateView
from django.contrib import messages
from accounts.utils import recommend_motorcycles, recommend_clothing, get_compatibility_color

from accounts.forms import MotoUserCreationForm, ProfileForm, OwnedMotorcycleForm
from accounts.models import MotoUser, Profile, OwnedMotorcycle


class RegisterView(CreateView):
    model = MotoUser
    form_class = MotoUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('profile-detail')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile-edit.html'
    success_url = reverse_lazy('profile-detail')

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'accounts/profile-detail.html'
    context_object_name = 'profile'

    def get_object(self, queryset=None):
        return get_object_or_404(Profile, user=self.request.user)


class MotorcycleCreateView(LoginRequiredMixin, CreateView):
    model = OwnedMotorcycle
    form_class = OwnedMotorcycleForm
    template_name = 'accounts/motorcycle-add.html'
    success_url = reverse_lazy('profile-detail')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class MotorcycleUpdateView(LoginRequiredMixin, UpdateView):
    model = OwnedMotorcycle
    form_class = OwnedMotorcycleForm
    template_name = 'accounts/motorcycle-edit.html'
    success_url = reverse_lazy('profile-detail')

    def get_queryset(self):
        return OwnedMotorcycle.objects.filter(user=self.request.user)


class MotorcycleDeleteView(LoginRequiredMixin, DeleteView):
    model = OwnedMotorcycle
    template_name = 'accounts/motorcycle-delete.html'
    success_url = reverse_lazy('profile-detail')

    def get_queryset(self):
        return OwnedMotorcycle.objects.filter(user=self.request.user)


class FindMyBikeView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/find-my-bike.html'

    def dispatch(self, request, *args, **kwargs):
        # Check if user has a complete profile
        profile = request.user.profile
        if not all([profile.body_type, profile.riding_style, profile.experience]):
            messages.warning(
                request,'Please complete your profile first to get personalized bike recommendations!')
            return redirect('profile-edit')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user.profile
        recommendations = recommend_motorcycles(profile)

        context.update({
            'profile': profile,
            'recommendations': recommendations,
            'get_compatibility_color': get_compatibility_color,
            'has_recommendations': len(recommendations) > 0
        })
        return context


class FindMyClothingView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/find-my-clothing.html'

    def dispatch(self, request, *args, **kwargs):
        # Check if user has a complete profile
        profile = request.user.profile
        if not all([profile.body_type, profile.riding_style]):
            messages.warning(
                request,'Please complete your profile first to get personalized clothing recommendations!')
            return redirect('profile-edit')

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.request.user.profile
        recommendations = recommend_clothing(profile)

        context.update({
            'profile': profile,
            'recommendations': recommendations,
            'get_compatibility_color': get_compatibility_color,
            'has_recommendations': len(recommendations) > 0
        })
        return context
