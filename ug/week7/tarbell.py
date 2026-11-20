from py5canvas import *

"""
TASK
- Run the code and observe the behaviour
- Alter the code so that there is an array of three streets moving in random directions at the start
- Alter the code of Street so that street holds an array of streets. Add multiple calls to spawnStreet
- Adapt spawnStreet to allow streets to spawn to the left and the right
- Experiment with adjusting minMag, magThresh. How does it change the pattern ?
- Experiment with adjusting the angle of rotation away from 90 degrees.
"""

class Street:
    def __init__(self, x, y, direction):
        self.mag = 0  # the length of the current street
        self.pos = vector(x, y) #same as np.array([x, y])
        self.direction = direction
        self.is_moving = True
        self.streets = []
        self.id = id_count[0] + 1  # a unique id for each street
        id_count[0] = self.id

    def move(self):
        if self.is_moving:
            self.pos += self.direction
            x = round(self.pos[0])
            y = round(self.pos[1])

            if x >= width or y >= height or x < 0 or y < 0:
                # check if the street is out of bounds
                self.is_moving = False
                print('out of bounds')
            elif (id_grid[x][y] > 0 and 
                  id_grid[x][y] != self.id and 
                  self.mag > mag_thresh):
                # check if the street is on an occupied cell
                self.is_moving = False
                print('occupied cell')
            else:
                id_grid[x][y] = self.id  # register the id in the cell
                self.mag += 1  # increase the length

                stroke(0)  # random(0, 200)) #a bit of tarbellesque shading
                point(self.pos[0], self.pos[1])

            if not self.is_moving:
                if self.mag > min_mag:
                    self.streets.append(self.spawn_street(90))
                    self.streets.append(self.spawn_street(-90))

        if self.streets:
            for street in self.streets:
                street.move()

    def spawn_street(self, angle):
        # this function creates a new street starting at some point along the current street and sets its direction to a perpendicular
        d = floor(random(self.mag * 0.05, self.mag * 0.95))

        # new tip
        x = self.pos[0] - self.direction[0] * d
        y = self.pos[1] - self.direction[1] * d

        dir_vec = self.direction.copy()
        # Rotate by angle (convert to radians)
        angle_rad = radians(angle)
        new_x = dir_vec[0] * cos(angle_rad) - dir_vec[1] * sin(angle_rad)
        new_y = dir_vec[0] * sin(angle_rad) + dir_vec[1] * cos(angle_rad)
        dir_vec = vector(new_x, new_y)
        
        return Street(x, y, dir_vec)

# Global variables
streets = []
id_grid = []
id_count = [0]
min_mag = 20
mag_thresh = 0

def setup():
    create_canvas(512, 512)
    
    global min_mag, mag_thresh, streets, id_grid, id_count
    
    # Initialize id_grid
    for i in range(width):
        id_grid.append([])  # columns
        for j in range(height):
            id_grid[i].append(False)  # rows

    # Start with three streets in random directions
    for _ in range(3):
        angle = random(TWO_PI)
        streets.append(Street(
            random(width * 0.1, width * 0.9),
            random(height * 0.1, height * 0.9),
            vector(cos(angle), sin(angle))
        ))

    background(255)
    stroke(0)

def draw():
    for rep in range(5):  # increase to draw faster
        for street in streets:
            street.move()

run()
