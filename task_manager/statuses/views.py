from django.shortcuts import redirect
from task_manager.utils import ListView
from task_manager.statuses.models import Status
from task_manager.utils import error_flash
from django.db.models.deletion import ProtectedError
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy


class StatusesIndexView(ListView):
    model = Status
    fields = ['id', 'name', 'created_at']


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = 'common/create.html'
    success_message = _('Status created successfully')
    success_url = reverse_lazy('status_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = _(f'Create status')
        return context


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'common/update.html'
    success_message = _('The status was updated')
    success_url = reverse_lazy('status_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = _(f'Edit status')
        return context


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'common/delete.html'
    success_message = _('The status was deleted')
    success_url = reverse_lazy('status_index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = _(f'Delete status')
        return context

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            error_flash(request, 'Assigned status cannot be deleted')
            return redirect('status_index')
