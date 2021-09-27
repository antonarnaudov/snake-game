import config
from copy import deepcopy
import food

snake_pos = [[0, 0], [config.SCALE, 0], [config.SCALE*2, 0]]

# Set all snake images to None
snake_head_img = {
    'up': None, 
    'right': None,
    'down': None,
    'left': None
}

snake_body_img = {
    'up': None, 
    'right': None,
    'down': None,
    'left': None
}

snake_tail_img = {
    'up': None, 
    'right': None,
    'down': None,
    'left': None
}

snake_angle_img = {
    'up left': None,
    'up right': None,
    'down left': None,
    'down right': None
}


def show():
    # Draw the snake images
    image(snake_head_img[config.CURRENT_DIR], snake_pos[-1][0], snake_pos[-1][1], config.SCALE, config.SCALE)
        
    for segment in snake_pos[1:-1]:
        if segment[0] == snake_pos[-1][0] or segment[1] == snake_pos[-1][1]:
            image(snake_body_img[config.CURRENT_DIR], segment[0], segment[1], config.SCALE, config.SCALE)
            
        else:
            image(snake_body_img[config.CURRENT_DIR], segment[0], segment[1], config.SCALE, config.SCALE)
    
    if snake_pos[0][0] == snake_pos[-1][0] or snake_pos[0][1] == snake_pos[-1][1]:
        image(snake_tail_img[config.CURRENT_DIR], snake_pos[0][0], snake_pos[0][1], config.SCALE, config.SCALE)

    else:
        image(snake_tail_img[config.CURRENT_DIR], snake_pos[0][0], snake_pos[0][1], config.SCALE, config.SCALE)
    
    
def check_edges():
    head = snake_pos[-1]
    if head[1] < 0:
        head[1] = config.WINDOW_HEIGHT
    elif head[1] >= config.WINDOW_HEIGHT:
        head[1] = 0
    elif head[0] < 0:
        head[0] = config.WINDOW_WIDTH
    elif head[0] >= config.WINDOW_WIDTH:
        head[0] = 0
        

def move():
    current_changes = config.DIRECTIONS[config.CURRENT_DIR]
    
    snake_copy = deepcopy(snake_pos)
    snake_pos[-1][0] += current_changes[0]
    snake_pos[-1][1] += current_changes[1]
    
    for i in range(len(snake_pos) - 2, -1, -1):
        snake_pos[i] = snake_copy[i + 1]
        
    check_edges()
    

def touches_food():
    return snake_pos[-1] == food.food_pos


def eat_food():
    snake_pos.insert(0, snake_pos[0])
    
def eats_self():
    head = snake_pos[-1]
    return any(seg == head for seg in snake_pos[:-1])
