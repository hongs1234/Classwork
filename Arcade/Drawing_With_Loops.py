import arcade


WIDTH = 640
HEIGHT = 480

x = 70
y = 0


def update(delta_time):
    pass




def on_draw():
    arcade.start_render()

    global x
    global y

    # Draw in here...

    for x in range(30, WIDTH, 80):
        for y in range(0, WIDTH, 160):
            arcade.draw_xywh_rectangle_filled(x, y, 10, 50, arcade.color.BROWN)
            arcade.draw_triangle_filled(x - 20, y + 50, x + 5, y + 150, x + 30, y + 50, arcade.color.GREEN)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/60)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


if __name__ == '__main__':
    setup()