# Steve Baker - 650 995-3501
# First American Take Home Eval (Senior Software Development Engineer in Test)

I have created a service using FastAPI based upon the user story and a suite of 19 tests to run against it.

* clone repo
  * ssh
    * `git clone git@github.com:stevebaker01/first_american.git`
  * https
    * `git clone https://github.com/stevebaker01/first_american.git`
* `cd first_american`

* set up environment
  * `python3 -m venv venv`
  * `source venv/bin/activate`
  * `pip install -r requirements.txt`
  
* run is_name_matched service
  * `uvicorn main:app --reload`
  * view swagger docs:
    * http://127.0.0.1:8000/docs

* run the tests
  * In a separate shell terminal navigate to the first_american directory.
  * `source venv/bin/activate`
  * `pytest test`

### Questions and Assumptions:
1. The second sentence of the user story is somewhat strange. I have made the assumption that the author meant the following...
> This service *compares* up to the first 4 characters of the last name*(s)* from File A (Buyer) to *up to the first 4 characters of the last name(s) from* File B (Owners).
2. I have assumed that the POST body for the is_name_matched endpoint includes a full Buyer record and a full Owner (Assess) record. (see provided json)
3. I have assumed that there can be multiple buyers per buyer record because the Buyer field in the buyer record is a list.
4. I have assumed that a single match regardless number of buyers and owners will return *IsNameMatched=True*
5. I have assumed that buyer and owner names can be represented in any case (title, upper or lower).
6. I have assumed that no buyers and/or no owners will raise a 404 Bad Request error.

All of these assumptions would precipitate questions to the production developer and/or product manager.


