from django.test import TestCase
from reviews.forms import ReviewCreationForm

# Create your tests here.


class TestReviewCreationForm(TestCase):
    def test_comment_field_is_required(self):
        form = ReviewCreationForm({'comment': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('comment', form.errors.keys())
        self.assertEqual(form.errors['comment'][0], 'This field is required.')

    def test_field_are_explicit_in_form_meta_class(self):
        form = ReviewCreationForm()
        self.assertEqual(form.Meta.fields, ['name', 'comment'])
