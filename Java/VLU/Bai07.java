import java.util.Scanner;

public class Bai07 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Nhap so nguyen n: ");
        int n = scanner.nextInt();
        
        if (n > 0)
            System.out.println("So nguyen duong");
        else
            System.out.println("So nguyen am");
    }
}
