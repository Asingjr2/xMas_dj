from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy

import factory
from factory import fuzzy
from uuid import uuid4

from base.factories import BaseModelFactory
from secret_santa import factories
from secret_santa.factories import ListFactory, MemberFactory, GiftPairFactory, UserFactory


class HomeViewTestCase(TestCase):
    def test_200(self):
        user = UserFactory()
        url = reverse('secret_santa:santa_home')
        client = Client()
        client.force_login(user)
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class ListDetailViewTestCase(TestCase):
    def test_200(self):
        list_test = ListFactory()
        url = reverse('secret_santa:list_detail', args=(list_test.id,))
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class ListUpdateViewTestCase(TestCase):
    def test_200(self):
        list_test = ListFactory()
        url = reverse('secret_santa:update_list', args=(list_test.id,))
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class ListDeleteViewTestCase(TestCase):
    def test_200(self):
        list_test = ListFactory()
        url = reverse('secret_santa:delete_list', args=(list_test.id,))
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class GiftPairsViewTestCase(TestCase):
    def test_200(self):
        list_test = ListFactory()
        url = reverse('secret_santa:gift_pairs', args=(list_test.id,))
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class EnterMembersViewTestCase(TestCase):
    def test_200(self):
        url = reverse('secret_santa:enter_members')
        client = Client()
        data = {}
        response = client.get(url, data, follow=True)
        self.assertEqual(response.status_code, 200)


class AddMemberViewTestCase(TestCase):
    def test_200(self):
        list_test = ListFactory()
        url = reverse('secret_santa:add_member', args=(list_test.id,))
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class MemberUpdateViewTestCase(TestCase):
    def test_200(self):
        member_test = MemberFactory()
        url = reverse('secret_santa:update_member', args=(member_test.id,))
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)


class MemberDeleteViewTestCase(TestCase):
    def test_200(self):
        member_test = MemberFactory()
        url = reverse('secret_santa:delete_member', args=(member_test.id,))
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code, 200)
