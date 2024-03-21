import java.text.SimpleDateFormat;
import java.util.Date;

public class DateExample {
    public static void main(String[] args) throws Exception {
        // Current date and time
        Date now = new Date();
        System.out.println("Current Date and Time: " + now);

        // Formatting date
        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
        String formattedDate = sdf.format(now);
        System.out.println("Formatted Date and Time: " + formattedDate);

        // Parsing a date string
        String dateStr = "2024-03-21 10:00:00";
        Date expiredDate = sdf.parse(dateStr);
        System.out.println("Parsed Date and Time: " + expiredDate);

        // ERROR: it should now.after(expiredDate) instead.
        boolean expired = expiredDate.after(now);
        if (expired) {
            System.out.println("The product has expired");
        } else {
            System.out.println("The product is still valid");
        }
    }
}
