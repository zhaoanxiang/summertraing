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
		System.out.println("���Ϊ��"+Math.PI*r*r);
		
	}
	public void getPerimete() {
		System.out.println("�ܳ�Ϊ��"+Math.PI*r*2);
	}

}
