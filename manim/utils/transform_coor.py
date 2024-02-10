def transform_coor(x, y):
    # Scale factor for reducing coordinate space down to manim dimensions
    original_width = 3840
    original_height = 2160
    manim_width = 8
    manim_height = 14.222222222222221
    # Scale the coordinates from the original system to the Manim system
    scaled_x = (x / original_width) * manim_width
    scaled_y = (y / original_height) * manim_height
    
    # Translate the coordinates to Manim's center-origin coordinate system
    # Subtract half of Manim's width/height from the scaled coordinates to shift the origin to the center
    translated_x = scaled_x - manim_width / 2
    translated_y = scaled_y - manim_height / 2

    return translated_x, translated_y