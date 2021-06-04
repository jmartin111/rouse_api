#! rouse_api/bin/python3.8
import json


def calc_value(model, year):
    """
    Take the model id and year, and returns an object
    containing the calculated values (Market and Auction).

    :param: model: equipment model
    :param: year: model year
    :return: object: market and auction values
    """
    pass


if __name__ == "__main__":
    with open("res/api-response.json", "r") as resp:
        data = json.load(resp)

        # scan through and grab valid models
        valid_models = [y for y in data]
        model = input(f"Enter a model number e.g. {valid_models[0]}: ")

        # now get the valid years
        valid_years = [y for y in data[model]["schedule"]["years"]]
        year = input(f"Enter a year e.g. {valid_years[0]}: ")

        try:
            calc_value(data[model], data[model]["schedule"][year])
        except KeyError as error:
            print(f"{error} is not a valid entry.")
