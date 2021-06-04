#! /usr/bin/python3.8

import json


def calc_value(model, year):
    """
    Take the model id and year, and returns an object
    containing the calculated values (Market and Auction).

    :param: model: equipment model
    :param: year: model year
    :return: object: market and auction values
    """


if __name__ == "__main__":
    with open("res/api-response.json", "r") as resp:
        data = json.load(resp)
