"""
Problem Statement:
Design a Python program to demonstrate abstraction using a report export system.
Create an abstract base class that defines a common interface for exporting reports.
Different report formats such as PDF, CSV, and JSON should provide their own
implementation for exporting data. The program should accept details for multiple
reports from the user, store the corresponding exporter objects in a list, and
export each report using abstraction. The abstract class should define what an
export operation is, but not how it is performed.
"""

from abc import ABC, abstractmethod

class ReportExporter(ABC):
    @abstractmethod
    def export(self,title,data):
        pass

class PDFReportExporter(ReportExporter):
    def export(self,title,data):
        return f"PDF report '{title}' exported with {len(data)} records"

class CSVReportExporter(ReportExporter):
    def export(self,title,data):
        return f"CSV report '{title}' exported with {len(data)} rows"

class JSONReportExporter(ReportExporter):
    def export(self,title,data):
        return f"JSON report '{title} exported with {len(data)} objects"


reports=[]
n=int(input("Enter number of reports: "))

for i in range(n):
    print(f"\nReport {i+1}")
    report_type=input("Enter report format (pdf,csv,json): ").lower()
    title=input("Enter report title: ")
    count=int(input("Enter number of data records:"))

    data=[]
    print("Enter data:\n")
    for _ in range(count):
        data.append(input())

    if report_type == "pdf":
        reports.append((PDFReportExporter(),title,data))
    elif report_type == "csv":
        reports.append((CSVReportExporter(), title, data))
    elif report_type == "json":
        reports.append((JSONReportExporter(), title, data))            

print("\n--- Report Export Status ---")
for exporterObject,title,data in reports:
    print(exporterObject.export(title,data))

'''
Sample Output:

Enter number of reports: 2

Report 1
Enter report format (pdf,csv,json): pdf 
Enter report title: Sales Summary
Enter number of data records:3
Enter data:

item1
item2
item3

Report 2
Enter report format (pdf,csv,json): json
Enter report title: User Activity
Enter number of data records:2
Enter data:

Login
Logout

--- Report Export Status ---
PDF report 'Sales Summary' exported with 3 records
JSON report 'User Activity exported with 2 objects
'''    