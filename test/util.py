from faker import Faker
from typing import List
from dataclasses import dataclass
from random import randint, choice


fake = Faker()


@dataclass
class BuyerRecord:
    Buyer: List[str]
    DocumentType: str = "Deed"
    Position: int = randint(1, 999)
    Vesting: str = choice(["yes", "no"])
    Borrowers: str = ""
    ChildSeqIDS: List[int] = None


@dataclass
class AssessRecord:
    ID: str = f"{str(randint(100, 999))}-{str(randint(100, 999))}"
    Latitude: str = str(fake.latitude())
    Addresses: List[str] = None
    Owners: List[str] = None


@dataclass
class NameMatch:
    BuyerRecord: BuyerRecord = AssessRecord()
    AssessRecord: AssessRecord = AssessRecord()