package test;

//import java.util.Scanner;

public class circle {
	private float radius;

	public circle(float radius) {
		this.radius = radius;
	}
	public circle() {
		
	}
	public double getArea() {
		return Math.PI*radius*radius;
	}
	public double getPerimete() {
		return Math.PI*radius*2;
	}
    public void show() {
	double area=getArea();
	double perimete=getPerimete();
	System.out.println("圆的半径："+radius);
	System.out.println("面积为："+area);
	System.out.println("周长为："+perimete);
}
   /*public static void main(String[] args) {
	@SuppressWarnings("resource")
	Scanner sc=new Scanner(System.in);
	System.out.println("请输入半径:");
	float radius=sc.nextFloat();
	circle circle=new circle(radius);
	circle.show();*/
}

