public class HelloWorld{
public void display(){
System.out.println("Hello World");
}
  public int add(int x,int y){
    return x+y;
  }
  public int substraction(int x,int y){
    return x-y;
  }

public static void main(String []args){
HelloWorld obj =new HelloWorld();
obj.display();
System.out.println(obj.add(3,4));
System.out.println(obj.substraction(5,4));
}
}
