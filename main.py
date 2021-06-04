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
    with open("res/api-response.json", "r") as resp:
        data = json.load(resp)

        cost = data[model]["saleDetails"]["cost"]
        market_ratio = data[model]["schedule"]["years"][year]["marketRatio"]
        auction_ratio = data[model]["schedule"]["years"][year]["auctionRatio"]

        return {"marketValue": cost * market_ratio,
                "auctionValue": cost * auction_ratio
                }


if __name__ == "__main__":
    print("=====AMAZING BOB'S AUCTION HOUSE=====")
    model = input(f"Enter a model number: ")
    year = input(f"Enter a year: ")

    try:
        values = calc_value(model, year)
        print(f"\nMarket Value : {values['marketValue']:.2f}")
        print(f"Auction Value: {values['auctionValue']:.2f}")
    except KeyError as error:
        print(f"{error} is not a valid entry.")
    finally:
        print("\nThanks for your patronage!!")

