from random import Random


class Model:



    def __init__(self):
        """
        The model of the GUI.
        Contains all relevant data and a random number
        generator.

        relevant data: 1) open => how many fields are still open  default 15
        2) correct => how many buttons were pressed in the correct order.
        3) wrong => how many buttons were pressed in the wrong order.
        the total amount is calculated by adding correct and wrong together.
        4) games => the total number of games played.
        initializes the default values of the 4 above values
        """
        self.rng = Random()

        self.last_clicked_button = 0
        self.open = 15
        self.correct = 0
        self.wrong = 0
        self.games = 1
        # total = correct + wrong
