import json
from requests import Session
from dataclasses import asdict
from pytest import fixture
from test.util import BuyerRecord, AssessRecord, NameMatch
from faker import Faker

BASE_URL = "https://127.0.0.1:8000"
MATCHED_URL = f"{BASE_URL}/is_name_matched"
MATCHED_FULL_URL = f"{MATCHED_URL}_full"


fake = Faker()


@fixture
def buyer():

    buyer = BuyerRecord(
        Buyer=[fake.name()],
        ChildSeqIDS=[10, 20, 50]
    )
    return buyer


@fixture
def assess():

    assess = AssessRecord(
        Addresses=[fake.address()],
        Owners=[fake.name()]
    )
    return assess


@fixture
def session():

    session = Session()
    session.headers.update(dict(Accept="application/json"))
    return session


class TestIsNameMatchedFull:

    def test_is_name_matched_full_match(self, buyer, assess, session):

        assess.Owners = buyer.Buyer
        name_match = json.dumps(asdict(NameMatch(AssessRecord=assess, BuyerRecord=buyer)))
        res = session.post(MATCHED_FULL_URL, data=name_match, verify=False)
        print(res)


