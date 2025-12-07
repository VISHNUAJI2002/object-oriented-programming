/*
Experiment 13

Array of objects

Aim:Program to create a class for Employee having attributes eNo, eName, eSalary.
Read ‘n’ employee information and Search for an employee given eNo, using the
concept of array of Objects.
*/

import java.util.Scanner;

class Employee{
    int eNo,eSalary;
    String eName;
    Employee(int eNo,String eName,int eSalary){
        this.eNo=eNo;
        this.eSalary=eSalary;
        this.eName=eName;
    }
    void display(){
        System.out.println("\n---Employee Details---");
        System.out.println("Employee number: "+eNo);
        System.out.println("Employee name: "+eName);
        System.out.println("Employee salary: "+eSalary);
    }
}

class EmpMain{
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);
        System.out.print("Enter number of emloyees:");
        int n=s.nextInt();

        Employee e[]=new Employee[n];

        for(int j=0;j<n;j++){
            System.out.print("\nEnter employee number: ");
            int no=s.nextInt();
            s.nextLine();
            System.out.print("Enter employee name: ");
            String name=s.nextLine();
            System.out.print("Enter employee salary: ");
            int sal=s.nextInt();

            e[j]=new Employee(no,name,sal);
        }

        int ch;
        do{
            int flag=0;
            System.out.print("\nEnter employee number to search:");
            int search=s.nextInt();

            for (int i=0;i<n;i++){
                if (search==e[i].eNo){
                    flag=1;
                    e[i].display();
                    break;
                }
            }
            if (flag==0) {
                System.out.println("Employee not found.");
            }
            System.out.print("\nDo you want to continue?(1/0):");
            ch=s.nextInt();
        }while(ch!=0);
    }
}

/*
Sample Output:

Enter number of emloyees:2

Enter employee number: 101
Enter employee name: Hari
Enter employee salary: 98000

Enter employee number: 102
Enter employee name: Preyith
Enter employee salary: 85000

Enter employee number to search:104
Employee not found.

Do you want to continue?(1/0):1

Enter employee number to search:102

---Employee Details---
Employee number: 102
Employee name: Preyith
Employee salary: 85000

Do you want to continue?(1/0):0
PS C:\Users\ASUS\Desktop\object-oriented-programming\mca-s2\co2> 
*/