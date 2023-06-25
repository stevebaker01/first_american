import json
from faker import Faker
from typing import List
from random import randint, choice, shuffle
from string import ascii_uppercase



fake = Faker()


def prep_list(lst):
    """
    Randomizes the case of strings in a list (upper, lower, title), shuffles and returns list.
    :param lst: List of strings to randomize case and shuffle.
    :return: List of strings with random casing and shuffled order.
    """

    for i in range(len(lst)):
        case = choice(["lower", "upper", "title"])
        if case == "lower":
            lst[i] = lst[i].lower()
        elif case == "upper":
            lst[i] = lst[i].upper()
        else:
            lst[i] = lst[i].title()
        shuffle(lst)
        return lst


def fake_name():
    name = f"{fake.last_name()} {fake.first_name()}"
    name += choice([f" {choice(ascii_uppercase)}", ""])
    return name


def match_name(buyers: List[str], owners: List[str]) -> str:

    records = dict(
        BuyerRecord=dict(
            Buyer=buyers,
            DocumentType="Deed",
            Position=randint(1, 999),
            Vesting=choice(["yes", "no", ""]),
            Borrowers="",
            ChildSeqIDS=[randint(1, 999) for _ in range(randint(1, 5))]
        ),
        AssessRecord=dict(
            ID=f"{str(randint(100, 999))}-{str(randint(100, 999))}",
            Latitude=float(fake.latitude()),
            Addresses=[fake.address()],
            Owners=owners,
        )
    )
    return json.dumps(records)
