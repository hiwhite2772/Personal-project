import java.util.Scanner;

public class Bai08 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Nhap so nguyen n: ");
        int n = scanner.nextInt();

        int tongchan = 0, tongle = 0;

        for (int i = 1; i <= n; i++) {
            if (i % 2 == 0)
                tongchan += i;
            else
                tongle += i;
        }

        System.out.println("Tong các so le = " + tongle);
        System.out.println("Tong các so chan = " + tongchan);
    }
}
