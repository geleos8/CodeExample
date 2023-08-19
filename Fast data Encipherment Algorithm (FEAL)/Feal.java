import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Random;

public class Feal {
    public static final int FEAL = 4;
    private ArrayList<byte[]> decrypted;
    private int missing;
    public static   final int ENCRYPT = 1;
    public static   final int DECRYPT = 2;
    public static   final int BLOCK_LEN = 8;
    private byte[] myFile;
    private byte[]  key;
    private ArrayList<byte[]> encrypted;
    private boolean pic;
    private int height;
    private int width;
    private int imgType;
    private boolean ofb;
    private byte[] initVect;

    public Feal(String filename, byte[]  key, boolean ofb) throws IOException {
        initVect = new byte[8];
        this.key=key;
        this.ofb=ofb;
        FileInputStream fis = new FileInputStream(new File(filename));
        myFile = new byte[fis.available()];
        fis.read(myFile, 0, fis.available());
        encrypted=new ArrayList<>();
        decrypted=new ArrayList<>();
        pic=false;
    }

    public Feal(String filename, byte[] key, boolean pic, boolean ofb) {
        initVect = new byte[8];
        this.key=key;
        this.pic=pic;
        this.ofb=ofb;
        encrypted=new ArrayList<>();
        decrypted=new ArrayList<>();
        BufferedImage source = null;
        try {
            source = ImageIO.read(new File(filename));
        } catch (IOException e) {
            e.printStackTrace();
        }
         width=source.getWidth();
        height=source.getHeight();
       myFile = new byte[width * height * 3];
        int count = 0;
        for (int x = 0; x < source.getHeight(); x++) {
            for (int y = 0; y < source.getWidth(); y++) {
                Color color = new Color(source.getRGB(y, x));
                myFile[count] = (byte)color.getRed();
                myFile[count+1] = (byte)color.getGreen();
                myFile[count+2] = (byte)color.getBlue();
                count+=3;
            }
        }

       imgType = source.getType();

    }

    public void writeImg(ArrayList<byte[]> img, int type) throws IOException {
        ArrayList<Byte> b=new ArrayList<>();
        for (byte[] arr : img) {
            for (byte value : arr) {
                b.add(value);
            }
        }
        BufferedImage res1 = new BufferedImage(width, height, imgType);
        int count = 0;
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                int Red = b.get(count);
                if (Red < 0)
                    Red += 256;
                int Green = b.get(count + 1);
                if (Green < 0)
                    Green += 256;
                int Blue = b.get(count + 2);
                if (Blue < 0)
                    Blue += 256;
                Color newColor = new Color(Red, Green, Blue);
                res1.setRGB(x, y, newColor.getRGB());
                count += 3;
            }
        }
        File output1 =null;
        if(type==1) {
            if(ofb)
                output1 = new File("E:\\Программы\\FEAL\\src\\enc.bmp");
            else
                output1 = new File("E:\\Программы\\FEAL\\src\\enc1.bmp");

        }
        else {

            if (ofb){
                output1 = new File("E:\\Программы\\FEAL\\src\\dec.bmp");

        }
            else
                output1 = new File("E:\\Программы\\FEAL\\src\\dec1.bmp");
        }
        ImageIO.write(res1, "bmp", output1);
        //if(type==DECRYPT) ImageIO.write(res1, "bmp", output2);
    }

    public ArrayList<byte[]> getEncrypted() {
        return encrypted;
    }

    public void createFeal(int type) throws IOException {

        ArrayList<byte[]> rKeys = generateRoundKeys(key);
        byte[] prevBlock = new byte[8];
        if(type==DECRYPT) {
            if(!ofb) {
                ArrayList<byte[]> tmp = new ArrayList<>();
                for (int i = rKeys.size() - 3; i >= 0; i--)
                    tmp.add(rKeys.get(i));
                tmp.add(rKeys.get(rKeys.size() - 1));
                tmp.add(rKeys.get(rKeys.size() - 2));
                rKeys.clear();
                rKeys.addAll(tmp);
            }
            if(ofb){//
                byte[]   b = encrypted.get(2);
                for (int i = 0; i <b.length; i++) {
                   b[i]=0;
                }
                encrypted.remove(2);
                encrypted.add(2,b);


            }
            int  k=0;
            for (byte[] t : encrypted) {
                for (byte b : t) {
                    myFile[k] = b;
                    k++;
                }
            }
        }
        if(ofb&&type==ENCRYPT) {
            Random r = new Random();
            for (int i = 0; i < prevBlock.length; i++) {
                r.nextBytes(prevBlock);
            }
            initVect=prevBlock;

        }
        else if(ofb&&type==DECRYPT) {
           prevBlock=initVect;
        }

        if(myFile.length%BLOCK_LEN!=0) {
            missing = myFile.length%BLOCK_LEN;
            byte[] newArr=new byte[myFile.length+(BLOCK_LEN-missing)];
            int j;
            for (j = 0; j < myFile.length; j++) {
                newArr[j]=myFile[j];
            }
            j++;
            for (int i = j; j < BLOCK_LEN - missing; j++) {
               newArr[j]=0;
            }
            myFile=newArr;
        }

        for (int i = 0; i<myFile.length/BLOCK_LEN; i++) {
            byte[] block =new byte[BLOCK_LEN];

            if(!ofb) {
                System.arraycopy(myFile, i*BLOCK_LEN,block,0,BLOCK_LEN);
            }
            else {
                System.arraycopy(prevBlock, 0, block, 0, BLOCK_LEN);
            }
            block = XOR(block, rKeys.get(rKeys.size()-2));
            ArrayList<byte[]> XORs = new ArrayList<byte[]>();
            byte[] leftPart = new byte[4], rightPart = new byte[4];
            System.arraycopy(block, 0, leftPart, 0, block.length / 2);
            System.arraycopy(block, block.length / 2, rightPart, 0, block.length / 2);
            XORs.add(leftPart);
            XORs.add(XOR(leftPart, rightPart));
            int k=2;
            for(int j=0; j<FEAL; j++, k++) {
                byte[] f = f(rKeys.get(j),XORs.get(k-1));
                XORs.add(XOR(f, XORs.get(k-2)));
            }
            leftPart=XORs.get(k-1);
            rightPart=XOR(XORs.get(XORs.size()-1), XORs.get(XORs.size()-2));
           byte[] ex=new byte[8];
           System.arraycopy(leftPart,0,ex,0,leftPart.length);
           System.arraycopy(rightPart,0,ex,ex.length/2,rightPart.length);
           ex=XOR(ex,rKeys.get(rKeys.size()-1));
           if(ofb&&type==ENCRYPT) {
               byte[] curInf = new byte[8];
               System.arraycopy(myFile, i*BLOCK_LEN,curInf,0,BLOCK_LEN);
               ex=XOR(ex, curInf);
               prevBlock=ex;
           }
           else if(ofb&&type==DECRYPT) {
               byte[] curInf = new byte[8];
               System.arraycopy(myFile, i*BLOCK_LEN,curInf,0,BLOCK_LEN);
               prevBlock=curInf;
               ex=XOR(ex, curInf);
           }
           if(type==ENCRYPT) {
              // System.out.println("ENCRYPT"+i+Arrays.toString(ex));
               encrypted.add(ex);
           }
           else if(type==DECRYPT) {
              // System.out.println("DECRYPT "+i+Arrays.toString(ex));
               decrypted.add(ex);
           }

        }
        if(type==ENCRYPT && !pic) {
            FileOutputStream fos  = null;
            try {
                fos = new FileOutputStream(new File("E:\\Программы\\FEAL\\src\\encrypted.txt"));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
            assert fos != null;
            for (int i=0;i<encrypted.size();i++) {
                if(i==encrypted.size()-1) {
                    byte[] arr = encrypted.get(i);
                    int j = 0;
                    while (j < missing) {
                        fos.write(arr[j]);
                        j++;
                    }
                }
                else {
                   fos.write(encrypted.get(i));
                }
            }

        }
        if(type==DECRYPT && !pic) {
            FileOutputStream fos  = null;
            try {
                fos = new FileOutputStream(new File("E:\\Программы\\FEAL\\src\\decrypted.txt"));
            } catch (FileNotFoundException e) {
                e.printStackTrace();
            }
            assert fos != null;
            for (int i=0;i<decrypted.size();i++) {
                if(i==decrypted.size()-1) {
                    byte[] arr = decrypted.get(i);
                    int j = 0;
                    while (j < missing) {
                        fos.write(arr[j]);
                        j++;
                    }
                }
                else {
                   fos.write(decrypted.get(i));
                }
            }

        }
        else if(type == DECRYPT) {
            writeImg(decrypted, DECRYPT);
        }
        else if(type==ENCRYPT&&pic) {
            writeImg(encrypted, ENCRYPT);
        }
    }

    public ArrayList<byte[]> generateRoundKeys(byte[]  key) {
        ArrayList<byte[]> roundKeys=new ArrayList<>();
        byte[] leftPart = new byte[4], rightPart = new byte[4];
        System.arraycopy(key,0,leftPart,0,4);
        System.arraycopy(key,key.length/2,rightPart,0,4);

        byte[] k01=extendKey(leftPart,rightPart);
        byte[] k = new byte[2],kk = new byte[2],kkk = new byte[2],kkkk = new byte[2];
        System.arraycopy(k01,0,k,0,2);
        roundKeys.add(k);
        System.arraycopy(k01,2,kk,0,2);
        roundKeys.add(kk);

        byte[] temp1 = XOR(leftPart, k01);
        byte[] k23 = extendKey(temp1, rightPart);
        System.arraycopy(k23,0,kkk,0,2);
        roundKeys.add(kkk);
        System.arraycopy(k23,2,kkkk,0,2);
        roundKeys.add(kkkk);

        byte[] temp2 = XOR(rightPart, k23);
        byte[] k4 = extendKey(temp2, k01);
        byte[] temp3 = XOR(k4, k01);
        byte[] k5 = extendKey(temp3, k23);
        byte[] k45 = new byte[8];
        System.arraycopy(k4,0,k45,0,k4.length);
        System.arraycopy(k5,0,k45,k45.length/2,k5.length);
        roundKeys.add(k45);

        byte[] temp4 = XOR(k4, k5);
        byte[] k6 = extendKey(temp4, k4);
        byte[] temp5 = XOR(k6, k5);
        byte[] k7 = extendKey(temp5, k5);
        byte[] k67 = new byte[8];
        System.arraycopy(k6,0,k67,0,k6.length);
        System.arraycopy(k6,0,k67,k67.length/2,k7.length);
        roundKeys.add(k67);

        return roundKeys;
    }

    public byte[] extendKey(byte[] x, byte[] y) {//fk
        byte[] resKey = new byte[4];
        byte t1=(byte)(x[0]^ x[1]);
        byte t2=(byte)(x[2]^ x[3]);
        resKey[1]=S1(t1,(byte)(t2^ y[0]));
        resKey[2]=S0(t2,(byte)(resKey[1]^ y[1]));
        resKey[0]=S0(x[0],(byte)(resKey[1]^ y[2]));
        resKey[3]=S1(x[3],(byte)(resKey[2]^ y[3]));
        return  resKey;

    }

    public byte S0(byte a, byte b) {
        return (byte) ((((a + b) % 256) << 2) | (((a + b) % 256) >> 6));

    }

    public byte S1(byte a, byte b) {
        return (byte) ((((a + b + 1) % 256) << 2) | (((a + b + 1) % 256) >> 6));

    }

    public byte[] XOR(byte[] a, byte[] b) {
        byte[] res = new byte[a.length];
        for (int i = 0; i < a.length; i++) {
            res[i] = (byte) (a[i] ^ b[i]);
        }
        return res;
    }

    public byte[] f(byte[] roundKey, byte[] subblock) {//16,32
        byte[] f = new byte[4];
        byte t1 = (byte) (subblock[1] ^ roundKey[0]);
        byte t2 = (byte) (subblock[2] ^ roundKey[1]);
        byte t3 = (byte) (subblock[0] ^ t1);
        byte t4 = (byte) (subblock[3] ^ t2);
        f[1] = S1(t3, t4);
        f[0] = S0(f[1], subblock[0]);
        f[2] = S0(f[1], t4);
        f[3] = S1(f[2], subblock[3]);
        return f;

    }
}
