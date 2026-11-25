from py5canvas import *
from slimgui import imgui

"""
TASK
Change the face to your liking. Make sure that the number of properties correspond to the number of genes in the dna
"""

face = None  # global face instance


# ---------------- UI PARAMETERS (for mutation probability) ----------------

def parameters():
    return {
        "Mutation Probability": (0.2, 0.0, 1.0),
    }


# ---------------- GUI (Mutate button using Imgui) ----------------

def gui():
    if imgui.button("Mutate"):
        random_seed(frame_count)
        mutate()
    

# ---------------- SETUP / DRAW ----------------

def setup():
    global face
    create_canvas(512, 512)

    # create one new face object
    face = Face(width / 2, height / 2)


def mutate():
    """
    This function calls the mutate method of face.dna and then
    calc_phenotype to express the mutated genes.
    """
    print("mutate")
    face.dna.mutate(params.mutation_probability)
    face.calc_phenotype()
    print(face.dna.genes)


def draw():
    background(0)
    face.draw()
    fill(255)


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
        self.fitness = 1.0

    def mutate(self, mutation_probability):
        # mutation_probability comes from params.mutation_probability
        for i in range(self.num_genes):
            if random() < mutation_probability:
                self.genes[i] = random()
        


run()
