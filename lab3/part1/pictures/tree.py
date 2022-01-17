import simple_draw as sd
sd.resolution = (1200, 800)

x = 1000
y = 30
root_point = sd.get_point(x, y)
root_angle = 90
root_color = (40, 40, 40)
def draw_tree(point, angle, length=100):
    if length < 10:
        return
    vector = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    vector.draw()
    next_point = vector.end_point
    delta = 30
    delta_deviation = delta * 0.4
    delta += sd.random_number(-delta_deviation, delta_deviation)
    length = length * 0.75
    length_deviation = round(length * 0.2)
    length += sd.random_number(0, length_deviation)
    length = round(length)
    next_angle = round(angle + delta)
    draw_tree(next_point, next_angle, length)
    next_angle = round(angle - delta)
    draw_tree(next_point, next_angle, length)
if __name__ == '__main__':
    root_point = sd.get_point(500, 30)
    draw_tree(point=root_point, angle=root_angle, length=50)
    sd.pause()
