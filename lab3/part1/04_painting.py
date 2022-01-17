import simple_draw as sd
import pictures
from pictures import tree
from pictures import house
from pictures import men
from pictures import snow

sd.resolution = (1200,800)
snow.snowflakes_count = 60
snow_falling = True
snowflakes = {}
snowflakes_remove = {}
tick = 0
house.start = sd.get_point(x = 300, y = 10)
house.size_paint = (480, 240)
house.point_list_draw = [sd.get_point
                               (house.start.x+1,
                                house.start.y+1 + house.size_paint[1]),
                                sd.get_point
                                (house.start.x+1 + house.size_paint[0] // 2,
                                house.start.y+1 + house.size_paint[1] + house.size_paint[1]),
                                sd.get_point
                               (house.start.x+1 + house.size_paint[0],
                                house.start.y+1 + house.size_paint[1]),
                               ]
root_point = ((sd.get_point(950, 10), house.size_paint[1] / 2 - sd.random_number(10, 30)),
              (sd.get_point(200, 20),  house.size_paint[1] / 2 - sd.random_number(10, 30)))
rainbow.draw_rainbow(500,-100)
#snow.draw_snow(0, 0)
tree.draw_tree(point=root_point[1][0], angle=90, length=root_point[1][1])
house.draw_house()
snow.draw_snowflake(house.point_list_draw, falling=snow_falling)
men.draw_smile(house.start.x + 1 + house.size_paint[0] // 2,
                        house.start.y + 1 + house.size_paint[1] // 2)
sd.sleep(0.03)

tick += 1
sd.finish_drawing()

if sd.user_want_exit():
    break
sd.pause()
