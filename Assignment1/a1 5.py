print("=================================================")
print("                   MY BAZAAR")
print("=================================================")
dicti = {
    0: ["Tshirt", "Apparels", 500],
    1: ["Trousers", "Apparels", 600],
    2: ["Scarf", "Apparels", 250],
    3: ["Smartphone", "Electronics", 20000],
    4: ["iPad", "Electronics", 30000],
    5: ["Laptop", "Electronics", 50000],
    6: ["Eggs", "Eatables", 5],
    7: ["Chocolate", "Eatables", 10],
    8: ["Juice", "Eatables", 100],
    9: ["Milk", "Eatables", 45]
}


def greet():
    print("Hello! Welcome to my grocery store!")


def show_menu():
    '''
    Description: Prints the menu as shown in the PDF

    Parameters: No paramters

    Returns: No return value
    '''

    print("Following are the products available in the shop:")
    print()
    print("-------------------------------------------------")
    print("CODE | DESCRIPTION |   CATEGORY   | COST (Rs)")
    print("-------------------------------------------------")
    print("  0  | Tshirt      | Apparels     | 500")
    print("  1  | Trousers    | Apparels     | 600")
    print("  2  | Scarf       | Apparels     | 250")
    print("  3  | Smartphone  | Electronics  | 20,000")
    print("  4  | iPad        | Electronics  | 30,000")
    print("  5  | Laptop      | Electronics  | 50,000")
    print("  6  | Eggs        | Eatables     | 5")
    print("  7  | Chocolate   | Eatables     | 10")
    print("  8  | Juice       | Eatables     | 100")
    print("  9  | Milk        | Eatables     | 45")


def input_func():
    print("------------------------------------------------")
    print()
    s = str(input("Would you like to buy in bulk? (y or Y / n or N): "))
    if (s == "n" or s == "N" or s == "y" or s == "Y"):
        print("------------------------------------------------")
    else:
        while True:
            if (s == "n" or s == "N" or s == "y" or s == "Y"):
                print("------------------------------------------------")
                break
            else:
                s = str(input("Would you like to buy in bulk? (y or Y / n or N): "))
    print()
    print()

    return s


def get_regular_input():
    '''
    Description: Takes space separated item codes (only integers allowed).
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: No parameters

    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''
    print("ENTER ITEMS YOU WISH TO BUY")
    print("------------------------------------------------")

    k = []
    for i in range(10):
        k.append(0)
    b = input("Enter the item codes (space seperated):")
    b = b.split()

    for i in range(len(b)):
        if int(b[i]) >= 0 and int(b[i]) < 10:
            k[int(b[i])] = k[int(b[i])] + 1
    return k


def get_bulk_input():
    '''
    Description: Takes inputs (only integers allowed) from a bulk buyer.
    For details, refer PDF. Include appropriate print statements to match
    the output with the screenshot provided in the PDF.

    Parameters: No parameters

    Returns: Returns a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.
    '''

    print("ENTER ITEMS YOU WISH TO BUY")
    print("------------------------------------------------")

    j = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    while True:
        q = str(input("Enter code and quantity (leave blank to stop): "))
        q = q.split()
        if(len(q) == 0):
            print("Your order has been finalized.")

            break

        elif(len(q) == 2):

            if(int(q[0]) < 0 or int(q[0]) > 9) and (int(q[1]) < 0):
                print("Invalid code and quantity. Try again.")

            elif(int(q[1]) < 0):
                print("Invalid quantity. Try again.")
            elif(int(q[0]) < 0 or int(q[0]) > 9):
                print("Invalid code. Try again.")
            else:
                item_details = dicti.get(int(q[0]))
                j[int(q[0])] += int(q[1])
                print("You added", int(q[1]), (item_details[0]))
        else:
            print("Please provide correct code and quantity, in order. Try again.")
            continue
    return j


def print_order_details(quantities):
    '''
    Description: Prints the details of the order in a manner similar to the
    sample given in PDF.

    Parameters: Takes a list of integers of length 10, where the i_th
    element represents the quantity of the item with item code i.

    Returns: No return value
    '''

    print("------------------------------------------------")
    print("ORDER DETAILS")
    print("------------------------------------------------")

    ind = 0
    for i in range(len(quantities)):
        if quantities[i] != 0:
            ind = ind + 1

            item_details = dicti.get(i)

            print("[" + str(ind) + "] " + item_details[0] + " x " + str(quantities[i]) + "=" + "Rs" + str(
                item_details[2]) + "*" + str(quantities[i]) + "=" + "Rs" + str(item_details[2] * quantities[i]))


def calculate_category_wise_cost(quantities):
    print("------------------------------------------------")
    print("CATEGORY-WISE COST")
    print("------------------------------------------------")
    appcost = 0
    elecost = 0
    eatcost = 0
    k = 0
    code = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in quantities:
        if (i != 0):
            c = code[k]
            # print("code in loop:",c)
            if (dicti[c][1] == "Apparels"):
                appcost = appcost + dicti[c][2] * i
            if (dicti[c][1] == "Electronics"):
                elecost = elecost + dicti[c][2] * i
            if (dicti[c][1] == "Eatables"):
                eatcost = eatcost + dicti[c][2] * i
        k = k + 1

    tcatcost = (appcost, elecost, eatcost)

    return tcatcost


def get_discount(cost, discount_rate):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - discount_rate: Float: 0 <= discount_rate <= 1

    Returns: The discount on the cost provided.
    '''
    return int(cost * discount_rate)


def calculate_discounted_prices(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the discounted category-wise price, if applicable.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes 3 integer parameters:
    - apparels_cost: 	cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost: 	cost for the category 'Eatables'

    Returns: A 3-tuple of integers in the following format:
    (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost).
    '''
    print("------------------------------------------------")
    print("DISCOUNTS")
    print("------------------------------------------------")
    app_dis, elec_dis, eat_dis = 0, 0, 0

    if apparels_cost > 2000:
        app_dis = get_discount(apparels_cost, 0.1)
        discounted_apparels_cost = apparels_cost - \
            get_discount(apparels_cost, 0.1)
        print("[APPAREL]= Rs", apparels_cost, "-",
              get_discount(apparels_cost, 0.1), "= Rs", discounted_apparels_cost)
    else:
        discounted_apparels_cost = apparels_cost

    if (electronics_cost > 25000):
        elec_dis = get_discount(electronics_cost, 0.1)

        discounted_electronics_cost = electronics_cost - \
            get_discount(electronics_cost, 0.1)
        print("[ELECTRONICS]= Rs", electronics_cost, "-", get_discount(electronics_cost, 0.1), "= Rs",
              discounted_electronics_cost)
    else:
        discounted_electronics_cost = electronics_cost

    if (eatables_cost > 500):
        eat_dis = get_discount(eatables_cost, 0.1)
        discounted_eatables_cost = eatables_cost - \
            get_discount(eatables_cost, 0.1)
        print("[EATABLES]= Rs", eatables_cost, "-",
              get_discount(eatables_cost, 0.1), "= Rs", discounted_eatables_cost)
    else:
        discounted_eatables_cost = eatables_cost

    print("TOTAL DISCOUNT= RS", app_dis + elec_dis + eat_dis)
    print("TOTAL COST= Rs", discounted_apparels_cost +
          discounted_electronics_cost + discounted_eatables_cost)
    return (discounted_apparels_cost, discounted_electronics_cost, discounted_eatables_cost)


def get_tax(cost, tax):
    '''
    Description: This is a helper function. DO NOT CHANGE THIS.
    This function must be used whenever you are calculating discounts.

    Parameters: Takes 2 parameters:
    - cost: Integer
    - tax: 	Float: 0 <= tax <= 1

    Returns: The tax on the cost provided.
    '''
    return int(cost * tax)


def calculate_tax(apparels_cost, electronics_cost, eatables_cost):
    '''
    Description: Calculates the total cost including taxes.
    Include appropriate print statements to match the output with the
    screenshot provided in the PDF.

    Parameters: Takes 3 integer parameters:
    - apparels_cost: 	cost for the category 'Apparels'
    - electronics_cost: cost for the category 'Electronics'
    - eatables_cost: 	cost for the category 'Eatables'

    Returns: A 2-tuple of integers in the following format:
    (total_cost_including_tax, total_tax)
    '''
    print("------------------------------------------------")
    print("TAX")
    print("------------------------------------------------")
    if (apparels_cost > 0):
        print("[APPAREL]= Rs", apparels_cost, "*0.10",
              "= Rs", get_tax(apparels_cost, 0.1))
    if (electronics_cost > 0):
        print("[ELECTRONICS]= Rs", electronics_cost, "*0.15",
              "= Rs", get_tax(electronics_cost, 0.15))
    if (eatables_cost > 0):
        print("[EATABLES]= Rs", eatables_cost, "*0.05",
              "= Rs", get_tax(eatables_cost, 0.05))
    total_tax = get_tax(apparels_cost, 0.1) + \
        get_tax(electronics_cost, 0.15) + \
        get_tax(eatables_cost, 0.05)
    total_cost_including_tax = apparels_cost + \
        electronics_cost + eatables_cost + total_tax
    print("TOTAL TAX = Rs", total_tax)
    print("TOTAL COST= Rs", total_cost_including_tax)
    return (total_cost_including_tax, total_tax)


def apply_coupon_code(total_cost):
    '''
        Description: Takes the coupon code from the user as input (case-sensitive).
        For details, refer the PDF. Include appropriate print statements to match
        the output with the screenshot provided in the PDF.

        Parameters: The total cost (integer) on which the coupon is to be applied.

        Returns: A 2-tuple of integers:
        (total_cost_after_coupon_discount, total_coupon_discount)
        '''

    print("------------------------------------------------")
    print("COUPON CODE")
    print("------------------------------------------------")
    total_cost_including_tax = total_cost
    while True:

        x = str(input("Enter coupon code (else leave blank)"))

        if x == "HELLE25":
            if(total_cost_including_tax >= 25000):
                discount = 0.25*total_cost_including_tax
                if discount >= 5000:
                    total_coupon_discount = min(5000, discount)
                    total_cost_after_coupon_discount = total_cost_including_tax - \
                        min(5000, discount)
                    print("[HELLE25] min(5000,", "Rs",
                          total_cost_including_tax, "*0.25) =", "Rs 5000")
                else:
                    total_coupon_discount = discount
                    total_cost_after_coupon_discount = (
                        0.75)*total_cost_including_tax
                    print("[HELLE25] min(5000,", "Rs", total_cost_including_tax,
                          "*0.25) =", "Rs", total_coupon_discount)
                break
            else:
                print("Sorry. Code valid only for purchases more than Rs 25000")

        elif(x == "CHILL50"):
            if(total_cost_including_tax >= 50000):
                discount = 0.50*total_cost_including_tax
                if discount >= 10000:
                    total_coupon_discount = min(10000, discount)
                    total_cost_after_coupon_discount = total_cost_including_tax - \
                        min(10000, discount)
                    print("[CHILL50] min(10000,", "Rs",
                          total_cost_including_tax, "*0.50) =", "Rs 10000")
                else:
                    total_coupon_discount = discount
                    total_cost_after_coupon_discount = (
                        0.50)*total_cost_including_tax
                    print("[CHILL50] min(5000,", "Rs", total_cost_including_tax,
                          "*0.50)  =", "Rs", total_coupon_discount)

                break

            else:
                print("Sorry. Code valid only for purchases more than Rs 50000")

        elif not len(x):
            print("No coupon code applied")
            total_cost_after_coupon_discount = total_cost
            total_coupon_discount = 0
            break

        else:
            print("Invalid coupon code. Try again. ")
            continue

    return (total_cost_after_coupon_discount, total_coupon_discount)


def main():
    greet()
    show_menu()

    s = input_func()

    if (s == "N" or s == "n"):
        k = get_regular_input()

        print(k)
    else:
        k = get_bulk_input()

    print_order_details(k)

    t1 = calculate_category_wise_cost(k)
    if (t1[0] > 0):
        print("Apparels= Rs", t1[0])
    if (t1[1] > 0):
        print("Electronics= Rs", t1[1])
    if (t1[2] > 0):
        print("Eatables= Rs", t1[2])

    m = calculate_discounted_prices(t1[0], t1[1], t1[2])

    p = calculate_tax(m[0], m[1], m[2])

    b = apply_coupon_code(p[0])

    print("TOTAL COUPON DISCOUNT = Rs", b[1])
    print("TOTAL COST = Rs", b[0])
    print()
    print("Thank you for visiting!")


if __name__ == '__main__':
    main()
