from django.test import TestCase
from django.contrib.auth import get_user_model
from gallery.models import Photo, Category
from django.core.urlresolvers import reverse
from django.core.files import File
import logging
logging.basicConfig(level=logging.INFO)

# Create your tests here.
class TestPhotoAdmin(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user('admin', 'testie@test.com', 'test')
        self.user.is_staff = True
        self.user.is_superuser = True
        self.user.save()

    def test_single_image_upload(self):
        cat = Category.objects.create(name="testcat")
        with File(open("/Users/tom/Code/python/jessmathews/gallery/tests/files/jo5bjEB.jpg", "rb")) as f:
            data = {"title": "test",
                    "category": (cat.id,),
                    "image": f
                    }
            self.client.login(username="admin", password="test")
            response = self.client.post(reverse("admin:gallery_photo_add"), data, follow=True)
            self.assertEquals(response.status_code, 200)

    def test_zip_file_upload(self):
        pass
    def test_single_bad_image_upload(self):
        pass
    def test_bad_zip_file_upload(self):
        pass
