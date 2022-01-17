def draw_bunches(point_start, angle_start, length_start):
    if length_start < 5:
        return
    angle_list = (-30, 30)
    for angle_delta in angle_list:
        angle_random = sd.random_number(-12, 12)
        angle = angle_start + angle_delta + angle_random
        # print(angle_random)
        point_end_f = sd.get_vector(point_start, angle, length_start).end_point
        sd.line(start_point=point_start, end_point=point_end_f, color=sd.COLOR_YELLOW, width=1)
        length_random = sd.random_number(-15, 15) / 100
        # print(length_random)
        draw_bunches(point_end_f, angle, length_start * (.75 + length_random))


angle_root = 90
length_root = 100
point_root = sd.get_point(300, 0)
point_end = sd.get_vector(point_root, angle_root, length_root/2).end_point
sd.line(start_point=point_root, end_point=point_end, color=sd.COLOR_YELLOW, width=1)
draw_bunches(point_end, angle_root, length_root)

sd.pause()
