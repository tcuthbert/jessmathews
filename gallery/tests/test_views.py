from django.test import TestCase
from gallery.models import Photo

# Create your tests here.


class TestHomePageView(TestCase):
    def test_homepage_no_photos(self):
        """
        Test that homepage renders message that no photos exist to be rendered
        """
        response = self.client.get('/')
        self.assertContains(response,
                            text="No images uploaded...",
                            status_code=200
                            )

        def test_homepage_with_photos(self):
            pass
