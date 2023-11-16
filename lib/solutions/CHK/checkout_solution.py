
# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # empty basket
    if len(skus) == 0: return 0

    # counter for skus
    basket = {item: 0 for item in "ABCDEF"}
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
              "F": {"unit_price": [1, 10]}}

    # get one free deals
    # deal item: [required number of deal item, free item]
    special_deals = {"E": [2, "B"],
                     "F": [3, "F"]}

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
        


