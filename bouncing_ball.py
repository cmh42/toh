#!/usr/bin/env python
"""
Module name: bouncing_ball.py 
Module contains: get_command_line_input, bouncing_ball_main
Author: Charles 21 February 2021
"""


import sys, pygame, random 
import numpy as np

def get_command_line_input(min_vel_factor, max_vel_factor):
    '''
    Gets speed factor as command line input. If no command line input 
    given or this is of the wrong type or outside the interval 
    [min_vel_factor, max_vel_factor] then None is returned. Otherwise the 
    value give on the command line is returned. 
    '''
    try:
        assert len(sys.argv) == 2
        vel_factor = int(sys.argv[1])
        assert vel_factor >=  min_vel_factor and vel_factor<= max_vel_factor 
        return  vel_factor
    except:
        return None 
        


    

def bouncing_ball_main():
    '''
    Function simulating simple bouncing ball within a rectangular 
    room. Speed of ball can be adjusted by entering a speed factor 
    on the command line (e.g. python bouncing_ball 3 to use speed 
    factor 3 
    '''
    
    # Randomised x direction 
    x_direction = random.choice([-1,1])
    # Slightly randomised step sizes for x, y directions to vary simulations
    x_step, y_step =  x_direction*random.randint(8,10), -random.randint(8,10)
    min_speed_factor, max_speed_factor  = 1, 10
    default_speed_factor = 5
    screen_size = (screen_width, screen_height) = (800, 600)
    white = (255,255,255)
    ball_size = 30
    x0, y0 = (screen_width - ball_size)/2, screen_height - ball_size

    # The ball will start using speed_factor given from command line (or default used)
    speed_factor = get_command_line_input(min_speed_factor,max_speed_factor)
    # Case when no command line input given, or input was erroneous
    if speed_factor is None:
        speed_factor = default_speed_factor
        print("\nNo argument given,", end = " ")
        print("or out of range [{},{}].".format(min_speed_factor,max_speed_factor), end = " ")
        print(" Using default speed factor: {}".format(speed_factor))
    # Case when speed_factor of correct type given on command line 
    else:
        print("\nUsing speed factor that you input:  {}".format(speed_factor))

    # For information for user 
    print("The forward horizontal step size is  x_step = {}".format(x_step))
    print("The forward vertical step size is    y_step = {}".format(y_step))

    # Used for the pause time in the animation while loop below
    frames_per_second = 10 + 10*speed_factor
    clock = pygame.time.Clock()

    # Set up the animation     
    pygame.init()
    screen = pygame.display.set_mode(screen_size)
    # Put the title and instructions for the animation in the title bar of the animation.
    caption = 'Bouncing Ball'
    caption += '                              '
    caption += '(Keystroke:  \'Space\' to start or pause)'
    pygame.display.set_caption(caption)
    # We use an image file for the ball: must be in present working folder
    ball = pygame.image.load("intro_ball.gif")
    # We resize the image object 'ball'
    ball = pygame.transform.scale(ball, (ball_size, ball_size))
    # The rectangle ball_rect is used for displaying the ball where (x0, y0)
    # is the top left hand corner of the rectangle (and length of sides given) 
    ball_rect = pygame.Rect(x0,y0,ball_size,ball_size)

    # Ball is motionless to start with 
    screen.fill(white)
    # Overlay the ball image on screen 
    screen.blit(ball, ball_rect)
    # Now re-initialise the display (to show the ball etc.) 
    pygame.display.flip()

    # We keep going for ever in this program (until quit is input - e.g. Ctrl-Q - by user ).
    keep_running = True
    # Use the following  as switch to move the ball or not using the space bar.
    move_ball = False

    # Animation loop 
    while keep_running:
        # If a keyboard event happens register it... 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                keep_running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                move_ball = not move_ball
                
        # Pressing the space bar changes the value of move_ball (see elif above)
        # So you can toggle move/not move with the space bar
        if move_ball:
            # Move the ball a step 
            ball_rect.x += x_step
            ball_rect.y += y_step
            # Alternatively use use the following line 
            # ball_rect = ball_rect.move((x_step,y_step))
            # The ball bounces when it hits an edge
            if ball_rect.left < 0 or ball_rect.right > screen_width:
                x_step = - x_step
            if ball_rect.top < 0 or ball_rect.bottom > screen_height:
                y_step = - y_step

        # Redraw the screen 
        screen.fill(white)
        # Redraw the ball 
        screen.blit(ball, ball_rect)
        # Re-initialise the display t
        pygame.display.flip()
        # Wait a clock tick until starting next iteration of animation loop
        clock.tick(frames_per_second)

        
    pygame.quit()
    return None 
                
if __name__ == '__main__': 
    bouncing_ball_main()



