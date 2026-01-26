"""
Problem Statement:
Design a Python program to perform system audits using abstraction.
Create an abstract base class that defines common audit operations such as
validating data and generating audit results. Different audit types such as
Financial Audit, Security Audit, and Performance Audit should provide their own
implementation for these operations. The program should accept details for
multiple audit requests from the user, store the corresponding audit objects in
a list, and display audit results using abstraction. The abstract class should
define what operations are required, but not how they are implemented.
"""

from abc import ABC, abstractmethod


class Audit(ABC):
    @abstractmethod
    def validate(self, data):
        pass

    @abstractmethod
    def generate_report(self, data):
        pass


class FinancialAudit(Audit):
    def validate(self, data):
        return data >= 0

    def generate_report(self, data):
        return f"Financial Audit Passed | Balance Verified: {data}"


class SecurityAudit(Audit):
    def validate(self, data):
        return data >= 2

    def generate_report(self, data):
        return f"Security Audit Passed | Issues Found: {data}"


class PerformanceAudit(Audit):
    def validate(self, data):
        return data <= 75

    def generate_report(self, data):
        return f"Performance Audit Passed | Load Percentage: {data}"


audits = []
n = int(input("Enter number of audit requests: "))

for i in range(n):
    print(f"\nAudit Request {i + 1}")
    audit_type = input("Enter audit type (financial/security/performance): ").lower()
    value = float(input("Enter audit data value: "))

    if audit_type == "financial":
        audits.append((FinancialAudit(), value))
    elif audit_type == "security":
        audits.append((SecurityAudit(), value))
    elif audit_type == "performance":
        audits.append((PerformanceAudit(), value))


print("\n--- Audit Results ---")
i = 1
for audit, value in audits:
    print(f"\nAudit {i}")
    if audit.validate(value):
        print("Status: Valid")
        print(audit.generate_report(value))
    else:
        print("Status: Invalid")
    i += 1


"""
Sample Output:

Enter number of audit requests: 3

Audit Request 1
Enter audit type (financial/security/performance): financial
Enter audit data value: 50000

Audit Request 2
Enter audit type (financial/security/performance): security
Enter audit data value: 1

Audit Request 3
Enter audit type (financial/security/performance): performance
Enter audit data value: 60

--- Audit Results ---

Audit 1
Status: Valid
Financial Audit Passed | Balance Verified: 50000.0

Audit 2
Status: Invalid

Audit 3
Status: Valid
Performance Audit Passed | Load Percentage: 60.0
"""
