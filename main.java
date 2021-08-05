import java.util.Scanner;

// Algumas funções em java com o tempo que sobrou

class Main {
  public static void main(String[] args) {
    System.out.println(_1());
  }

  public static int _1() {
    Scanner scan = new Scanner(System.in);
    int pares = 0;
    while (true) {
      System.out.println("Digita um número com 4 digitos");
      Integer num = scan.nextInt();

      if (num<1000 || num>9999) {
        System.out.println("O número deve ser de 1000 a 9999");
        continue;
      }
      
      for (String i : num.toString().split("")) {
        if (new Integer(String.valueOf(i)) % 2 == 0) pares++;
      }
      return pares;
    }
  }
}