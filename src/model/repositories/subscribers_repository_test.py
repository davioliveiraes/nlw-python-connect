import pytest
from .subscribers_repository import SubscribersRepository

@pytest.mark.skip('Insert in DB')
def test_insert():
   subscriber_info = {
      'name': 'meuNome2',
      'email': 'meuemail2@email.com',
      'evento_id': 3
   }
   subs_repo = SubscribersRepository()
   subs_repo.insert(subscriber_info)

@pytest.mark.skip('Select in DB')
def test_select_subscriber():
    email = 'meuemail2@email.com'
    evento_id = 23

    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, evento_id)
    print(resp)
