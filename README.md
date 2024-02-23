## Overview

Flapy is a simple language learning flashcard app built with Python and Tkinter. It helps users learn new words by presenting them with French words and testing their knowledge of corresponding English translations.

## Features

- Interactive flashcards with French and English words.
- Intuitive "right" and "wrong" buttons for user feedback.
- Dynamic card flipping to reveal English translations.
- Progress tracking with words to learn stored in a CSV file.

## Prerequisites

- Python 3.x
- pandas library (`pip install pandas`)

## Getting Started

1. Clone the repository:

    ```bash
    git clone https://github.com/nikhiltelase17/Flash-card-app.git
    cd flapy
    ```

2. Install dependencies:

    ```bash
    pip install pandas
    ```

3. Run the application:

    ```bash
    python flapy.py
    ```

## Usage

- The app displays French words on the front of the flashcard.
- Click the "right" button if you know the English translation.
- Click the "wrong" button if you need more practice.
- The app dynamically flips cards, revealing the correct English translation.
- Progress is tracked, and words to learn are saved in the `data/words_to_learn.csv` file.

## Acknowledgments

- French words data source: `data/french_words.csv`
- Flashcard images: `images/card_front.png`, `images/card_back.png`
- Icons: `images/right.png`, `images/wrong.png`

## Contributing

Feel free to contribute to Flapy by opening issues, providing feedback, or submitting pull requests. Let's make language learning fun and interactive together!

---

Feel free to customize the README further based on additional information or specific details you'd like to include.
