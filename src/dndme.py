from src.imagemeasure import initial_form, measurement_picker
from src.monsters import monstercomparison

name = initial_form.survey()
front_path = initial_form.select_front_image()
side_path = initial_form.select_side_image()
measurement_picker.make_measurements(front_path, side_path, name)

monstercomparison.makeMonster()
