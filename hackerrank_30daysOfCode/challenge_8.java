//Complete this code or write your own from scratch
import java.util.*;
import java.io.*;

class Solution{
   public static void main(String []args)
   {
      Scanner in = new Scanner(System.in);
      int N=in.nextInt();
      in.nextLine();
      HashMap<String,Integer> dict=new HashMap<String,Integer>();
      for(int i=0;i<N;i++) {
         String name=in.nextLine();
         int phone=in.nextInt();
         in.nextLine();
         dict.put(name,phone);    
      }
      while(in.hasNext())
      {
         String s=in.nextLine();
         if (dict.get(s) == null) {
             System.out.println("Not found");
         } else {
             System.out.println(s+"="+dict.get(s)); 
         ; 
      }
   }
}

class Solution {
	public static void main (String [] args) {
		Scanner in = new Scanner(System.in); 
		int N = in.nextInt(); 
		HashMap<String,Integer> dict = new HashMap<String,Integer>(); 
	}
}
