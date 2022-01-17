import simple_draw as sd
smile_size = 40
smile_color = sd.COLOR_BLACK
oculus_color = sd.COLOR_WHITE
beard_color = sd.COLOR_BLACK

eyeball_radius = round(smile_size * 0.3)
eye_radius = round(smile_size * 0.1)
oculus_radius = eyeball_radius + 1
def draw_smile(x, y):

    #body_list_point = (sd.get_point(x - smile_size*1.5, y - smile_size*1.5),
                       #sd.get_point(x  - smile_size*1.5, y - smile_size*1.55),
                       #sd.get_point(x - smile_size*1.5, y-smile_size*1.5),
                      # sd.get_point(x-smile_size//2, y-smile_size//2))
    #sd.polygon(body_list_point, sd.COLOR_BLACK, width=0)
    face_point = sd.get_point(x=x, y=y)
    sd.circle(center_position=face_point, radius=smile_size, color=smile_color, width=0)
    oculus_distance = eyeball_radius * 1.3
    right_oculus_point = sd.get_point(x=x+oculus_distance, y=y+oculus_distance)
    left_oculus_point = sd.get_point(x=x-oculus_distance, y=y+oculus_distance)
    sd.circle(center_position=right_oculus_point, radius=eyeball_radius, color=oculus_color, width=0)
    sd.circle(center_position=left_oculus_point, radius=eyeball_radius, color=oculus_color, width=0)
    right_eye_point = sd.get_point(x=x+oculus_distance, y=y+oculus_distance)
    left_eye_point = sd.get_point(x=x-oculus_distance, y=y+oculus_distance)
    sd.circle(center_position=right_eye_point, radius=eye_radius, color=sd.COLOR_BLUE, width=0)
    sd.circle(center_position=left_eye_point, radius=eye_radius, color=sd.COLOR_BLUE, width=0)
    step = smile_size // 10
    smile_step = smile_size // 10
    smile_y_pos = y-3
    smile_length = (smile_size - round(smile_size * (6 / 7)))

    for i in range(x-smile_length-2, x+smile_length+2, step):

        if i < x:
            smile_step += step
        else:
            smile_step -= step

        point_start = sd.get_point(i, smile_y_pos-smile_length)
        point_end = sd.get_point(i, smile_y_pos-smile_length-smile_step)
        sd.line(point_start, point_end, sd.COLOR_RED, width=step)
start_point = sd.get_point(300, 300)
draw_smile(start_point.x, start_point.y)
sd.pause()
