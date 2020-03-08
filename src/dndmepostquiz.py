from src.imagemeasure import initial_form, measurement_picker
from src.monsters import monstercomparison, displaystacblockhtml
from src.statgen import statGenerator

def postQuiz():
    name = initial_form.survey()
    front_path = initial_form.select_front_image()
    side_path = initial_form.select_side_image()
    initial_form.frontmessage()
    new_name = measurement_picker.make_measurements(front_path, side_path, name)
    stats = statGenerator.genStats(name)
    monstercomparison.make(new_name, stats[0], stats[1], stats[2], stats[3], stats[4], stats[5])
    result = initial_form.complete()
    if result:
        displaystacblockhtml.showstatblock(new_name)