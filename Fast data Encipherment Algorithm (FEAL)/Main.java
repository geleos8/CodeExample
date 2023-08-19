import java.io.IOException;
import java.util.ArrayList;
import java.util.Random;

public class Main {
    public static void main(String[] args) throws IOException {
        byte[] key  =  new byte[8] ;
        Random r   =   new Random();
        for (int i = 0; i < key.length; i++) {
            r.nextBytes(key);
        }

        Feal   f   =   new Feal("E:\\Программы\\FEAL\\src\\text.txt",key, true);
        f.createFeal(1);
        f.createFeal(2);

        Feal   f2   =   new Feal("E:\\Программы\\FEAL\\src\\tank.bmp",key,true, true);
        f2.createFeal(1);
        f2.createFeal(2);

    }
}