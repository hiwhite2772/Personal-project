import java.util.Scanner;
public class Bai09 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap vao mot so nguyen: ");
        int n = scanner.nextInt();
        if (n > 0) {
            System.out.println("Day la so nguyen duong");
        } else if (n < 0) {
            System.out.println("Day la so nguyen am");
        } else {
            System.out.println("Đay la so 0");
        }
        
        scanner.close();
    }
}
