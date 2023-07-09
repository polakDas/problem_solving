import java.util.ArrayList;
import java.util.List;

public class PascalTriangle2 {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> row = new ArrayList<Integer>();
        row.add(1);

        for (int i = 0; i < rowIndex; i++) {
            for (int j = row.size() - 1; j > 0; j--) {
                row.set(j, row.get(j) + row.get(j - 1));
            }

            row.add(1);
        }

        return row;
    }

    public static void main(String[] args) {
        int rowIndex = 5;
        PascalTriangle2 solve = new PascalTriangle2();
        System.out.println(solve.getRow(rowIndex));
    }
}
