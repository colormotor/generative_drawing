"""
TASK
Replace the Face class with your own customized one
"""

from py5canvas import *
from slimgui import imgui

# ---------------- GLOBALS ----------------
population = []
population_size = 8
mutation_prob = 0.1
mating_pool = []


# ---------------- PARAMETERS (SLIDER UI) ----------------
def parameters():
    return {
        "Mutation Probability": (0.1, 0.0, 1.0),
        # You could add more, e.g. population size, but that would need re-init logic
    }


# ---------------- GUI (EVOLVE BUTTON) ----------------
def gui():
    if imgui.button("Evolve"):
        evolve()


# ---------------- SETUP / DRAW ----------------
def setup():
    global population, mating_pool, population_size, mutation_prob
    create_canvas(1200, 512)

    population_size = 8
    population = []
    mating_pool = []

    # Create initial population of faces
    # Expecting you to define a Face class with:
    # Face(x, y) having .draw(),  .dna, .calc_phenotype()
    for i in range(population_size):
        pad = 70
        x = remap(i, 0, population_size-1, pad, width - pad)
        y = height / 2
        population.append(Face(x, y))  # your Face class

    mutation_prob = 0.1
    text_align(CENTER)

def check_mouse_over(face):
    '''This function checks if the mouse is in close proximity of a face
        If it is, then it increases the fitness of this.DNA by 1'''
    d = dist(mouse_x, mouse_y, face.x, face.y)
    if d < face.width/2:
        face.dna.fitness += 5

def draw():
    global mutation_prob
    background(0)

    # read mutation probability from UI slider
    mutation_prob = params.mutation_probability

    # draw population and handle mouse-over fitness
    for indiv in population:
        indiv.draw()
        check_mouse_over(indiv)
        no_stroke()
        fill(255)
        text(f"fitness: {indiv.dna.fitness}", indiv.x, indiv.y+130)
    fill(255)


# ---------------- EVOLUTION LOGIC ----------------
def evolve():
    """
    Called when the Evolve button is pressed.
    Uses mating pool selection, crossover, and mutation to create a new generation.
    """
    random_seed(frame_count)

    update_mating_pool()

    for i in range(len(population)):
        parent_dna_a, parent_dna_b = select_parent_dna()
        crossed_dna = crossover_dna(parent_dna_a, parent_dna_b)

        # 1. mutate crossed_dna
        crossed_dna.mutate(params.mutation_probability)

        # 2. set this population member's DNA to crossed_dna
        population[i].dna = crossed_dna

        # 3. recalculate phenotype for this population member
        population[i].calc_phenotype()

def crossover_dna(parent_a, parent_b):
    """
    Given two DNA objects, create a new DNA object with genes selected
    randomly (50/50) from each parent.
    """
    num_genes = len(parent_a.genes)
    child = DNA(num_genes)

    for i in range(num_genes):
        if random() > 0.5:
            child.genes[i] = parent_a.genes[i]
        else:
            child.genes[i] = parent_b.genes[i]

    return child

def update_mating_pool():
    """
    - Creates a new empty mating pool.
    - Traverses the population and, for each population member's DNA,
      adds a number of DNA copies to the mating pool equal to the DNA's fitness.
    """
    global mating_pool
    mating_pool = []

    for indiv in population:
        # expects indiv.dna.fitness to be an integer >= 1
        for _ in range(indiv.dna.fitness):
            mating_pool.append(indiv.dna)


def select_parent_dna():
    """
    Selects two DNA instances from the mating pool at random and returns them as a tuple.
    """
    if len(mating_pool) == 0:
        # safeguard: if no fitness yet, just pick from population
        # (assuming each indiv has .dna)
        a = int(random(0, len(population)))
        b = int(random(0, len(population)))
        return population[a].dna, population[b].dna

    a = int(random(0, len(mating_pool)))
    b = int(random(0, len(mating_pool)))
    return mating_pool[a], mating_pool[b]



# ---------------- FACE CLASS ----------------

class Face:
    def __init__(self, x, y):
        # non-genetic properties
        self.x = x
        self.y = y

        # DNA: same number of genes as genetic properties
        self.dna = DNA(13)
        self.seed = random(99999, 999999)

        # these will be set in calc_phenotype
        self.facecol = color(255, 0, 0)
        self.haircol = color(0, 255, 0)

        # genetic properties (will be updated by calc_phenotype)
        self.width = None
        self.height = None
        self.face_distort = None
        self.eye_position_y = None
        self.eye_spread = None
        self.mouth_position_y = None
        self.mouth_open = None
        self.eye_size = None
        self.hair_length = None
        self.hair_variation = None
        self.hair_wave = None

        # express the genes when the face is created
        self.calc_phenotype()

    def calc_phenotype(self):
        # express each gene
        self.width = remap(self.dna.genes[0], 0, 1, 80, 200)
        self.height = remap(self.dna.genes[1], 0, 1, 80, 200)
        self.face_distort = remap(self.dna.genes[2], 0, 1, 0, 1)
        self.eye_position_y = remap(self.dna.genes[3], 0, 1, 0.05, 0.3)
        self.eye_spread = remap(self.dna.genes[4], 0, 1, 0.1, 0.25)
        self.mouth_position_y = remap(self.dna.genes[5], 0, 1, 0.1, 0.3)
        self.mouth_open = remap(self.dna.genes[6], 0, 1, 5, 20)
        self.eye_size = remap(self.dna.genes[7], 0, 1, 15, 30)
        self.hair_length = remap(self.dna.genes[8], 0, 1, 1, 1.5)
        self.hair_variation = remap(self.dna.genes[9], 0, 1, 0.1, 0.2)
        self.hair_wave = remap(self.dna.genes[10], 0, 1, 1, 10)

        # color from gene 11
        random_seed(int(self.dna.genes[11] * 99999999))
        self.facecol = random(0, 255, 3) #color(random(0, 255), random(0, 255), random(0, 255))

        # hair color from gene 12
        random_seed(int(self.dna.genes[12] * 99999999))
        self.haircol = random(0, 255, 3) #color(random(0, 255), random(0, 255), random(0, 255))


    def draw(self):
        push_matrix()
        translate(self.x, self.y)

        self.draw_face()
        self.draw_eyes()
        self.draw_mouth()
        self.draw_hair()

        pop_matrix()

    def draw_face(self):
        fill(self.facecol)
        no_stroke()

        begin_shape()
        n = 30
        for i in range(n):
            theta = i * TWO_PI / n
            n_x = noise(sin(theta * 0.5))
            offset_x = remap(n_x, 0, 1, 1 - self.face_distort, 1 + self.face_distort)
            x = (sin(theta) * self.width / 2) * offset_x
            y = (cos(theta) * self.height / 2)
            curve_vertex(x, y)
        end_shape()

    def draw_eyes(self):
        push_matrix()
        translate(0, -self.height * self.eye_position_y)

        fill(255, 255, 255)
        ellipse(-self.width * self.eye_spread, 0, self.eye_size, self.eye_size)
        ellipse(self.width * self.eye_spread, 0, self.eye_size, self.eye_size)

        fill(0, 0, 0)
        ellipse(-self.width * self.eye_spread, 3, 8, 8)
        ellipse(self.width * self.eye_spread, 3, 8, 8)

        pop_matrix()

    def draw_mouth(self):
        push_matrix()
        translate(0, self.height * self.mouth_position_y)
        stroke(255)
        stroke_weight(2)
        no_fill()

        begin_shape()
        curve_vertex(-self.width * 0.15, 0)
        curve_vertex(-self.width * 0.15, 0)
        curve_vertex(0, self.mouth_open)
        curve_vertex(self.width * 0.15, 0)
        curve_vertex(self.width * 0.15, 0)
        end_shape()

        pop_matrix()

    def draw_hair(self):
        # use fixed seed so hair layout is stable for a given face
        random_seed(int(self.seed))
        no_fill()
        stroke(self.haircol)
        stroke_weight(8)

        n = 20
        theta = np.linspace((PI * 3) / 4, (PI * 5) / 4, n)
        n_x = noise(sin(theta * 0.5))
        
        for i in range(n):
            offset_x = remap(n_x[i], 0, 1, 1 - self.face_distort, 1 + self.face_distort)
            x = (sin(theta[i]) * self.width / 2) * offset_x
            y = (cos(theta[i]) * self.height / 2)

            hair_length = self.hair_length * random(
                1 - self.hair_variation, 1 + self.hair_variation
            )

            m = np.linspace(1, hair_length, 20)
            n = remap(
                    noise(m * self.hair_wave, theta[i] * self.hair_wave),
                    0, 1, -0.1, 0.1)
            x1 = (sin(theta[i] + n) * self.width / 2) * offset_x * m
            y1 = (cos(theta[i] + n) * self.height / 2) * m
            polyline(x1, y1)
        # Slow
        # for i in range(10):
        #     theta = remap(i, 0, 10, (PI * 3) / 4, (PI * 5) / 4)
        #     n_x = noise(sin(theta * 0.5))
        #     offset_x = remap(n_x, 0, 1, 1 - self.face_distort, 1 + self.face_distort)
        #     x = (sin(theta) * self.width / 2) * offset_x
        #     y = (cos(theta) * self.height / 2)

        #     hair_length = self.hair_length * random(
        #         1 - self.hair_variation, 1 + self.hair_variation
        #     )
        #     begin_shape()
        #     for j in range(20):
        #         m = remap(j, 0, 19, 1, hair_length)
        #         n = remap(
        #             noise(m * self.hair_wave, theta * self.hair_wave),
        #             0,
        #             1,
        #             -0.1,
        #             0.1,
        #         )
        #         x1 = (sin(theta + n) * self.width / 2) * offset_x * m
        #         y1 = (cos(theta + n) * self.height / 2) * m
        #         vertex(x1, y1)
        #     end_shape()


# ---------------- DNA CLASS ----------------

class DNA:
    def __init__(self, num_genes):
        self.num_genes = num_genes
        self.genes = random(0, 1, num_genes)
        self.fitness = 1
        
    def mutate(self, mutation_probability):
        # mutation_probability comes from params.mutation_probability
        
        for i in range(self.num_genes):
            if random() < mutation_probability:
                self.genes[i] = random()
        


run()
