public class Foo{
    public static void main(String[] args) {
    System.out.println("Hello World!"); //Display the string.
    System.out.println(Foo.isConfusing()); //Display the string.
    }
    
    public static boolean isConfusing() {
       try {
         return true;
       } 
       finally {
         return false;
       }
    }
}