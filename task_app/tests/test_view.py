from django.test import TestCase
from django.urls import reverse
from task_app.models import Task, Tag


class TaskListViewTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(
            name="Test Tag"
        )
        self.task1 = Task.objects.create(
            content="Test Task 1",
            task_is_done=False
        )
        self.task2 = Task.objects.create(
            content="Test Task 2",
            task_is_done=True
        )
        self.task1.tags.add(self.tag)

    def test_task_list_view(self):
        """Test if task list view works correctly"""
        response = self.client.get(reverse("task_app:task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response,
            "task_master/task_list.html"
        )
        self.assertContains(response, "Test Task 1")
        self.assertContains(response, "Test Task 2")


class TaskCreateViewTest(TestCase):
    def test_create_task_view(self):
        """Test the task creation view"""
        response = self.client.post(
            reverse("task_app:task-add"),
            {
                "content": "New Task",
                "deadline": "2024-12-31 12:00",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.first().content, "New Task")


class TaskUpdateViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            content="Update Task Test",
            task_is_done=False
        )

    def test_update_task_view(self):
        """Test the task update view"""
        response = self.client.post(
            reverse(
                "task_app:task-update",
                args=[self.task.id]
            ),
            {
                "content": "Updated Task",
                "deadline": "2024-12-31 12:00",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.task.refresh_from_db()
        self.assertEqual(self.task.content, "Updated Task")


class TaskDeleteViewTest(TestCase):
    def setUp(self):
        self.task = Task.objects.create(
            content="Delete Task Test",
            task_is_done=False
        )

    def test_delete_task_view(self):
        """Test the task delete view"""
        response = self.client.post(
            reverse(
                "task_app:task-delete",
                args=[self.task.id]
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 0)
