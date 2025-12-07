/*
Experiment 3

Two-Dimensional Array

Aim
Write a program to read a matrix from the console and check whether it is symmetric or
not.
*/

class Matrix{
    public static void main (String args[]){
        int row =Integer.parseInt(args[0]);
        int col = Integer.parseInt(args[1]);

        int matrix[][]=new int[row][col];

        int index=2;
        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                matrix[i][j]=Integer.parseInt(args[index++]);
            }
        }

        boolean symmetric=true;

        for(int i=0;i<row;i++){
            for(int j=0;j<col;j++){
                if (matrix[i][j]!=matrix[j][i]){
                    symmetric=false;
                    break;
                }
            }
        }

        if (symmetric) System.out.println("Matrix is symmetric.");
        else System.out.println("Matrix is not symmetric."); 
    } 
}       

/*
Sample Output:

PS C:\Users\ASUS\Desktop\object-oriented-programming\mca-s2\co1> java Matrix 3 3 1 0 0 0 1 0 0 0 1
Matrix is symmetric.

*/