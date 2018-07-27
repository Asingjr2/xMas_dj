import factory
from factory import fuzzy

from django.contrib.auth.models import User
from base.factories import BaseModelFactory

from .models import List, Member, GiftPair

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user{}'.format(n))
    email = factory.LazyAttribute( lambda obj: '%s@example.org' % obj.username)
    

class ListFactory(BaseModelFactory):
    class Meta:
        model = List

    list_name = factory.fuzzy.FuzzyText(length=255)
    creator = factory.SubFactory(UserFactory)
    gift_max = factory.fuzzy.FuzzyInteger(0,1001)


class MemberFactory(BaseModelFactory):
    class Meta:
        model = Member
        
    member_list = factory.SubFactory(ListFactory)
    full_name = factory.fuzzy.FuzzyText(length=100)
    email = factory.LazyAttribute( lambda obj: '%s@example.org' % obj.full_name)
    telephone = "01234567897"


class GiftPairFactory(BaseModelFactory):
    class Meta:
        model = GiftPair
        
    gift_pair_original_list = factory.SubFactory(ListFactory)
    santa = factory.fuzzy.FuzzyText(length=100)
    gift_receiver = factory.SubFactory(MemberFactory)
