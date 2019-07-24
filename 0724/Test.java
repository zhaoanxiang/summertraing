package test;

public class Test {
		public static void main(String[] args) {
		    int[] fib=new int[20];
		    int sum=0;
		    FIB(fib);
		    for(int f:fib) {
		        System.out.println(f);
		        sum+=f;
		    }
		    System.out.println("ºÍÎª£º"+sum);
		}
		private static void FIB(int[] fib) {
		    fib[0]=1;
		    fib[1]=1;
		    for(int i=2;i<20;i++) {
		        fib[i]=fib[i-1]+fib[i-2];
		    }
		}
		}

