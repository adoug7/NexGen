import javax.swing.*;  
import java.util.Scanner;
import java.util.Timer;
import java.util.TimerTask;
import java.lang.Thread;
import java.util.Date;
import java.util.Random;
import java.util.concurrent.ThreadLocalRandom;
import java.awt.*;

class LabelExample  
{  
    static int interval;
static Timer timer;
static int[] packages = new int[100];
public static void main(String args[])  
    {  
        Random rand = new Random();
   // Scanner sc = new Scanner(System.in);
   // System.out.print("Input seconds => : ");
   // String secs = sc.nextLine();
   // int delay = 1000;
   // int period = 1000;
    //timer = new Timer();
    //interval = Integer.parseInt(secs);
    //timer.scheduleAtFixedRate(new TimerTask() {

    //    public void run() {
    //        System.out.println(setInterval());

    //    }
    //}, delay, period);
    JFrame f= new JFrame("Label Example");     
    JLabel l1,l2, l3, l4;
    l1=new JLabel("first label");  
    Font labelFont = l1.getFont();
    l1.setFont(new Font(labelFont.getName(), Font.PLAIN, 96));
    //l1.setBounds(50,50, 100,30);
    l2=new JLabel("Second Label.");  
    l2.setFont(new Font(labelFont.getName(), Font.PLAIN, 48));
    //l2.setBounds(50,100, 100,30); 
    l3=new JLabel("third label");  
    l3.setFont(new Font(labelFont.getName(), Font.PLAIN, 48));
    //l3.setBounds(50,50, 100,30);
    l4=new JLabel("fourth label");  
    l4.setFont(new Font(labelFont.getName(), Font.PLAIN, 48));
   // l4.setBounds(50,100, 100,30); 
    f.add(l1); f.add(l2);  f.add(l3); f.add(l4);
    f.setSize(1600,900);  
    f.setLayout(new GridLayout(4,1));  
    f.setVisible(true); 
    
    for (int i = 0; i < 100; i++)
    {
        packages[i] = ThreadLocalRandom.current().nextInt(i*12,(i+1)*12);
    }
    for (int k = 0; k<100; k++)
    {
    
        while (packages[k] != 0)
            {
    for (int j = 0; j<100; j++)
    {
        packages[j]--;
    
    } 
     l1.setText("Next Package: " + Integer.toString(packages[k]));
     l2.setText("2nd Package " + Integer.toString(packages[k+1]));
     l3.setText("3rd Package " + Integer.toString(packages[k+2]));
     l4.setText("4th Package: " + Integer.toString(packages[k+3]));
   
        
    try
    {
         
    Thread.sleep(1000);
        }
        catch (InterruptedException ie) {
                ie.printStackTrace();
}
 }  
}
   // private static final int setInterval() {
    //if (interval == 1)
    //    timer.cancel();
   // return --interval;
//}
    }  
    
        }