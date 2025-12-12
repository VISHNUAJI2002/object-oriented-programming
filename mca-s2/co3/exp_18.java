/*
Experiment 18 
Interface 2- Prepare bill with the given format

Aim
Prepare bill with the given format using calculate method from interface.
Order No.:
Date :
Product Id Name Quantity unit price Total

101 A 2 25 50
102 B 1 100 100
Net. Amount 150
*/

import java.util.Scanner;

interface Billcalc{
    void calculate_total();
}

class Bill implements Billcalc{
    
    int orderno,pid,quantity;
    String pname;
    float unitprice,total_price;
    static float net_total=0;

    Bill(String pname,int pid,int quantity,float unitprice){
        this.pname=pname;
        this.pid=pid;
        this.quantity=quantity;
        this.unitprice=unitprice;
        calculate_total();
        calc_net_total();
    }

    public void calculate_total(){
        total_price=quantity*unitprice;
    }

    void calc_net_total(){
        net_total+=total_price;
    }

    void display(){
        System.out.println(pid+"\t\t"+pname+"\t\t"+quantity+"\t\t"+unitprice+"\t\t"+total_price);
        System.out.println("------------------------------------------------------------------------");
    }
    
    static void display_net_total(){
        System.out.println("\t\t\tNet Amount\t"+net_total);
    }
}

class Product{
    public static void main(String args[]){
        Scanner s=new Scanner(System.in);

        int pid,qty;
        String pname;
        float price;

        System.out.println("Product list\n----------");
        System.out.println("Product id\tProduct name\tPrice\n----------------------");
        System.out.println("101\t\tA\t\t50");
        System.out.println("105\t\tB\t\t20");
        System.out.println("Enter the number of products needed : ");
        int n = s.nextInt();
        s.nextLine();

        Bill bill[]=new Bill[n];

        for(int i=0;i<n;i++){
            System.out.println("Enter product id and product name : ");
            pid = Integer.parseInt(s.nextLine());
            pname = s.nextLine();

            System.out.println("Enter quantity and unit price : ");
            qty = Integer.parseInt(s.nextLine());
            price = Float.parseFloat(s.nextLine());

            bill[i] = new Bill(pname,pid,qty,price);
        }

        System.out.println("Product id\tProduct name\tQuantity\tUnit Price\tTotal");
        System.out.println("------------------------------------------------------------------------");

        for(Bill b:bill){
        b.display();
        }
        Bill.display_net_total();
    }
}

/*
Sample Output:
Product list
----------
Product id      Product name    Price
----------------------
101             A               50
105             B               20
Enter the number of products needed :
2
Enter product id and product name : 
101
A
Enter quantity and unit price : 
3
50
Enter product id and product name : 
105
B
Enter quantity and unit price : 
1
20
Product id      Product name    Quantity        Unit Price      Total
------------------------------------------------------------------------
101             A               3               50.0            150.0
------------------------------------------------------------------------
105             B               1               20.0            20.0
------------------------------------------------------------------------
                        Net Amount      170.0

*/                        