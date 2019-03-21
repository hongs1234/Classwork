import arcade

WIDTH = 640
HEIGHT = 480

arcade.open_window(WIDTH, HEIGHT, "My Drawing")
arcade.set_background_color(arcade.color.BLUE_YONDER)

arcade.start_render()
# Begin drawing

#Sun
arcade.draw_circle_filled(540, 380, 50, arcade.color.YELLOW)

#Grass
arcade.draw_xywh_rectangle_filled(0, 0, 640, 100, arcade.color.GREEN)

#Left Tree
arcade.draw_xywh_rectangle_filled(515, 75, 20, 75, arcade.color.BROWN)
arcade.draw_triangle_filled(485, 150, 525, 225, 565, 150, arcade.color.DARK_GREEN)

#Middle Tree
arcade.draw_xywh_rectangle_filled(440, 75, 20, 75, arcade.color.BROWN)
arcade.draw_triangle_filled(410, 150, 450, 225, 490, 150, arcade.color.DARK_GREEN)

#Right Tree
arcade.draw_xywh_rectangle_filled(190, 75, 20, 75, arcade.color.BROWN)
arcade.draw_triangle_filled(160, 150, 200, 225, 240, 150, arcade.color.DARK_GREEN)

# End drawing
arcade.finish_render()
arcade.run()
