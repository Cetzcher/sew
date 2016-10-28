from random import Random


class Model:
    """
    The model of the GUI
    """


    def __init__(self):
        self.rng = Random()

        self.last_clicked_button = 0
        self.open = 15
        self.correct = 0
        self.wrong = 0
        self.games = 1
        # total = correct + wrong
