import arcade


WIDTH = 640
HEIGHT = 480

player_health = 100
max_health = 350
bar_width = 200
bar_height = 50


def update(delta_time):
    pass




def on_draw():
    arcade.start_render()

    global player_health

    # DRAW IN HERE

    arcade.draw_xywh_rectangle_filled(WIDTH/2 - bar_width/2, HEIGHT/2 - bar_height/2, bar_width, 50, arcade.color.BLACK)


    health_width = player_health / max_health * bar_width
    arcade.draw_xywh_rectangle_filled(WIDTH/2 - bar_width/2, HEIGHT/2 - bar_height/2, health_width, 50, arcade.color.GREEN)

    arcade.draw_text(f"{player_health} / {max_health}", WIDTH/2 - bar_width/2, HEIGHT/2 - bar_height/2, arcade.color.WHITE, font_size=30)




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