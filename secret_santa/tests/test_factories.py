from django.test import TestCase

import factory

from secret_santa import factories
from secret_santa.factories import ListFactory, MemberFactory, GiftPairFactory, UserFactory


class ListFactoryTestCase(TestCase):
    def test_factory(self):
        list_factory = ListFactory()
        self.assertIsNotNone(list_factory.list_name)
        self.assertIsNotNone(list_factory.creator)
        self.assertIsNotNone(list_factory.gift_max)

    
class MemberFactoryTestCase(TestCase):
    def test_factory(self):
        member_factory = MemberFactory()

        self.assertIsNotNone(member_factory.member_list)
        self.assertIsNotNone(member_factory.full_name)
        self.assertIsNotNone(member_factory.email)
        self.assertIsNotNone(member_factory.telephone)


class GiftPairFactoryTestCase(TestCase):
    def test_factory(self):
        gift_pair_factory = GiftPairFactory()

        self.assertIsNotNone(gift_pair_factory.gift_pair_original_list)
        self.assertIsNotNone(gift_pair_factory.santa)
        self.assertIsNotNone(gift_pair_factory.gift_receiver)  
