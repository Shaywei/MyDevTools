public class Gingleton {
    private static Gingleton INSTANCE = null;
    private static int c = 0;
    public int b;
    public static Gingleton getInstance()
    {
        if ( INSTANCE == null )
        {
            c++;
            INSTANCE = new Gingleton(c);
        }
        return INSTANCE;
    }

    private Gingleton(int _c) {
        b = _c;
    }
}

