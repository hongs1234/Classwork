import arcade


WIDTH = 640
HEIGHT = 480

x = 200
y = 200

max_health = 100
bar_width = 200
player_health = 100

def update(delta_time):
    pass




def on_draw():
    arcade.start_render()

    global max_health
    global bar_width
    global player_health
    global x
    global y

    # DRAW IN HERE


    arcade.draw_xywh_rectangle_filled(x, y, bar_width, 50, arcade.color.BLACK)
    arcade.draw_xywh_rectangle_filled(x, y, player_health, 50, arcade.color.GREEN)



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