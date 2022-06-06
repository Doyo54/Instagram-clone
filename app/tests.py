from email.mime import image
from django.test import TestCase
from .models import Profile,InstagramPost,Comment

class testInstagramPost(TestCase):
    def setUp(self):
        self.profile = Profile(name='doyo')
        self.profile.save_profile()

        self.image = InstagramPost(image='default.png')
        self.image.save_image()

        self.image_test = InstagramPost(id=1, title='food', description='this is a test image',user=self.profile,
                                pub_date= 'june 06 2022',image='default.png')

    def test_instance(self):
        self.assertTrue(isinstance(self.image_test, InstagramPost))

    def test_save_image(self):
        after = InstagramPost.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_image(self):
        self.image_test.delete_image()
        images = InstagramPost.objects.all()
        self.assertTrue(len(images) == 0)

    def test_update_image(self):
        self.image_test.update_image(self.image_test.id, 'image/test.jpg')
        changed_img = InstagramPost.objects.filter(image='image/test.jpg')
        self.assertTrue(len(changed_img) == 0)

    def tearDown(self):
        InstagramPost.objects.all().delete()
        Profile.objects.all().delete()


