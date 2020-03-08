from src.imagemeasure import initial_form, measurement_picker
from src.monsters import monstercomparison, displaystacblockhtml
from src.statgen import statGenerator
from src.quiz import displayquizhtml, quizform

result = initial_form.quizmessage()
#displayquizhtml.showquiz()
if result:
    quizform.display()





