public class MatrixTest {
    public static void main(String[] args) {
        // 创建两个 2 行 3 列的矩阵
        Matrix a = new Matrix(2, 3);
        Matrix b = new Matrix(2, 3);

        // 初始化矩阵元素
        a.initValue(new int[][]{
                {1, 2, 3},
                {4, 5, 6}
        });

        b.initValue(new int[][]{
                {6, 5, 4},
                {3, 2, 1}
        });

        // 打印原矩阵
        System.out.println("矩阵 A：");
        System.out.println(a);

        System.out.println("矩阵 B：");
        System.out.println(b);

        // 矩阵加法
        Matrix sum = a.add(b);
        System.out.println("A + B：");
        System.out.println(sum);

        // 矩阵减法
        Matrix difference = a.sub(b);
        System.out.println("A - B：");
        System.out.println(difference);

        // 测试 equals
        Matrix c = new Matrix(2, 3);
        c.initValue(new int[][]{
                {1, 2, 3},
                {4, 5, 6}
        });

        System.out.println("A 是否等于 C：" + a.equals(c));
        System.out.println("A 是否等于 B：" + a.equals(b));
    }
}
