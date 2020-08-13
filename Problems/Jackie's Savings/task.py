def final_deposit_amount(amount=1000, *interest):
    for i in interest:
        amount *= (int(i)/100 + 1)
        amount = round(amount, 2)
    return amount
