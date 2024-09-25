from django.urls import path

from .views import (
    TaskDeleteView,
    TaskUpdateView,
    TaskCreateView,
    TaskListView,
    toggle_task_status,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("add/", TaskCreateView.as_view(), name="task-add"),
    path("update/<int:pk>/", TaskUpdateView.as_view(), name="task-update"),
    path("delete/<int:pk>/", TaskDeleteView.as_view(), name="task-delete"),
    path(
        "toggle-status/<int:pk>/",
        toggle_task_status,
        name="task-toggle-status"
    ),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/add/", TagCreateView.as_view(), name="tag-add"),
    path("tags/update/<int:pk>/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/delete/<int:pk>/", TagDeleteView.as_view(), name="tag-delete"),
]

app_name = "task_app"
