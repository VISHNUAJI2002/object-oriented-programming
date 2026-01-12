"""
Problem Statement:
Design a Python program to manage an insurance policy system using inheritance.
Create a base class that stores common policy details such as policy ID and
policy holder name. Derive a class that adds premium-related details. Further,
derive different insurance policy types such as Health Insurance and Vehicle
Insurance that calculate premium amounts differently. The program should accept
details for multiple policies from the user and display the final premium amount
for each policy using inheritance and method overriding.
"""

class Policy:
    def __init__(self, policy_id, holder_name):
        self.policy_id = policy_id
        self.holder_name = holder_name


class PremiumPolicy(Policy):
    def __init__(self, policy_id, holder_name, base_premium):
        super().__init__(policy_id, holder_name)
        self.base_premium = base_premium

    def calculate_premium(self):
        return self.base_premium


class HealthInsurance(PremiumPolicy):
    def __init__(self, policy_id, holder_name, base_premium, age, coverage_amount):
        super().__init__(policy_id, holder_name, base_premium)
        self.age = age
        self.coverage_amount = coverage_amount

    def calculate_premium(self):
        age_factor = 1.2 if self.age > 45 else 1.0
        return self.base_premium * age_factor + (self.coverage_amount * 0.01)


class VehicleInsurance(PremiumPolicy):
    def __init__(self, policy_id, holder_name, base_premium, vehicle_type, vehicle_value):
        super().__init__(policy_id, holder_name, base_premium)
        self.vehicle_type = vehicle_type
        self.vehicle_value = vehicle_value

    def calculate_premium(self):
        type_factor = 1.5 if self.vehicle_type.lower() == "car" else 1.2
        return self.base_premium * type_factor + (self.vehicle_value * 0.02)


policies = []
n = int(input("Enter number of insurance policies: "))

for i in range(n):
    print(f"\nPolicy {i + 1}")
    policy_type = input("Enter policy type (health/vehicle): ").lower()
    policy_id = int(input("Enter policy ID: "))
    holder = input("Enter policy holder name: ")
    base_premium = float(input("Enter base premium: "))

    if policy_type == "health":
        age = int(input("Enter age: "))
        coverage = float(input("Enter coverage amount: "))
        policies.append(
            HealthInsurance(policy_id, holder, base_premium, age, coverage)
        )

    elif policy_type == "vehicle":
        vehicle_type = input("Enter vehicle type (car/bike): ")
        value = float(input("Enter vehicle value: "))
        policies.append(
            VehicleInsurance(policy_id, holder, base_premium, vehicle_type, value)
        )


print("\n--- Insurance Premium Details ---")
for policy in policies:
    print("\nPolicy ID:", policy.policy_id)
    print("Policy Holder:", policy.holder_name)
    print("Final Premium Amount:", policy.calculate_premium())


"""
Sample Output:

Enter number of insurance policies: 2

Policy 1
Enter policy type (health/vehicle): health
Enter policy ID: 701
Enter policy holder name: Anil
Enter base premium: 12000
Enter age: 50
Enter coverage amount: 300000

Policy 2
Enter policy type (health/vehicle): vehicle
Enter policy ID: 702
Enter policy holder name: Meera
Enter base premium: 8000
Enter vehicle type (car/bike): car
Enter vehicle value: 600000

--- Insurance Premium Details ---

Policy ID: 701
Policy Holder: Anil
Final Premium Amount: 15600.0

Policy ID: 702
Policy Holder: Meera
Final Premium Amount: 20000.0
"""
