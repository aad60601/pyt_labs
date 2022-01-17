def triangle(point, angle, length):
    for _ in range(3):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        angle = angle + 120
        point = v1.end_point


def square(point, angle, length):
    for _ in range(4):
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        angle = angle + 90
        point = v1.end_point

def pentagon(point, angle, length):
    for count in range(4):
        count += 1
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        if count == 1:
            v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        if count == 4:
            sd.line(start_point=v1.end_point, end_point=v2.start_point, width=3)
        angle = angle + 70
        point = v1.end_point

def hexagon(point, angle, length):
    for count in range(5):
        count += 1
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw()
        if count == 1:
            v2 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        if count == 5:
            sd.line(start_point=v1.end_point, end_point=v2.start_point, width=3)
        angle = angle + 60
        point = v1.end_point

point_triangle = sd.get_point(100, 100)
triangle(point=point_triangle, angle=50, length=150)

point_square = sd.get_point(400, 100)
square(point=point_square, angle=20, length=150)

point_pentagon = sd.get_point(100, 350)
pentagon(point=point_pentagon, angle=20, length=100)

point_hexagon = sd.get_point(400, 350)
hexagon(point=point_hexagon, angle=20, length=100)

sd.pause()

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!
def vector(vector_start, length, angle):
    v = sd.get_vector(vector_start, angle, length)
    return v.end_point


def polygon(point, heads, length):
    angle = 0
    angle_start = 15
    angle_polygon = 360 / heads
    point_polygon = point
    for _ in range(heads):
        if _ == 0:
            angle = angle_start
        else:
            angle += angle_polygon
        if _ < (heads - 1):
            end_point = vector(point, length, angle)
        else:
            end_point = point_polygon
        sd.line(start_point=point, end_point=end_point, color=sd.COLOR_YELLOW, width=1)
        point = end_point
        # t2 = sd.get_vector(t1.end_point, angle + 120, length, 5)
        # sd.line(start_point=t1.end_point, end_point=t2.end_point, color=sd.COLOR_YELLOW, width=1)
        # sd.line(start_point=t2.end_point, end_point=point, color=sd.COLOR_YELLOW, width=1)


# (point_start_x, point_start_y, length_start, type_of_polygon)
start_point = [(100, 100, 150, 3), (350, 100, 150, 4), (100, 350, 100, 5), (350, 350, 100, 6)]

for _ in start_point:
    point_start = sd.get_point(_[0], _[1])
    length_start = _[2]
    heads_start = _[3]
    polygon(point_start, heads_start, length_start)
sd.pause()
