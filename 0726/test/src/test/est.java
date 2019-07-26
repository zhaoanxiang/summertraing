package test;


public class est {
public String chibang="chibang";
public String jiao;
public String wuzang;

public est() {
	System.out.println("gouzaoff");
	// TODO Auto-generated constructor stub
}
//public est(String s) {
//System.out.println("gouzaoff");
 //TODO Auto-generated constructor stub
//}
public void fly() {
	System.out.println("fly");
}
public void fly(String s) {
	System.out.println(s+"  fly-----");
}
public void eat() {
	System.out.println("eat");
	
}
public void food() {
	System.out.println("food");
}
public static void main(String[] args) {
	
    //est bird= new est();
	est bird= new est("ÄñµÄ³á°ò","ÄñµÄ½Å","ÄñµÄÎåÔà");
    bird.fly();
    bird.eat();
    bird.food(); 
    bird.fly("ss");
    System.out.println(bird.chibang);
}
public est(String chibang, String jiao, String wuzang) {
	super();
	this.chibang = chibang;
	this.jiao = jiao;
	this.wuzang = wuzang;
}
}
