import simple_draw as sd
def draw_rainbow(x,y):
    rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)
    step = 0
    for color in rainbow_colors:
        start_point = sd.get_point(x-step, y)
        end_point = sd.get_point(x-step, y)
        sd.line(start_point=start_point, end_point=end_point, color=color, width=4)
        step += 5
sd.pause()
