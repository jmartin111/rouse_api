from unittest import TestCase
import rouse_api


class TestRouseApi(TestCase):

    control_data = {
        "valid": {
            "id": "67352",
            "year": "2007"
        },
        "invalid": {
            "id": "87964",
            "year": "2011"
        }
    }

    def test_calculate_valid_values(self):
        values = rouse_api.calculate_values(self.control_data["valid"]["id"],
                                            self.control_data["valid"]["year"])

        assert round(values["marketValue"], 2) == 216384.71
        assert round(values["auctionValue"], 2) == 126089.53

    def test_calculate_invalid_values(self):
        self.setUp()
        self.assertRaises(KeyError,
                          rouse_api.calculate_values,
                          self.control_data["invalid"]["id"],
                          self.control_data["invalid"]["year"]
                          )
