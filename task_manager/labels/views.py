from django.shortcuts import redirect
from task_manager.utils import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from task_manager.labels.models import Label
from task_manager.utils import LoginRequiredMixin
from django.utils.translation import gettext_lazy as _
from task_manager.utils import error_flash
from django.db.models.deletion import ProtectedError


class LabelsIndexView(ListView):
    model = Label
    fields = ['id', 'name', 'created_at']


class LabelDeleteView(DeleteView):
    model = Label

    def dispatch(self, request, *args, **kwargs):
        try:
            return super().dispatch(request, *args, **kwargs)
        except ProtectedError:
            error_flash(request, 'Assigned label cannot be deleted')
            return redirect('labels_index')


class LabelCreateView(CreateView):
    model = Label
    fields = ['name']


class LabelUpdateView(UpdateView):
    model = Label
    fields = ['name']
