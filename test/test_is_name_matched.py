from test.util import match_name, fake_name, prep_list
from random import choice, shuffle

BASE_URL = "http://127.0.0.1:8000"
MATCHED_URL = f"{BASE_URL}/is_name_matched"


class TestIsNameMatchedFull:

    def test_is_name_matched_single_buyer_single_owner_match(self, session):
        """
        Single buyer and single owner match.
        """
        name = fake_name()
        json_data = match_name(buyers=prep_list([name]), owners=prep_list([name]))
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is True

    def test_is_name_matched_single_buyer_single_owner_no_match(self, session):
        """
        Single buyer and single owner no match.
        """
        json_data = match_name(buyers=prep_list(["baker steven a"]), owners=prep_list(["lee eric m"]))
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is False

    def test_is_name_matched_multiple_buyers_one_owner_one_match(self, session):
        """
        Multiple buyers and a single owner match.
        """
        buyers = prep_list([fake_name(), fake_name(), fake_name(), fake_name(), fake_name()])
        owners = prep_list([choice(buyers)])
        json_data = match_name(buyers=buyers, owners=owners)
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is True

    def test_is_name_matched_multiple_buyers_single_owner_no_match(self, session):
        """
        Multiple buyers and a single owner on match.
        """
        buyers = prep_list(["Baker Steven A", "Lee Eric M", "Davidson David D", "Stevens Steven"])
        owners = prep_list(["JENNER BRUCE K"])
        json_data = match_name(buyers=buyers, owners=owners)
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is False

    def test_is_name_matched_single_buyer_multiple_owners_one_match(self, session):
        """
        Multiple owners and a single owner match.
        """
        owners = prep_list([fake_name(), fake_name(), fake_name(), fake_name(), fake_name()])
        buyers = prep_list([choice(owners).upper()])
        json_data = match_name(buyers=buyers, owners=owners)
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is True

    def test_is_name_matched_single_buyer_multiple_owners_no_match(self, session):
        """
        Multiple owners and a single buyer no match.
        """
        buyers = prep_list(["BAKER STEVEN A", "LEE ERIC M", "DAVIDSON DAVID D", "STEVENS STEVEN"])
        owners = prep_list(["Jenner Bruce K"])
        json_data = match_name(buyers=buyers, owners=owners)
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is False

    def test_is_name_matched_single_buyer_multiple_owners_multiple_matches(self, session):
        """
        Multiple owners and a single owner with multiple matches.
        """
        owners = prep_list(["Baker Steven A", "Baker Anne", "Baker Edwin C", "Baker Joanne I"])
        buyers = prep_list(["baker allen"])
        json_data = match_name(buyers=buyers, owners=owners)
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is True

    def test_is_name_matched_multiple_buyers_multiple_owners_no_matches(self, session):
        """
        Multiple buyers and multiple owners with no matches.
        """
        buyers = prep_list(["Baker Steven A", "Baker Anne", "Baker Edwin C", "Baker Joanne I"])
        owners = prep_list(["CAMERON JAMES A", "SPEILBERG STEVEN B", "KUBRICK STANLEY J"])
        json_data = match_name(buyers=buyers, owners=owners)
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is False

    def test_is_name_matched_multiple_buyers_multiple_owners_one_match(self, session):
        """
        Multiple buyers and multiple owners one match
        """
        buyers = prep_list(["Baker Steven A", "Baker Anne", "Baker Edwin C", "Baker Joanne I", "Cameron James"])
        owners = prep_list(["CAMERON JAMES A", "SPEILBERG STEVEN B", "KUBRICK STANLEY J"])
        json_data = match_name(buyers=buyers, owners=owners)
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is True

    def test_is_name_matched_multiple_buyers_multiple_owners_multiple_matches(self, session):
        """
        Multiple buyers and multiple owners with multiple matches.
        """
        buyers = prep_list(["Baker Steven A", "Baker Anne", "Baker Edwin C", "Baker Joanne I", "Cameron James"])
        owners = prep_list(["cameron james a", "SPEILBERG STEVEN B", "baker susan"])
        json_data = match_name(buyers=buyers, owners=owners)
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is True

    def test_is_name_matched_one_word_name_match(self, session):
        """
        Single word names with match.
        """
        json_data = match_name(buyers=prep_list(["MCFOOBAR"]), owners=prep_list(["mcfoobar"]))
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is True

    def test_is_name_matched_one_word_name_no_match(self, session):
        """
        Single word names with no match.
        """
        json_data = match_name(buyers=prep_list(["MCFOOBAR"]), owners=prep_list(["mcfubar"]))
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is False

    def test_is_name_matched_matching_first_name_no_match(self, session):
        """
        Matching first names only, no match.
        """
        json_data = match_name(buyers=prep_list(["baker steven"]), owners=prep_list(["stevens steven"]))
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is False

    def test_is_name_matched_short_last_name_match(self, session):
        """
        Short lasts names (2 chars) with a match.
        """
        json_data = match_name(buyers=prep_list(["HO KATE"]), owners=prep_list(["HO BART"]))
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is True

    def test_is_name_matched_short_last_name_no_match(self, session):
        """
        Short last names (2 chars) no match.
        """
        json_data = match_name(buyers=prep_list(["HO KATE"]), owners=prep_list(["HA KATE"]))
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is False

    def test_is_name_matched_ambiguous_first_four_chars_no_match(self, session):
        """
        Ambiguous names. Buyer first and last name 4 chars altogether with a owner last name of the same 4 chars.
        No match.
        """
        json_data = match_name(buyers=prep_list(["HO LA"]), owners=prep_list(["HOLA KATE"]))
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 200
        assert res.json()["IsNameMatched"] is False

    def test_is_name_matched_no_buyers_raises_404(self, session):
        """
        No buyers raises a 404 error with appropriate message.
        """
        json_data = match_name(buyers=[], owners=prep_list([fake_name()]))
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 404
        assert res.json() == dict(detail="Buyer record must contain one or more Buyer.")

    def test_is_name_matched_no_owners_raises_404(self, session):
        """
        No owners raises a 404 error with appropriate message.
        """
        json_data = match_name(buyers=prep_list([fake_name()]), owners=[])
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 404
        assert res.json() == dict(detail="Assess record must contain one or more Owners.")

    def test_is_name_matched_no_owners_and_no_buyers_raises_404(self, session):
        """
        No buyers or owners raises a 404 error with appropriate message.
        """
        json_data = match_name(buyers=[], owners=[])
        res = session.post(MATCHED_URL, data=json_data)
        assert res.status_code == 404
        detail = "Buyer record must contain one or more Buyer.\nAssess record must contain one or more Owners."
        assert res.json() == dict(detail=detail)
