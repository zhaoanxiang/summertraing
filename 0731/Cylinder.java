package test;

public class Cylinder extends circle{
private double hight;
private float radius;
public Cylinder(float radius, double hight) {
	super(radius);
	this.hight = hight;
	this.radius=radius;
}

public double getVolume() {
	return getArea()*hight;
}

public void showVolume() {
	double volume=getVolume();
	double area=getArea();
	double perimete=getPerimete();
	System.out.println("Բ�İ뾶��"+radius);
	System.out.println("Բ�ĸߣ�"+hight);
	System.out.println("���Ϊ��"+area);
	System.out.println("�ܳ�Ϊ��"+perimete);
System.out.println("���Ϊ��"+volume);
}
}
