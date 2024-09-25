from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from .forms import TaskForm
from .models import Tag, Task


class TaskListView(generic.ListView):
    model = Task
    template_name = "task_master/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return (
            Task.objects
            .prefetch_related("tags")
            .order_by("task_is_done", "-datetime"))


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    template_name = "task_master/task_form.html"
    success_url = reverse_lazy("task_app:task-list")

    def form_valid(self, form):
        return super().form_valid(form)


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "task_master/task_form.html"
    success_url = reverse_lazy("task_app:task-list")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "task_master/task_confirm_delete.html"
    success_url = reverse_lazy("task_app:task-list")


def toggle_task_status(request: HttpRequest, pk) -> HttpResponse:
    task = get_object_or_404(Task, pk=pk)
    task.task_is_done = not task.task_is_done
    task.save()
    return redirect("task_app:task-list")


class TagListView(generic.ListView):
    model = Tag
    template_name = "task_master/tag_list.html"
    context_object_name = "tags"


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    template_name = "task_master/tag_form.html"
    success_url = reverse_lazy("task_app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ["name"]
    template_name = "task_master/tag_form.html"
    success_url = reverse_lazy("task_app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "task_master/tag_confirm_delete.html"
    success_url = reverse_lazy("task_app:tag-list")
