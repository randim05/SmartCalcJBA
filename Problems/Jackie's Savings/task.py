def final_deposit_amount(*interest, amount=1000):
    try:
        for i in interest:
            amount *= (int(i)/100 + 1)
            # amount = round(amount, 2)
        return round(amount, 2)
    except:
        return amount
