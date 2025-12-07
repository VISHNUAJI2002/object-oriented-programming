/*
Experiment 9 

Matrix operations

Aim: Read 2 matrices from the console and perform matrix addition and multiplication
using class and object.
*/

import java.util.Scanner;

class Matrix{
    int r1,c1,r2,c2;
    int [][]mat1,mat2,result;
    Matrix(int row1,int col1,int row2,int col2){
        r1=row1;
        c1=col1;
        r2=row2;
        c2=col2;
        mat1=new int[r1][c1];
        mat2=new int[r2][c2];
        result=new int[r1][c2];
    }
    void readMatrix(Scanner s){
        System.out.println("Enter elements of first matrix:");
        for (int i = 0; i < r1; i++){
            for (int j = 0; j < c1; j++){
                mat1[i][j] = s.nextInt();
            } 
        }
        System.out.println("Enter elements of second matrix:");
        for (int i = 0; i < r2; i++) {
            for (int j = 0; j < c2; j++) {
                mat2[i][j] = s.nextInt();
            }
        }
    }
    void add(){
        System.out.println("Resultant Matrix:");
        for (int i=0;i<r1;i++){
            for (int j=0;j<c1;j++){
                System.out.print((mat1[i][j]+mat2[i][j])+" ");
            }
            System.out.println();
        }
    }
    void multiply(){
        System.out.println("Resultant Matrix:");
        for (int i = 0; i < r1; i++) {
            for (int j = 0; j < c2; j++) {
                result[i][j] = 0;
                for (int k = 0; k < c1; k++) {
                    result[i][j] += mat1[i][k] * mat2[k][j];
                }
                System.out.print(result[i][j] + " ");
            }
            System.out.println();
        }
    }
}

class MatrixOperations{
    public static void main (String args[]){
        Scanner s = new Scanner(System.in);

        System.out.println("Enter number of rows and columns for the first matrix:");
        int r1 = s.nextInt();
        int c1 = s.nextInt();
        System.out.println("Enter number of rows and columns for the second matrix:");
        int r2 = s.nextInt();
        int c2 = s.nextInt();

        Matrix obj = new Matrix(r1,c1,r2,c2);
        obj.readMatrix(s);

        System.out.println("1. Addition\n2. Multiplication\n3. Exit");
        while (true) {
            System.out.print("Enter choice: ");
            int choice = s.nextInt();
            switch (choice) {
                case 1:
                    if (r1==r2 && c1==c2){
                        obj.add();
                        break;
                    }
                    else{
                        System.out.println("Dimensions don't match.");
                        break;
                    }    
                case 2:
                    if (c1==r2){
                        obj.multiply();
                        break;
                    }
                    else{
                        System.out.println("Matrix multiplication not possible. Check dimensions of matrices!");
                        break;
                    }    
                case 3:
                    System.out.println("Exiting program.");
                    s.close();
                    return;
            default:
                System.out.println("Invalid choice. Please try again.");
            } 
        }
    }
}        

/*
Sample Output:
PS C:\Users\ASUS\Desktop\object-oriented-programming\mca-s2\co2> java MatrixOperations      
Enter number of rows and columns for the first matrix:
2 2
Enter number of rows and columns for the second matrix:
2 2
Enter elements of first matrix:
1 2
3 4
Enter elements of second matrix:
0 5
5 0
1. Addition
2. Multiplication
3. Exit
Enter choice: 1
Resultant Matrix:
1 7
8 4
Enter choice: 2
Resultant Matrix:
10 5
20 15
Enter choice: 3
Exiting program.
*/