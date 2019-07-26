package test;

public class circle {
	public double r;

	public circle(double r) {
		super();
		this.r = r;
	}
	
	public circle() {
		
	}
	public void getArea() {
		System.out.println("圆的面积为："+Math.PI*r*r);
		
	}
	public void getPerimete() {
		System.out.println("圆的周长为"+Math.PI*r*2);
	}

}
