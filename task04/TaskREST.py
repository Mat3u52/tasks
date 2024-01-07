import argparse
from PriceOfGold import PriceOfGold


def main():
    parser = argparse.ArgumentParser(description="NBP API")
    parser.add_argument("-d", "--date", help="format YYYY-MM-DD")
    args = parser.parse_args()

    obj_price_of_gold = PriceOfGold(args.date)

    if obj_price_of_gold.gold_price():
        print("cena zlota:")
        print(obj_price_of_gold.gold_price())
    else:
        print("Error!")


if __name__ == "__main__":
    main()
