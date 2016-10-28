import sys
from PySide import QtGui
from view import Ui_MyGame


_MAX_BUTTONS = 15


class Controller:
    """
    Handles the behavioural part of the game it also
    sets up the connections for each button.
    """

    def __init__(self, model, view):
        if not isinstance(view, Ui_MyGame):
            raise TypeError()
        self.__view = view
        self.__model = model

        self.__buttons = self.__get_all_buttons()
        self.__setup_connections()
        self.__setup_buttons()
        self.__update_lables()

    def __get_all_buttons(self):
        """
        Returns all buttons of the view, this is rather,
        this assumes that the name of every used control button is in the
        form bN where N is a integer in the range 0 to _MAX_BUTTONS
        :return: a button list.
        """
        arr = []
        for i in range(_MAX_BUTTONS):
            attr = "b{0}".format(i)
            btn = getattr(self.__view, attr)
            if not isinstance(btn, QtGui.QAbstractButton):
                raise TypeError()
            arr.append(btn)
        return arr

    def __setup_connections(self):
        """
        sets up the connections for every used button.
        :returns: None
        """
        self.__view.b_new_game.clicked.connect(self.__new_game_clicked)
        self.__view.b_end.clicked.connect(self.__end_button_clicked)
        for b in self.__buttons:
            b.clicked.connect(lambda b=b: self.__button_clicked(b))  # b=b to overcome late-binding issues

    def __new_game_clicked(self):
        """
        Fires when the new game button is clicked, resets the scores
        and increments the games_played variable.
        :return: None
        """
        self.__model.games += 1
        self.__model.last_clicked_button = 0
        self.__model.open = _MAX_BUTTONS
        self.__model.correct = 0
        self.__model.wrong = 0

        for b in self.__buttons:
            b.setEnabled(True)

        self.__update_lables()
        self.__setup_buttons()

    def __end_button_clicked(self):
        """
        Fires when the end button is clicked.
        :return: None
        """
        sys.exit(0)

    def __button_clicked(self, button):
        """
        Fires when any of the default 15 buttons in the middle panel is clicked.
        Performs some checks and inc/decrements some variables.
        :param button: the clicked button, the text value of the button MUST BE an integer.
        :return: None
        """
        clicked = int(button.text())
        if clicked == self.__model.last_clicked_button + 1:
            # pushed button was correct.
            button.setEnabled(False)
            self.__model.last_clicked_button += 1
            self.__model.correct += 1
            self.__model.open -= 1
        else:
            self.__model.wrong += 1
        self.__update_lables()

    def __update_lables(self):
        """
        Updates every label on the left panel
        :return: None
        """
        self.__view.v_open.setText(str(self.__model.open))
        self.__view.v_correct.setText(str(self.__model.correct))
        self.__view.v_games.setText(str(self.__model.games))
        self.__view.v_wrong.setText(str(self.__model.wrong))
        self.__view.v_total.setText(str(self.__model.wrong + self.__model.correct))

    def __setup_buttons(self):
        """
        Assigns random numbers to every button as it's text property
        :return: None
        """
        # randomize buttons
        options = list(range(1, len(self.__buttons) + 1))
        for btn in self.__buttons:
            rn = self.__model.rng.randint(0, len(options) - 1)
            pick = options.pop(rn)
            btn.setText(str(pick))



