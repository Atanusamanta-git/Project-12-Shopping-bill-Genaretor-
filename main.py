def schooping_bill():
    print("-------Welcome Billing App------")
    total=0
    while (True):

        product=input("Enter Your Product name or (type 'done' for finished): ")
        if product.lower()=="done":
            break
        price=int(input("Enter Product Price($): Rs- "))
        quantity=int(input("Enter Product Quantity: "))

        item_total=price*quantity
        total=total+item_total
    print("\n========Shooping Bill========")
    print("Product     Qty    Price")
    print(f"\n {product}       {quantity}     {price}")
    print("----------------------------------------")
    print(f"\nTotal Bill:          {total}")
schooping_bill()