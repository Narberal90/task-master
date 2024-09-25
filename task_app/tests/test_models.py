from django.test import TestCase

from task_app.models import Task, Tag
from django.utils import timezone


class TagModelTest(TestCase):
    def setUp(self):
        self.tag = Tag.objects.create(name="Game")

    def test_create_tag(self):
        """Test that the tag is created successfully"""
        tag = Tag.objects.get(name="Game")
        self.assertEqual(tag.name, "Game")

    def test_tag_str(self):
        """Test the string representation of the Tag model"""
        self.assertEqual(str(self.tag), "Game")


class TaskModelTest(TestCase):
    def setUp(self):
        self.tag1 = Tag.objects.create(name="Home")
        self.tag2 = Tag.objects.create(name="Sport")
        self.task = Task.objects.create(
            content="Exercises at home",
            deadline=timezone.now() + timezone.timedelta(days=2),
            task_is_done=False,
        )
        self.task.tags.add(self.tag1, self.tag2)

    def test_create_task(self):
        """Test that the task is created successfully"""
        task = Task.objects.get(content="Exercises at home")
        self.assertEqual(task.content, "Exercises at home")
        self.assertFalse(task.task_is_done)

    def test_task_str(self):
        self.assertEqual(str(self.task), "Exercises at home")

    def test_task_tags_relationship(self):
        self.assertEqual(self.task.tags.count(), 2)
        self.assertIn(self.tag1, self.task.tags.all())
        self.assertIn(self.tag2, self.task.tags.all())

    def test_task_is_done_default(self):
        self.assertFalse(self.task.task_is_done)

    def test_task_deadline(self):
        """Test that the deadline is correctly set"""
        task = Task.objects.get(content="Exercises at home")
        self.assertIsNotNone(task.deadline)
