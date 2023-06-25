from pytest import fixture
from requests import Session

@fixture(scope="session")
def session():

    session = Session()
    session.headers.update(dict(Accept="application/json"))
    return session