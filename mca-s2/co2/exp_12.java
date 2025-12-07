/*
Experiment 12

Inner class and Static nested class

Aim: Create CPU with attribute price. Create inner class Processor with attributes no. of
cores, manufacturer and static nested class RAM with attributes memory and
manufacturer. Create an object of CPU class and print information of Processor
and RAM.
*/

import java.util.*;
class CPU{
    int price;
    CPU(int price){
        this.price=price;
    }


    class Processor{
        int cores;
        String manufacturer;
        Processor(int cores,String manufacturer){
            this.cores=cores;
            this.manufacturer=manufacturer;
        }
        void displayProcessorInfo(){
            System.out.println("\nProcessor Information");
            System.out.println("Number of cores:"+cores);
            System.out.println("Manufacturer:"+manufacturer);
        }
    }

    static class RAM{
        int memory;
        String manufacturer;
        RAM(int memory,String manufacturer){
            this.memory=memory;
            this.manufacturer=manufacturer;
        }
        void displayRamInfo(){
            System.out.println("\nRAM Information:");
            System.out.println("Memory size: "+memory+" GB");
            System.out.println("Manufacturer: "+manufacturer);
        }
    }
}

class CpuMain{
    public static void main(String args[]){
        Scanner s = new Scanner(System.in);
        System.out.print("Enter price of CPU :");
        int price=s.nextInt();
        System.out.print("Enter number of cores of CPU :");
        int cores=s.nextInt();
        System.out.print("Enter memory size :");
        int memory=s.nextInt();
        s.nextLine();
        System.out.print("Enter Processor Manufacturer name :");
        String pm=s.nextLine();
        System.out.print("Enter Ram Manufacturer name :");
        String rm=s.nextLine();

        CPU c=new CPU(price);
        CPU.Processor p =c.new Processor(cores,pm);
        CPU.RAM r=new CPU.RAM(memory,rm);
        p.displayProcessorInfo();
        r.displayRamInfo();
    }
}

/*
Sample Output:

Enter price of CPU :55000
Enter number of cores of CPU :4
Enter memory size :256
Enter Processor Manufacturer name :Pedri
Enter Ram Manufacturer name :Iniesta

Processor Information
Number of cores:4
Manufacturer:Pedri

RAM Information:
Memory size: 256 GB
Manufacturer: Iniesta
*/


