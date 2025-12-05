/*
Experiment 15 :
Single Inheritance and Array of Objects

Aim
Create a class ‘Employee’ with data members Empid, Name, Salary, Address and
constructors to initialize the data members. Create another class ‘Teacher’ that inherit
the properties of class employee and contain its own data members Department,
Subjects taught and constructors to initialize these data members and also include
display function to display all the data members. Use array of objects to display details
of N teachers.
*/

import java.util.Scanner;

class Employee{
    int Empid,Salary;
    String Name,Address;

    Employee(int Empid,int Salary,String Name,String Address){
        this.Empid=Empid;
        this.Salary=Salary;
        this.Name=Name;
        this.Address=Address;
    }
}

class Teacher extends Employee{
    String Department,Subjects;
    Teacher(int Empid,int Salary,String Name,String Address,String Department,String Subjects){
        super(Empid,Salary,Name,Address);
        this.Department=Department;
        this.Subjects=Subjects;
    }

    void display(){
        System.out.println("\nEmployee ID: "+Empid);
        System.out.println("Name: "+Name);
        System.out.println("Address: "+Address);
        System.out.println("Department: "+Department);
        System.out.println("Subjects: "+Subjects);
        System.out.println("Salary: "+Salary);
    }
}

class Main{
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);

        System.out.print("Enter number of teachers:");
        int n=s.nextInt();

        Teacher t[]=new Teacher[n];

        for(int i=0;i<n;i++){
            System.out.println("\nEnter details of teacher "+(i+1));

            System.out.print("\nEmployee Id:");
            int id=s.nextInt();
            s.nextLine();
            System.out.print("Name:");
            String name=s.nextLine();
            System.out.print("Address:");
            String address=s.nextLine();
            System.out.print("Department:");
            String dep=s.nextLine();
            System.out.print("Subjects:");
            String sub=s.nextLine();
            System.out.print("Salary:");
            int sal=s.nextInt();

            t[i] =new Teacher(id,sal,name,address,dep,sub);
        }
        System.out.println("\n---Details---");
        for (int j=0;j<n;j++){
            t[j].display();
        }
    }
}

/*
Sample Output:

Enter number of teachers:2

Enter details of teacher 1

Employee Id:101
Name:Sivadas
Address:Muvattupuzha
Department:Computer Application 
Subjects:IPR
Salary:50000

Enter details of teacher 2

Employee Id:201
Name:Minu
Address:Ernakulam
Department:Maths
Subjects:Statistics
Salary:75000

---Details---

Employee ID: 101
Name: Sivadas
Address: Muvattupuzha
Department: Computer Application
Subjects: IPR
Salary: 50000

Employee ID: 201
Name: Minu
Address: Ernakulam
Department: Maths
Subjects: Statistics
Salary: 75000

*/