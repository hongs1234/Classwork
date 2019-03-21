import arcade


WIDTH = 640
HEIGHT = 480

x = 50
y = 200

def setup():
    arcade.open_window(WIDTH, HEIGHT, "My Arcade Game")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(update, 1/80)

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = draw
    window.on_key_press = on_key_press
    window.on_key_release = on_key_release

    arcade.run()


def update(delta_time):
    global x
    global y

    x = x + 1
    if x > 680:
        x = -40


def draw():
    arcade.start_render()
    global x
    global y

    arcade.draw_circle_filled(x, y, 40, arcade.color.RED)


def on_key_press(key, modifiers):
    pass


def on_key_release(key, modifiers):
    pass


def on_mouse_press(x, y, button, modifiers):
    pass


if __name__ == '__main__':
    setup()