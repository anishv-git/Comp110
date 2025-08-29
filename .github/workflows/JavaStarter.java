package assn01;

import java.util.Scanner;


public class JavaStarter {

    public static double quadFun(double a, double b, int m){
        return a * m * m +b;
    }

    public static String stringFun(String s1){
        return s1.toUpperCase();
    }

    public static String stringFun2(String s2, int i1, int i2, int i3, int i4) {
        String sA = s2.substring(i1, i2);
        String sB = s2.substring(i3, i4);
        return sA + sB;
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        int n = scanner.nextInt();

        if (n == 1) {
            System.out.println("Hello, Universe!");
        } else if (n == 2) {
            double a = scanner.nextDouble();
            double b = scanner.nextDouble();
            int m = scanner.nextInt();
            System.out.println("a = " + a + ", b = " + b + ", m = " + m);

        } else if (n == 3) {
            double a = scanner.nextDouble();
            double b = scanner.nextDouble();
            int m = scanner.nextInt();
            double result = quadFun(a, b, m);
            System.out.println(result);
        } else if (n == 4) {
            String s1 = scanner.next();
            String result = stringFun(s1);
            System.out.println(result);
        } else if (n == 5) {
            String s2 = scanner.next();
            int i1 = scanner.nextInt();
            int i2 = scanner.nextInt();
            int i3 = scanner.nextInt();
            int i4 = scanner.nextInt();
            String result = stringFun2(s2, i1, i2, i3, i4);
            System.out.println(result);
        } else if (n == 6) {
            int m = scanner.nextInt();
            double[] arr = new double[m];

            double sum = 0.0;
            for (int i = 0; i < m; i++) {
                arr[i] = scanner.nextDouble();
                sum += arr[i];
            }

            double avg = sum / m;
            System.out.printf("Average = %.2f\n", avg);

            for (int i = m - 1; i >= 0; i--) {
                System.out.println("arr[" + i + "]=" + arr[i]);
            }
            scanner.close();


        }
    }
}
