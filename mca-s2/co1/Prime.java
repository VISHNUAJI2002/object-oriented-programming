/*
Basic Java Programs

Aim:
Print prime numbers upto a limit.
 */

class Prime{
    public static void main(String args[]){
        int n=Integer.parseInt(args[0]);
        if (n<=1) System.out.println("None");
        else{
            System.out.println("The prime numbers upto "+n+" are:");
            for (int i=2;i<=n;i++){
                int flag=1;
                for (int j=2;j*j<=i;j++){
                    if(i%j==0){
                        flag=0;
                        break;
                    }
                }
            if (flag==1){
                System.out.print(i+" ");
            }    
            }
        }
    }
}

/*
Sample Output:

PS C:\Users\ASUS\Desktop\object-oriented-programming\mca-s2\co1> java Prime 20   
The prime numbers upto 20 are:
2 3 5 7 11 13 17 19 
*/

   
