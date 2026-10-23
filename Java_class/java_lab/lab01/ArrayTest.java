public class ArrayTest {
    public static void main(String[] args){
        int[] a;
        Person[] b;
        a = new int[10];
        b = new Person[3];
        for (int i=0; i<10; ++i){
            a[i] = (int)(100 * Math.random());
        }
        b[0] = new Person("Alice", 30, 'F');
        b[1] = new Person("John", 20, 'M');
        b[2] = new Person();
        b[2].setName("Bob");
        b[2].setAge(25);
        b[2].setSex('M');
        for (int i = 0; i<10; ++i){
            System.out.println("a["+i+"]="+a[i]);
        }
        System.out.println(b[0] + "\n" +b[1]+"n"+b[2]);
        System.out.println("The number of elements in a:" + a.length);
        System.out.println("The number of elements in b:" + b.length);
    }
}
