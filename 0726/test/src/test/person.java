package test;

public class person {
	
		 public int age;
		 public String name;
		 public person (int age,String name) {
			 super();
			 this.age=age;
			 this.name=name;
		 }
		 public person() {
		}
		 public void display() {
			 System.out.println("年龄为:"+age+"  "+"姓名:"+name);
		 }
		public static void main(String[] args) {
			person person=new person(23,"zhaoanxiang");
			person.display();
		}
		}

