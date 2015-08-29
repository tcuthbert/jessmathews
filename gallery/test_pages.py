from django.test import TestCase


class TestPages(TestCase):
    def test_homepage(self):
        res = self.client.get("/")
        self.assertEquals(200, res.status_code)

    def test_contactpage(self):
        res = self.client.get("/contact/")
        self.assertEquals(200, res.status_code)
