import email
from django.test import TestCase,Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTest(TestCase):

    def setUp(self):
       self.client=Client()
       self.admin_user=get_user_model().objects.create_superuser(
           email = 'asingh@gmail.com',
           password = 'pas123'
       )
       self.client.force_login(self.admin_user)
       self.user=get_user_model().objects.create_user(
           email = 'test@gmail.com',
           password = 'pas1234',
           name = 'aarya'
       )

    def test_user_listed(self):
        """test that user are listed in user page"""

        url=reverse('admin:core_user_changelist')
        res=self.client.get(url)

        self.assertContains(res,self.user.name)
        self.assertContains(res,self.user.email)

    def test_user_change_page(self):
        """Test that user edit page should work"""
        url=reverse('admin:core_user_change',args=[self.user.id])
        res=self.client.get(url)
        self.assertEqual(res.status_code,200)

    def test_create_user_page(self):
        """create user page should work"""
        url=reverse('admin:core_user_add')
        res=self.client.get(url)
        self.assertEqual(res.status_code,200)

