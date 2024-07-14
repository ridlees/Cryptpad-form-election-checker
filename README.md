# Cryptpad-form-election-checker
#Cryptpad Turn Forms into preferential election|voting|decide tool.

Do you want to vote with the ability to make preference in votes? Now you can with this script and Cryptpad!

## Dependencies
* python3.8 (should work on newer versions, too)

## Usage
0. Download the main.py (either through ZIP download or git clone)
1. Go to your cryptpad instance (I am using the Czech one at [cryptpad.cz](https://cryptpad.cz))
2. Select Forms and create your form. Name it anything you want.
3. Inside form, use only **Checkbox grids**. Create your first vote by selecting a Checkbox grind.
4. Set as many rows as preferences you want to use. Name them anything you want.
5. Set the columns to your "candidates" or options. You can add one extra with the value Abstain, if you want.
6. Set the **Maximum selectable options** to 1. 
7. You should have Checkbox grid like this one:
![Screenshot of Checkbox grid.](/images/image1.png)

8. Copy the public link and send it to your voters. Let them vote.
9. When you have all the votes you need, click on **Responses** in your Cryptpad instance.
![Screenshot of Responses button](/images/image2.png)
10. At the Responses screen, click on **Export** and select **Export to JSON**.
![Screenshot of Export selection](/images/image3.png)
11. Wait until you download the JSON file. Its name will be the same as the name of your Form.

12. In your computer, move your JSON file into the *Cryptpad-form-election-checker* folder.
13. Open terminal/cmd.
14. Run `python3 main.py <Name of your JSON.json>`.
15. In your terminal, you will see your winner with the winning score.

## Political theory

Preferential voting has certain psychological effect on the voters, because it creates stronger relationship with them and electee (or the selected option). It allows to make your vote count in multiple rounds. The voting method of this script is with weighted votes (1st preference has weight 1, 2nd halved, etc.), so the one with overall most "votes" is selected.

## Credits

If you tried it, message me at twitter.com/KapesniP to let me know what you think about this.