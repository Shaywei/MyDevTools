public class Gingleton {
  public static void main(String[] args) {
    System.out.println("Hello World!"); //Display the string.
    Gingleton g1 = Gingleton.getInstance();
    Gingleton g2 = Gingleton.getInstance();
    System.out.println(c); //Display the string.
    System.out.println(g1.b); //Display the string.
    System.out.println(g2.b); //Display the string.
  }

    private static Gingleton INSTANCE = null;
    private static int c = 0;
    public int b;
    public static Gingleton getInstance()
    {
        c++;
        if ( INSTANCE == null )
        {
            System.out.println("Creating!"); //Display the string.
            INSTANCE = new Gingleton(c);
        }
        System.out.println("returning Gingleton"); //Display the string.
        return INSTANCE;
    }

    private Gingleton(int _b) {
        b = _b;
    }
}
