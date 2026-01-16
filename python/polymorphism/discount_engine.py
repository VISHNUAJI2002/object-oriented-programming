"""
Problem Statement:
Design a Python program to calculate final payable amounts using runtime
polymorphism. Create a base class that defines a method for applying discounts.
Different discount strategies such as Seasonal Discount, Membership Discount,
and Coupon Discount should override this method to apply their own discount
logic. The program should accept details for multiple purchases from the user,
store the corresponding discount objects in a single list, and calculate the
final payable amount for each purchase using polymorphism without using
conditional logic for discount calculation.
"""

class Discount:
    def apply_discount(self, amount):
        pass


class SeasonalDiscount(Discount):
    def apply_discount(self, amount):
        return amount - (amount * 0.10)


class MembershipDiscount(Discount):
    def apply_discount(self, amount):
        return amount - (amount * 0.15)


class CouponDiscount(Discount):
    def apply_discount(self, amount):
        return amount - 200


purchases = []

n = int(input("Enter number of purchases: "))

for i in range(n):
    print(f"\nPurchase {i + 1}")
    discount_type = input("Enter discount type (seasonal/membership/coupon): ").lower()
    amount = float(input("Enter purchase amount: "))

    if discount_type == "seasonal":
        purchases.append((SeasonalDiscount(), amount))
    elif discount_type == "membership":
        purchases.append((MembershipDiscount(), amount))
    elif discount_type == "coupon":
        purchases.append((CouponDiscount(), amount))


print("\n--- Final Payable Amounts ---")
i = 1
for discount, amount in purchases:
    print(
        f"Final amount for purchase {i}:",
        discount.apply_discount(amount)
    )
    i += 1


"""
Sample Output:

Enter number of purchases: 3

Purchase 1
Enter discount type (seasonal/membership/coupon): seasonal
Enter purchase amount: 5000

Purchase 2
Enter discount type (seasonal/membership/coupon): membership
Enter purchase amount: 4000

Purchase 3
Enter discount type (seasonal/membership/coupon): coupon
Enter purchase amount: 2500

--- Final Payable Amounts ---
Final amount for purchase 1: 4500.0
Final amount for purchase 2: 3400.0
Final amount for purchase 3: 2300.0
"""
