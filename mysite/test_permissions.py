# creating and testing permissions and test groups in django tests.
from django.contrib.auth.models import User, Permission, Group
from django.test import TestCase
from django.test import Client


class ExampleGroupPermissionsTests(TestCase):

    def setUp(self):
        #create permissions group
        group_name = "My Test Group"
        self.group = Group(name=group_name)
        self.group.save()
        self.c = Client()
        self.user = User.objects.create_user(username="test", email="test@test.com", password="test")

    def tearDown(self):
        self.user.delete()
        self.group.delete()

    def test_user_cannot_access(self):
        """user NOT in group should not have access
        """
        self.c.login(username='test4', password='test')
        response = self.c.get("/my_view")
        self.assertEqual(response.status_code, 404, u'user in group should have access')
        
        
    def test_user_can_access(self):
        """user in group should have access
        """
        self.user.groups.add(self.group)
        self.user.save()
        self.c.login(username='test', password='test')
        response = self.c.get("/")
        self.assertEqual(response.status_code, 200, u'user in group should have access')