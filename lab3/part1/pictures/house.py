import simple_draw as sd
#import wall
#from pictures import wall
sd.resolution = (1000, 800)
start = sd.get_point(x=300, y=10)
size_paint = (480, 240)
wall_size = (400, 400)
brick_sizer_x = 40
brick_sizer_y = 20

half_brick = brick_sizer_x // 2


def paint_wall(pos_x=0, pos_y=0):
    brick_x_count = wall_size[0] // brick_sizer_x  # sd.resolution[0] // x
    brick_y_count = wall_size[1] // brick_sizer_y  # sd.resolution[1] // y
    x_count = brick_x_count
    start_x = pos_x
    start_y = pos_y
    for brick_y in range(brick_y_count):
        end_x = start_x + brick_sizer_x
        end_y = start_y + brick_sizer_y
        if brick_y % 2 == 1:
            x_count += 1
        else:
            x_count = brick_x_count
        for brick_x in range(x_count):
            if brick_y % 2 == 1:
                if brick_x == 0:
                    start_position = sd.get_point(start_x, start_y)
                    end_position = sd.get_point(end_x-half_brick, end_y)
                elif brick_x == x_count-1:
                    start_position = sd.get_point(start_x-half_brick, start_y)
                    end_position = sd.get_point(end_x - brick_sizer_x, end_y)
                else:
                    start_position = sd.get_point(start_x-half_brick, start_y)
                    end_position = sd.get_point(end_x-half_brick, end_y)
            else:
                start_position = sd.get_point(start_x, start_y)
                end_position = sd.get_point(end_x, end_y)
            sd.rectangle(left_bottom=start_position, right_top=end_position, color=sd.COLOR_DARK_BLUE, width=0)
            sd.rectangle(left_bottom=start_position, right_top=end_position, color=sd.COLOR_BLACK, width=1)
            start_x += brick_sizer_x
            end_x += brick_sizer_x
        start_x = pos_x
        start_y = end_y
        end_y += brick_sizer_y
wall_size = size_paint
point_list_draw = [sd.get_point(start.x+1,
                            start.y+1 + size_paint[1]),
                            sd.get_point
                            (start.x+1 + size_paint[0] // 2,
                            start.y+1 + size_paint[1] + size_paint[1]),
                            sd.get_point
                            (start.x+1 + size_paint[0],
                            start.y+1 + size_paint[1]),
                            ]


def draw_house():

    paint_wall(start.x, start.y)
    sd.polygon(point_list = point_list_draw, color = sd.COLOR_PURPLE, width = 1)
    sd.polygon(point_list = point_list_draw, color=sd.COLOR_BLACK, width=1)
    step_1=size_paint[0] // 4
    step_2=size_paint[1]//5
    sd.rectangle(sd.get_point(start.x+1 + step_1, start.y+1 + step_2),
                 sd.get_point(start.x+1 + size_paint[0] - step_1,
                              start.y+1 + size_paint[1] - step_2),
                 color=sd.COLOR_YELLOW, width=0)

    sd.rectangle(sd.get_point(start.x+1 + step_1, start.y+1 + step_2),
                 sd.get_point(start.x+1 + size_paint[0] - step_1,
                              start.y+1 + size_paint[1] - step_2),
                 color=sd.COLOR_BLACK, width=3)

draw_house()
sd.pause()
