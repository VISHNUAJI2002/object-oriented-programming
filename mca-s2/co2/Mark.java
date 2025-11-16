/*
Experiment 7 :

Initialize instance variables using class and method

Aim:
Program to demonstrate use of command line arguments to initialize values to
member variables in a class and to display them.

Hint:- Create a class containing Rlno, stud_name, engmark, mathsmark, totalmark.
While executing the program we have to pass arguments through command line.
These values are obtained in an array which is passed as argument to main function,
here it is args[ ]. The marks are converted correspondingly and then passed to
constructor where values are stored to class variables. Find the total marks and later
displayed using display function.
*/

class Students{
    int roll_no,engmark,mathsmark,totalmark;
    String stud_name;
    Students(int r, int eng,int m,String s){
        roll_no=r;
        engmark=eng;
        mathsmark=m;
        stud_name=s;
    }
    void display(){
        totalmark=engmark+mathsmark;
        System.out.println("Name:"+stud_name);
        System.out.println("Roll_no:"+roll_no);
        System.out.println("English Mark:"+engmark);
        System.out.println("Maths Mark:"+mathsmark);
        System.out.println("TotalMark:"+totalmark);
    }
}
class Mark{
    public static void main(String args[]){
        int r=Integer.parseInt(args[0]);
        String s =args[1];
        int eng=Integer.parseInt(args[2]);
        int m=Integer.parseInt(args[3]);
        Students s1=new Students(r,eng,m,s);
        s1.display();
    }
}

/*
Sample Output:

PS C:\Users\ASUS\Desktop\object-oriented-programming\mca-s2\co2> java Mark.java 10 Vishnu 87 91
Name:Vishnu
Roll_no:10
English Mark:87
Maths Mark:91
TotalMark:178
*/