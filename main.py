from fastapi import FastAPI, HTTPException
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


@app.post("/is_name_matched")
async def is_name_matched(name_match: NameMatch):
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
    buyers = set([buyer.split()[0][:4].lower() for buyer in name_match.BuyerRecord.Buyer])
    owners = set([seller.split()[0][:4].lower() for seller in name_match.AssessRecord.Owners])

    errors =[]
    if not buyers:
        errors.append("Buyer record must contain one or more Buyer.")
    if not owners:
        errors.append("Assess record must contain one or more Owners.")
    if errors:
        errors = "\n".join(errors)
        raise HTTPException(status_code=404, detail=errors)

    if buyers.intersection(owners):
        return IsNameMatched(IsNameMatched=True)
    return IsNameMatched()
