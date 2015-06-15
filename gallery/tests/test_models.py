import os
import datetime
import logging
logger = logging.getLogger(__name__)
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files import File
from gallery.models import Photo, Category
from gallery.tests.utils import IMAGE_PATH
from jessmathews.settings import MEDIA_ROOT

# Create your tests here.


class TestPhotoModel(TestCase):
    def setUp(self):
        user = User.objects.create_user('testuser', 'test@example.com')
        user.save()
        new_image = Photo()
        new_image.title = "Test Photo"
        new_image.image = File(open(IMAGE_PATH + 'jo5bjEB.jpg', 'rb'))
        self.new_image = new_image

    def tearDown(self):
        users = User.objects.all()
        for u in users:
            u.delete()
        photos = Photo.objects.all()
        if len(photos) > 0:
            for p in photos:
                p.delete()

    def test_photo_saves_valid_data(self):
        self.new_image.save()
        self.assertEqual(
            self.new_image.date_created.date(), datetime.datetime.today().date()
        )
        self.assertRegex(self.new_image.slug, r'\w+(-\d+)?')
        self.assertTrue(isinstance(self.new_image.image, File))
        #self.assertEquals(self.new_image.get_absolute_url(), str(self.new_image.id))

    #def test_photo_saves_invalid_data(self):
        #pass

    def test_photo_thumbnails(self):
        self.new_image.save()
        tn = self.new_image.thumbnail
        self.assertEqual(tn.width, 100)
        self.assertEqual(tn.height, 50)

    def test_photo_deletes_from_media_cache(self):
        self.new_image.save()
        self.new_image.delete()
        for _, _, file in os.walk(MEDIA_ROOT):
            [self.assertNotRegex(str(f), r'jo5b.*jpg') for f in file if f]

    def test_photo_new_category(self):
        cat = Category()
        cat.name = "shit"
        cat.save()
        self.new_image.save()
        self.new_image.category.add(cat)


    #def test_bulk_photo_creation(self):
        #new_images = upload_zip_file(ZIP_FILE_PATH)
        #PhotoUploadForm(zip=new_images)
