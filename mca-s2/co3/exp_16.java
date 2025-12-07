/*
Experiment 16 

Multilevel Inheritance and Array of Objects

Aim
Create a class ‘Person’ with data members Name, Gender, Address, Age and a
constructor to initialize the data members and another class ‘Employee’ that inherits
the properties of class Person and also contains its own data members like Empid,
Company_name, Qualification, Salary and its own constructor. Create another class
‘Teacher’ that inherits the properties of class Employee and contains its own data
members like Subject, Department, Teacherid and also contain constructors and
methods to display the data members. Use array of objects to display details of N
teachers.
*/

import java.util.Scanner;

class Person{
    String name,gender,address;
    int age;
    
    Person(String name,String gender,String address,int age){
        this.name=name;
        this.gender=gender;
        this.address=address;
        this.age=age;
    }    
}

class Employee extends Person{
    int empid,salary;
    String company_name,qualification;

    Employee(String name,String gender,String address,int age,int id,int sal,String company,String Qualification){
        super(name,gender,address,age);
        empid=id;
        salary=sal;
        company_name=company;
        qualification=Qualification;
    }
}

class Teacher extends Employee{
    int teacherId;
    String department,subject;

    Teacher(String name,String gender,String address,int age,int id,int sal,String company,String Qualification,int tId,String dep,String sub){
        super(name,gender,address,age,id,sal,company,Qualification);
        teacherId=tId;
        department=dep;
        subject=sub;
    }

    void display(){
        System.out.println("Name : "+ name);
        System.out.println("Gender : "+ gender);
        System.out.println("Address : "+ address);
        System.out.println("Age : "+ age);
        System.out.println("Employee Id : "+empid);
        System.out.println("Company Name : "+company_name);
        System.out.println("Qualification : "+qualification);
        System.out.println("Salary : "+salary);
        System.out.println("Teacher Id : "+teacherId);
        System.out.println("Department : "+department);
        System.out.println("Subject : "+subject);
    }
}

class Main{
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);
    
        System.out.print("Enter number of teachers:");
        int n=s.nextInt();
        s.nextLine();

        Teacher t[]=new Teacher[n];

        for(int i=0;i<n;i++){
            System.out.println("Input details of teacher " + (i + 1));

            System.out.println("Enter Name, Gender, Address, Age: ");
            String name = s.nextLine();
            String gndr = s.nextLine();
            String adrs = s.nextLine();
            int age = Integer.parseInt(s.nextLine());

            System.out.println("Enter Employee Id, Company name, Qualification and Salary: ");
            int eid = Integer.parseInt(s.nextLine());
            String comp = s.nextLine();
            String qlfn = s.nextLine();
            int sal = Integer.parseInt(s.nextLine());

            System.out.println("Enter Teacher Id, Department and Subject: ");
            int tid = Integer.parseInt(s.nextLine());
            String dept = s.nextLine();
            String sub = s.nextLine();

            t[i]=new Teacher(name,gndr,adrs,age,eid,sal,comp,qlfn,tid,dept,sub);
        }
        for(int j=0;j<n;j++){
            t[j].display();
        }    
    }
}

/*
Sample Output:

Enter number of teachers:1
Input details of teacher 1
Enter Name, Gender, Address, Age: 
Thanos
Male
Titan
53
Enter Employee Id, Company name, Qualification and Salary: 
200
Snap
pg
95000 
Enter Teacher Id, Department and Subject: 
56
Physics
Nuclear Physics
Name : Thanos
Gender : Male
Address : Titan
Age : 53
Employee Id : 200
Company Name : Snap
Qualification : pg
Salary : 95000
Teacher Id : 56
Department : Physics
Subject : Nuclear Physics
*/