from django.test import TestCase
from django.db.utils import IntegrityError
from Course.models import Course


class CourseModelTest(TestCase):
    def test_create_course(self):
        course = Course.objects.create(
            title="Test"
        )
        self.assertEqual(course.title, "Test")
        self.assertEqual(course.description, "")

    def test_create_course_double_title_fail(self):
        Course.objects.create(
            title="Test"
        )
        with self.assertRaises(IntegrityError):
            Course.objects.create(
                title="Test"
            )
