from manim import config as global_config
config = global_config.copy()

def transform_coor(x, y):
    x, y = float(x), float(y)
    # Scale factor for reducing coordinate space down to manim dimensions
    original_width = 3840
    original_height = 2160
   
    manim_height = config.frame_height
    manim_width = config.frame_width + 5
    # Scale the coordinates from the original system to the Manim system
    scaled_x = (x / original_width) * manim_width
    scaled_y = (y / original_height) * manim_height
    
    # Translate the coordinates to Manim's center-origin coordinate system
    # Subtract half of Manim's width/height from the scaled coordinates to shift the origin to the center
    translated_x = scaled_x - manim_width / 2
    translated_y = scaled_y - manim_height / 2
    translated_y = -translated_y

    return translated_x, translated_y