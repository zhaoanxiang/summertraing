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
	System.out.println("Բ�İ뾶��"+radius);
	System.out.println("���Ϊ��"+area);
	System.out.println("�ܳ�Ϊ��"+perimete);
}
   /*public static void main(String[] args) {
	@SuppressWarnings("resource")
	Scanner sc=new Scanner(System.in);
	System.out.println("������뾶:");
	float radius=sc.nextFloat();
	circle circle=new circle(radius);
	circle.show();*/
}

