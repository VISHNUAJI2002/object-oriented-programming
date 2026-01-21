"""
Problem Statement:
Design a Python program to manage hospital billing details using encapsulation.
Each patient should have private attributes such as patient ID, patient name,
room charges, treatment charges, medicine charges, and insurance coverage
percentage. Direct access to these attributes must be restricted. Provide
controlled access using getter methods and setter methods where necessary.
The program should calculate the final payable bill amount internally after
applying insurance coverage. The program should accept details for multiple
patients from the user and display patient ID, patient name, and final bill
amount.
"""

class HospitalBill:
    def __init__(self, patient_id, name, room_charges, treatment_charges, medicine_charges):
        self.__patient_id = patient_id
        self.__name = name
        self.__room_charges = room_charges
        self.__treatment_charges = treatment_charges
        self.__medicine_charges = medicine_charges
        self.__insurance_coverage = 0.0   

    def get_patient_id(self):
        return self.__patient_id

    def get_patient_name(self):
        return self.__name

    def set_insurance_coverage(self, percentage):
        if 0 <= percentage <= 100:
            self.__insurance_coverage = percentage

    def calculate_total_bill(self):
        return self.__room_charges + self.__treatment_charges + self.__medicine_charges

    def calculate_final_bill(self):
        total = self.calculate_total_bill()
        discount = total * (self.__insurance_coverage / 100)
        return total - discount


patients = []
n = int(input("Enter number of patients: "))

for i in range(n):
    print(f"\nPatient {i + 1}")
    pid = int(input("Enter patient ID: "))
    name = input("Enter patient name: ")
    room = float(input("Enter room charges: "))
    treatment = float(input("Enter treatment charges: "))
    medicine = float(input("Enter medicine charges: "))
    insurance = float(input("Enter insurance coverage percentage: "))

    bill = HospitalBill(pid, name, room, treatment, medicine)
    bill.set_insurance_coverage(insurance)

    patients.append(bill)


print("\n--- Hospital Billing Details ---")
for patient in patients:
    print("\nPatient ID:", patient.get_patient_id())
    print("Patient Name:", patient.get_patient_name())
    print("Final Bill Amount:", patient.calculate_final_bill())


'''
Sample Output:

Enter number of patients: 2

Patient 1
Enter patient ID: 901
Enter patient name: Arjun
Enter room charges: 15000
Enter treatment charges: 28000
Enter medicine charges: 7000
Enter insurance coverage percentage: 20

Patient 2
Enter patient ID: 902
Enter patient name: Neha
Enter room charges: 12000
Enter treatment charges: 20000
Enter medicine charges: 5000
Enter insurance coverage percentage: 10

--- Hospital Billing Details ---

Patient ID: 901
Patient Name: Arjun
Final Bill Amount: 40000.0

Patient ID: 902
Patient Name: Neha
Final Bill Amount: 33300.0
'''
