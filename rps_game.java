import java.util.Scanner;
import java.util.Random;

public class rps_game {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Press 1 for Rock");
        System.out.println("Press 2 for Paper");
        System.out.println("Press 3 for Scissor");
        System.out.println(" ");
        int input_user = sc.nextInt();
        String input_user1 = "ok";
        if (input_user == 1) {
            input_user1 = "Rock";
        } else if (input_user == 2) {
            input_user1 = "Paper";
        } else if (input_user == 3) {
            input_user1 = "Scissor";
        } else {
            System.out.println("Please Select Valid Option...");
            // break;
        }
        Random rd = new Random();
        int computer_input = rd.nextInt(1, 4);
        String computer_input1 = "OOK";
        // if (computer_input == 0) {
        // System.out.println("Please Choose Valid Option...");
        // break;
        // }
        if (computer_input == 1) {
            computer_input1 = "Rock";
        } else if (computer_input == 2) {
            computer_input1 = "Paper";
        } else if (computer_input == 3) {
            computer_input1 = "Scissor";
        }
        if (input_user1 == computer_input1) {
            System.out.println("Both Choosed: " + input_user1);
            System.out.println("Game Draw...");
        } else if (input_user1 == "Rock" && computer_input1 == "Scissor"
                || input_user1 == "Paper" && computer_input1 == "Rock"
                || input_user1 == "Scissor" && computer_input1 == "Paper") {
            System.out.println("You Choosed: " + input_user1);
            System.out.println("Computer Choosed: " + computer_input1);
            System.out.println("Congratulations");
            System.out.println("You Win....");
        } else {
            System.out.println("You Choosed: " + input_user1);
            System.out.println("Computer Choosed: " + computer_input1);
            System.out.println("You Lose....");
        }
    }
}