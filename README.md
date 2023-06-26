# Steve Baker - 650 995-3501
# First American Take Home Eval (Senior Software Development Engineer in Test)

I have created [a service using FastAPI](https://github.com/stevebaker01/first_american/blob/main/main.py) based upon the user story and [a suite of 19 tests](https://github.com/stevebaker01/first_american/blob/main/test/test_is_name_matched.py) to run against it.

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
2. I have assumed that the POST body for the is_name_matched endpoint includes a full Buyer record and a full Owner (Assess) record. (see provided json). I have written [a helper function](https://github.com/stevebaker01/first_american/blob/main/test/util.py#L37) to create buyer and assess records with random values.
3. I have assumed that there can be multiple buyers per buyer record because the Buyer field in the buyer record is a list.
4. I have assumed that a single match regardless number of buyers and owners will return *IsNameMatched=True*
5. I have assumed that buyer and owner names can be represented in any case (title, upper or lower). I have written [a helper function](https://github.com/stevebaker01/first_american/blob/main/test/util.py#L12) to randomize the casing and order of elements in buyer and owner lists ensuring all variations ar covered.
6. I have assumed that no buyers and/or no owners will raise a 404 Bad Request error.
7. I have assumed that names will always follow the format "last name [first name [middle initial]]"

All of these assumptions would precipitate questions to the production developer and/or product manager.
My test plan began with several empty test cases with description. As I filled in the test case logic I added others test cases and ended up with [these 19](https://github.com/stevebaker01/first_american/blob/main/test/test_is_name_matched.py).

Thanks,
-Steve Baker
650 995-3501


