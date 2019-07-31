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
	System.out.println("圆的半径："+radius);
	System.out.println("圆的高："+hight);
	System.out.println("面积为："+area);
	System.out.println("周长为："+perimete);
System.out.println("体积为："+volume);
}
}
