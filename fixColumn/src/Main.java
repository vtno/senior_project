import com.opencsv.CSVReader;
import java.io.FileReader;
import java.io.IOException;
import org.apache.commons.lang3.math.NumberUtils;
import org.apache.commons.lang3.StringUtils;

//Currently in-working
//With speculation, misaligned tab can be corrected by verifying data consistency in a column
//Shift one by one
public class Main {

    public static void main(String[] args) throws IOException {

        CSVReader reader = new CSVReader(new FileReader("01S20152.csv"));
        String [] nextLine;
        int count = 0;
        while((nextLine = reader.readNext()) != null) {
            System.out.println(nextLine.length);
            String [] splitted = nextLine[0].split("\t");
            System.out.println(splitted.length);

        }
        System.out.println("There are " + count + " rows that are S/U");

    }
}
