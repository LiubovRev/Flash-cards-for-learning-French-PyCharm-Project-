Flashy - Flashcard App

Flashy is a simple flashcard application built with Python and Tkinter to help users learn and review French vocabulary. The app shows French words and their English translations, tracks progress, and provides a fun way to study new words.
Features

    French/English Flashcards: Display French words with their English translations.

    Automatic Flip: Flashcards automatically flip after 3 seconds to show the English translation.

    Progress Tracking: Words marked as known are saved to a CSV file for future sessions.

    Interactive Buttons: Users can click buttons to indicate whether they know a word or not.

Requirements

    Python 3.x

    Tkinter (usually comes bundled with Python)

    Pandas

To install the required libraries, use:

pip install pandas

Installation

    Clone the repository:

git clone https://github.com/<your-username>/flashy.git

    Navigate to the project directory:

cd flashy

    Install the necessary Python libraries:

pip install pandas

    Ensure that the images folder is in the same directory as the script (it should contain the necessary images for the front and back of the flashcards, as well as the buttons for correct/wrong actions).

File Structure

    flashy.py: The main Python script to run the application.

    data/words_to_learn.csv: CSV file where words that the user still needs to learn are saved.

    data/french_words.csv: Default dataset of French words (if words_to_learn.csv is not found).

    images/: Folder containing the flashcard images (front, back) and button images (right/wrong).

How to Run

    Make sure you have Python 3.x and the required libraries installed.

    Place the images folder in the same directory as the script.

    Run the main Python script:

python flashy.py

How It Works

    When the app starts, a French word is displayed on the flashcard.

    After 3 seconds, the card automatically flips to show the English translation.

    If the user knows the word, they click the right button to mark it as known, and it will be removed from the list of words to learn.

    If the user doesn't know the word, they click the wrong button to move on to the next word.

    The app automatically saves the updated list of words to the CSV file.

Troubleshooting

    If words_to_learn.csv is not found, the app will automatically load the default dataset from french_words.csv.

    Ensure that the images folder is in the same directory as the script, and contains the necessary image files.

License

This project is licensed under the MIT License - see the LICENSE file for details.
