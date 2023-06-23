from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()


class BuyerRecord(BaseModel):
    Buyer: List[str]
    DocumentType: str
    Position: int
    Vesting: str
    Borrowers: str
    ChildSeqIDS: List[int]


class AssessRecord(BaseModel):
    ID: str
    Latitude: str
    Addresses: List[str]
    Owners: List[str]


class NameMatch(BaseModel):
    BuyerRecord: BuyerRecord
    AssessRecord: AssessRecord


class IsNameMatched(BaseModel):
    IsNameMatched: bool = False


class IsNameMatchedFull(IsNameMatched):
    Extract: List[str] = []


@app.post("/is_name_matched_full")
async def is_name_matched_full(name_match: NameMatch):
    """
    Attempts to match *full* name of buyer with *full* name of seller
    :param name_match: post body includes a full (json) buyer record and a full (json) seller assess record
    :return: (json)
        {
            Extract: [<up to the first four characters of the matching last name>,]
            IsNameMatched <true if full buyer and seller name match, else false>
        }
    """
    buyers = set(name_match.BuyerRecord.Buyer)
    owners = set(name_match.AssessRecord.Owners)
    if buyers and owners:
        matches = buyers.intersection(owners)
        if matches:
            return IsNameMatchedFull(
                Extract=[match.split()[0][:4].upper() for match in matches],
                IsNameMatched=True
            )
    return IsNameMatchedFull()



@app.post("/is_name_matched")
async def is_name_matched_prefix(name_match: NameMatch):
    """
    Attempts to match up to the first four letters of buyers last name with the first four letters of the sellers last
    name.
    :param name_match: post body includes a full (json) buyer record and a full (json) seller assess record
    :return: (json)
        {
            IsNameMatched <true if (up to) first four letter of a buyers name matches (up to) the first four letters of
            the sellers name>
        }
    """
    buyers = set([buyer.split()[0][:4] for buyer in name_match.BuyerRecord.Buyer])
    owners = set([seller.split()[0][:4] for seller in name_match.AssessRecord.Owners])
    if buyers.intersection(owners):
        return IsNameMatched(IsNameMatched=True)
    return IsNameMatched()
