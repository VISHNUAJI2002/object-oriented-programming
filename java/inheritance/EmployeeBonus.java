/*
Problem Statement:
Design a Java program to calculate bonus for different types of employees using inheritance.
Create a base class Employee with common details like employee ID, name, and salary.

Derive Manager, Developer, and Intern classes with additional attributes.

Apply the following conditions:
- Manager: bonus based on number of team members
- Developer: bonus based on number of projects completed
- Intern: fixed bonus amount

Override the method to calculate bonus accordingly. The program should accept
multiple employee details and display the calculated bonus.
*/

import java.util.Scanner;

class Employee {

    protected int empId;
    protected String name;
    protected double salary;

    public Employee(int empId, String name, double salary) {
        this.empId = empId;
        this.name = name;
        this.salary = salary;
    }

    public double calculateBonus() {
        return 0;
    }
}

class Manager extends Employee {

    private int teamSize;

    public Manager(int empId, String name, double salary, int teamSize) {
        super(empId, name, salary);
        this.teamSize = teamSize;
    }

    @Override
    public double calculateBonus() {
        return salary * (0.05 * teamSize);
    }
}

class Developer extends Employee {

    private int projects;

    public Developer(int empId, String name, double salary, int projects) {
        super(empId, name, salary);
        this.projects = projects;
    }

    @Override
    public double calculateBonus() {
        return salary * (0.03 * projects);
    }
}

class Intern extends Employee {

    private double fixedBonus;

    public Intern(int empId, String name, double salary, double fixedBonus) {
        super(empId, name, salary);
        this.fixedBonus = fixedBonus;
    }

    @Override
    public double calculateBonus() {
        return fixedBonus;
    }
}

public class EmployeeBonus {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of employees: ");
        int n = sc.nextInt();
        sc.nextLine();

        Employee[] employees = new Employee[n];

        for (int i = 0; i < n; i++) {

            System.out.println("\nEmployee " + (i + 1));

            System.out.print("Enter type (manager/developer/intern): ");
            String type = sc.nextLine().toLowerCase();

            System.out.print("Enter employee ID: ");
            int id = sc.nextInt();
            sc.nextLine();

            System.out.print("Enter name: ");
            String name = sc.nextLine();

            System.out.print("Enter salary: ");
            double salary = sc.nextDouble();

            if (type.equals("manager")) {
                System.out.print("Enter team size: ");
                int team = sc.nextInt();
                employees[i] = new Manager(id, name, salary, team);

            } else if (type.equals("developer")) {
                System.out.print("Enter number of projects: ");
                int proj = sc.nextInt();
                employees[i] = new Developer(id, name, salary, proj);

            } else if (type.equals("intern")) {
                System.out.print("Enter fixed bonus: ");
                double bonus = sc.nextDouble();
                employees[i] = new Intern(id, name, salary, bonus);

            } else {
                System.out.println("Invalid type");
                i--;
                sc.nextLine();
                continue;
            }

            sc.nextLine();
        }

        System.out.println("\n--- Employee Bonus Details ---");

        for (Employee emp : employees) {
            System.out.println("\nEmployee ID: " + emp.empId);
            System.out.println("Name: " + emp.name);
            System.out.println("Bonus: " + emp.calculateBonus());
        }

        sc.close();
    }
}

/*
Sample Output:

Enter number of employees: 1

Employee 1
Enter type (manager/developer/intern): manager
Enter employee ID: 101
Enter name: Rahul
Enter salary: 50000
Enter team size: 5

--- Employee Bonus Details ---

Employee ID: 101
Name: Rahul
Bonus: 12500.0
*/