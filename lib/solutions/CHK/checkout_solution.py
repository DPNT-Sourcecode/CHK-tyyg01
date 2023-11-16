
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # empty basket
    if len(skus) == 0: return 0

    # counter for skus
    basket = {item: 0 for item in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"}
    for item in skus:
        # illegal input
        if item not in basket:
            return -1
        else:
            basket[item] += 1

    # storage of items and prices/deals
    # deals ordered best to worst
    prices = {"A": {"deal1": [5, 200], "deal2": [3, 130], "unit_price": [1, 50]},
              "B": {"deal1": [2, 45], "unit_price": [1, 30]},
              "C": {"unit_price": [1, 20]},
              "D": {"unit_price": [1, 15]},
              "E": {"unit_price": [1, 40]},
              "F": {"unit_price": [1, 10]},
              "G": {"unit_price": [1, 20]},
              "H": {"deal1": [10, 80], "deal2": [5, 45], "unit_price": [1, 10]},
              "I": {"unit_price": [1, 35]},
              "J": {"unit_price": [1, 60]},
              "K": {"deal1": [2, 150], "unit_price": [1, 80]},
              "L": {"unit_price": [1, 90]},
              "M": {"unit_price": [1, 15]},
              "N": {"unit_price": [1, 40]},
              "O": {"unit_price": [1, 10]},
              "P": {"deal1": [5, 200], "unit_price": [1, 50]},
              "Q": {"deal1": [3, 80], "unit_price": [1, 30]},
              "R": {"unit_price": [1, 50]},
              "S": {"unit_price": [1, 30]},
              "T": {"unit_price": [1, 20]},
              "U": {"unit_price": [1, 40]},
              "V": {"deal1": [3, 130], "deal2": [2, 90], "unit_price": [1, 50]},
              "W": {"unit_price": [1, 20]},
              "X": {"unit_price": [1, 90]},
              "Y": {"unit_price": [1, 10]},
              "Z": {"unit_price": [1, 50]}}

    # get one free deals
    # deal item: [required number of deal item, free item]
    special_deals = {"E": [2, "B"],
                     "F": [3, "F"],
                     "N": [3, "M"],
                     "R": [3, "Q"],
                     "U": [4, "U"]}

    # update basket
    basket = update_special_deals(basket, special_deals)

    price = get_price_total(basket, prices)
    return price


def update_special_deals(basket, special_deals):
    for item in special_deals:
        deal_quant, deal_item = special_deals[item]
        basket_quant = basket[item]

        # subtract the number of free items if deal is valid
        if basket_quant // deal_quant > 0:
            basket[deal_item] -= (basket_quant // deal_quant)
            if basket[deal_item] < 0:
                basket[deal_item] = 0
    return basket


def get_price_total(basket, prices):
    price = 0 
    for item in basket:
        for deal_quant, deal_price in prices[item].values():
            basket_quant = basket[item]
            price += (basket_quant // deal_quant) * deal_price

            # update price in basket
            basket[item] = basket_quant % deal_quant

    return price
        
