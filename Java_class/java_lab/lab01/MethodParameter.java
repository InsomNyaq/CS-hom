public class MethodParameter{
    public static void main(String[] args){
        int a = 6;
        char[] str = new char[]{'H', 'e', 'l','l','o'};
        StringBuffer sb = new StringBuffer("TOM");
        changeAddr(str, sb);
        System.out.println(str);
        System.out.println(sb.toString());
        changeValue(a, str, sb);
        System.out.println(a);
        System.out.println(str);
        System.out.println(sb.toString());
    }
    private static void changeAddr(char[] c, StringBuffer sb){
        c = new char[] {'Y', 'e', 'l', 'l', 'o'};
        sb = new StringBuffer("SawYer");
    }

    private static void changeValue(int a, char[] c, StringBuffer sb){
        a = 8;
        c[0] = 'Y';
        sb.append(" Sawya");
    }
}
