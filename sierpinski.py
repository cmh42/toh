#!/usr/bin/env python

import sys, pygame

def make_sierpinski(depth, triangle, triangle_list):
    '''
    Function inputs: depth (of recursion), triangle (vertex coordinates)
    triangle_list (list of triange coordinates)
    Modifies triangle_list: all the depth 1 (bottom) triangles are added 
    to this list (using recursion relative to the input triangle)
    '''
    (x0,y0) = triangle[0]
    (x1,y1) = triangle[1]
    (x2,y2) = triangle[2]
    # Maximum depth reached (going down) so add this triangle to the list
    if depth == 1:
        triangle_list.append(triangle)
        return None 
    # Otherwise split triangle into three sub triangles
    midpoint_A = (x0 + (x1-x0)/2.0, y0)
    midpoint_B = (x0 + (x2-x0)/2.0, y2 + (y0-y2)/2.0)
    midpoint_C = (x2 + (x1-x2)/2.0, y2 + (y1-y2)/2.0)
    # First triangle, recursive call on it
    new_triangle = ((x0,y0), midpoint_A, midpoint_B)
    make_sierpinski(depth-1, new_triangle, triangle_list)
    # Second triangle, recursive call on it
    new_triangle = (midpoint_A, (x1,y1), midpoint_C)
    make_sierpinski(depth-1,new_triangle,triangle_list)
    # Third triangle, recursive call on it
    new_triangle = (midpoint_B, midpoint_C, (x2,y2))
    make_sierpinski(depth-1, new_triangle, triangle_list)    
    # No need for a return statement (personal preference) 
    return None

def get_command_line_input(min_depth, max_depth, default_depth):
    '''
    Gets depth as command line input. If no command line input 
    given or this is of the wrong type or outside the interval 
    [min_depth, max_depth] then default depth is returned. 
    Otherwise the value given on the command line is returned. 
    '''
    try:
        assert len(sys.argv) == 2
        depth = int(sys.argv[1])
        assert depth >=  min_depth  and depth <= max_depth
        print("\nUsing depth that you input:  {}".format(depth))
    except:
        depth = default_depth
        print("\nNo argument given,", end = " ")
        print("or out of range [{},{}].".format(min_depth,max_depth), end = " ")
        print(" Using default depth: {}".format(depth))
    return depth 


def make_sierpinski_caption():
    '''
    Function that makes title and instructions for the animation.
    This will be put in title bar of the animation.
    '''
    caption = 'Sierpinski Triangle            '
    caption += '(1)  \'Space\' to start or pause    '
    caption += '(2)  Further keystroke instruction here?'
    return caption

def sierpinski_main():
    '''
    Function that draws the Sierpinski triangle as an animation. 
    The depth of the triangle (recursion) can be adjusted by entering 
    a depth integer value (in [1,10]) on the command line. 
    For example: python sierpinski.py 8 
    '''
    
    dimensions = (900, 862)
    backgroundColour = (255,255,255)
    blue, black = (0,0,255), (0,0,0)
    # This is the overall outline triangle
    master_triangle = ((50,800),(850,800),(450,62))
    min_depth, max_depth = 1, 10
    default_depth = 6
    speed_factor = 4
    clock = pygame.time.Clock()
    
    # The depth is input from command line
    # Default used if no command line input or input out of range
    depth = get_command_line_input(min_depth,max_depth,default_depth)

    # Defines the speed of the animation (see the animation loop) 
    frames_per_second = 20  + 10 * speed_factor
    # Make a list of all the triangle vertex coordinates of the given 
    # depth (in make_sierpinski we process  depth to work down to 1)
    triangle_list = []
    make_sierpinski(depth,master_triangle,triangle_list)

    # Initialise pygame and the screen display object and title
    pygame.init()
    screen = pygame.display.set_mode(dimensions)
    caption = make_sierpinski_caption()
    pygame.display.set_caption(caption)

    # Initialise the display 
    screen.fill(backgroundColour)
    pygame.display.flip()

    # Total number of triangles to be drawn 
    number_of_triangles = len(triangle_list)
    index = 0
    draw_triangle = False
    keep_running = True

    # Animation loop 
    while keep_running:
        for event in pygame.event.get():
            # Exit (at end of this iteration) using quit (e.g Ctrl-q or red button)
            if event.type == pygame.QUIT:
                keep_running = False
            # Start and pause the animation with the space key 
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                draw_triangle  = not draw_triangle 

        # Draw next triangle with index 'index' if not told to pause and not complete
        if draw_triangle and index  < number_of_triangles:
            pygame.draw.polygon(screen, black, triangle_list[index], 1)
            # Now update so that latest triangle is added 
            pygame.display.update()
            # Pause time before next iteration starts: one clock tick  
            clock.tick(frames_per_second)
            # Index uptate: index walks through triangle_list indices
            index += 1
            
    pygame.quit()
    return None
                  
if __name__ == '__main__':
    sierpinski_main()
