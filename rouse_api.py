#! rouse_api/bin/python3.8
import json


def calc_value(eq_model, eq_year):
    """
    Take the model id and year, and returns an object
    containing the calculated values (Market and Auction).

    :param: eq_model: equipment model
    :param: eq_year: equipment year
    :return: object: market and auction values
    """
    with open("res/api-response.json", "r") as resp:
        data = json.load(resp)

        # TODO: this notation is clunky; fix it
        cost = data[eq_model]["saleDetails"]["cost"]
        market_ratio = data[eq_model]["schedule"]["years"][eq_year]["marketRatio"]
        auction_ratio = data[eq_model]["schedule"]["years"][eq_year]["auctionRatio"]

        return {"marketValue": cost * market_ratio,
                "auctionValue": cost * auction_ratio
                }


if __name__ == "__main__":
    """ Main function """
    
    print("=====AMAZING BOB'S AUCTION HOUSE=====")
    model = input(f"Enter a model number: ")
    year = input(f"Enter a year: ")

    try:
        values = calc_value(model, year)
        print(f"\nMarket Value : ${values['marketValue']:,.2f}")
        print(f"Auction Value: ${values['auctionValue']:,.2f}")
    except KeyError as error:
        print(f"{error} is not a valid entry.")
    finally:
        print("\nThanks for your patronage!!")
