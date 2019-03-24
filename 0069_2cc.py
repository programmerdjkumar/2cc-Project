import random
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QInputDialog, QLabel, QWidget, QPushButton, QAction, QLineEdit, QMessageBox, QInputDialog, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def choose(): 
    words = ['naruto', 'bleach', 'helsing', 'gintama', 'berserk', 'clannad', 'haikyuu', 'dragonball', 'mushishi', 'monster',
             'beelzebub', 'toriko', 'hyouka', 'noblesse', 'gamer', 'boruto', 'blame', 'horimiya', 'gantz', 'senyuu',
             'nisekoi', 'gosick', 'danganronpa', 'stride', 'bakuman', 'parasyte', 'avatar', 'ajin', 'pokemon', 'inuyasha'] 
    pick = random.choice(words)
    return pick
def jumble(word): 
    random_word = random.sample(word, len(word)) 
    jumbled = ''.join(random_word) 
    return jumbled
class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Jumble Game'
        self.left = 10
        self.top = 10
        self.width = 450
        self.height = 220
        self.initUI() 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.play()
        self.show()
    def play(self):
        player_score = 0
        turn = 0
        while turn < 10:
            picked_word = choose()
            question = jumble(picked_word)
            QMessageBox.question(self, 'Jumble Game', "Question: " + question, QMessageBox.Ok, QMessageBox.Ok)
            answer, okPressed = QInputDialog.getText(self, "Get text","Type your guess:", QLineEdit.Normal, "")
            if answer == picked_word:
                QMessageBox.question(self, 'Result', "+1 Score!", QMessageBox.Ok, QMessageBox.Ok)
                player_score += 1
            else:
                QMessageBox.question(self, 'Result', "Oops! It's " + picked_word, QMessageBox.Ok, QMessageBox.Ok)           
            turn += 1
        QMessageBox.question(self, 'Total Score', "Your Score: " + str(player_score), QMessageBox.Ok, QMessageBox.Ok)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_()) 

