import arcade


WIDTH = 640
HEIGHT = 480

x = 325
y = 300
radius = 100

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.WHITE)

arcade.start_render()
# Begin drawing

arcade.draw_circle_filled(x, y, radius, arcade.color.ALIZARIN_CRIMSON)

# End drawing
arcade.finish_render()
arcade.run()

