import java.util.Arrays;
import java.util.Objects;

public class Matrix {
    private final int rows;
    private final int cols;
    private final int[][] data;

    // 构造方法：创建指定行数和列数的矩阵
    public Matrix(int rows, int cols) {
        if (rows <= 0 || cols <= 0) {
            throw new IllegalArgumentException("行数和列数必须大于 0");
        }

        this.rows = rows;
        this.cols = cols;
        this.data = new int[rows][cols];
    }

    // 初始化矩阵元素
    public void initValue(int[][] values) {
        if (values == null || values.length != rows) {
            throw new IllegalArgumentException("矩阵行数不匹配");
        }

        for (int i = 0; i < rows; i++) {
            if (values[i] == null || values[i].length != cols) {
                throw new IllegalArgumentException("矩阵列数不匹配");
            }
        }

        for (int i = 0; i < rows; i++) {
            System.arraycopy(values[i], 0, data[i], 0, cols);
        }
    }

    // 矩阵加法：返回一个新的矩阵
    public Matrix add(Matrix other) {
        checkDimensions(other);

        Matrix result = new Matrix(rows, cols);

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result.data[i][j] = this.data[i][j] + other.data[i][j];
            }
        }

        return result;
    }

    // 矩阵减法：返回一个新的矩阵
    public Matrix sub(Matrix other) {
        checkDimensions(other);

        Matrix result = new Matrix(rows, cols);

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                result.data[i][j] = this.data[i][j] - other.data[i][j];
            }
        }

        return result;
    }

    // 检查两个矩阵是否具有相同的行数和列数
    private void checkDimensions(Matrix other) {
        if (other == null || rows != other.rows || cols != other.cols) {
            throw new IllegalArgumentException("两个矩阵的行数和列数必须相同");
        }
    }

    // 将矩阵转换为字符串
    @Override
    public String toString() {
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < rows; i++) {
            sb.append(Arrays.toString(data[i]));
            if (i < rows - 1) {
                sb.append("\n");
            }
        }

        return sb.toString();
    }

    // 比较两个矩阵的行数、列数和元素是否完全相同
    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }

        if (!(obj instanceof Matrix)) {
            return false;
        }

        Matrix other = (Matrix) obj;

        return rows == other.rows
                && cols == other.cols
                && Arrays.deepEquals(data, other.data);
    }

    // equals 重写后，通常也应重写 hashCode
    @Override
    public int hashCode() {
        int result = Objects.hash(rows, cols);
        result = 31 * result + Arrays.deepHashCode(data);
        return result;
    }
}
