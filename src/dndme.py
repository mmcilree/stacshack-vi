from src.imagemeasure import initial_form, measurement_picker
from src.monsters import monstercomparison, displayhtml
from src.statgen import statGenerator

name = initial_form.survey()
front_path = initial_form.select_front_image()
side_path = initial_form.select_side_image()

measurement_picker.make_measurements(front_path, side_path, name)

#name = "Matthew"
stats = statGenerator.genStats(name)
monstercomparison.make(name, stats[0], stats[1], stats[2], stats[3], stats[4], stats[5])
result = initial_form.complete()

if result:
    displayhtml.showstatblock(name)
