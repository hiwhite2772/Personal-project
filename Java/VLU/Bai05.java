public class Bai05 {
 public static void main(String[] args) {
    int a=5, b=4, c=3;
    double p=(a+b+c)/2;
    double chuvi=p*2;
    double dientich=Math.sqrt(p*(p-a)*(p-b)*(p-c));
    System.out.println("nua chu vi tam giac = " + p);
    System.out.println("chu vi tam giac = " + chuvi);
    System.out.println("dien tich tam giac = " + dientich);
  }
 }