from os import write
from numpy.lib.function_base import gradient
from manimlib.imports import *
import numpy as np

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flag -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

class Open(Scene):
    def construct(self):
        tex = TextMobject('Why Study Further Maths?').set_color_by_gradient(ORANGE, BLUE)
        text2 = TextMobject('There are a number of reasons...')

        t3 = TextMobject("Computer Science").set_color_by_gradient(BLUE, GREEN)
        line = Line(np.array([4,0,0]), np.array([-4,0,0])).set_color_by_gradient(BLUE, GREEN)
        t4 = TextMobject("Computer Science NEEDS Math")
        t5 = TextMobject("Recursion Problems\n").set_color(BLUE)
        eq1 = TexMobject(r"f(x) = 3 \cdot f(x – 2) + 4")
        arrw = Arrow(np.array([-2,0,0]),np.array([2,0,0])).set_color_by_gradient(BLUE, GREEN)
        t6 = TextMobject("???    \n").to_edge(RIGHT).set_color(GREEN)
        eq2 = TexMobject(r"\int_{0}^{\infty} sin(x^2) dx")

        self.play(Write(tex.scale(2)), run_time=4)
        self.wait(4)
        self.play(Transform(tex,text2))
        self.wait(3)
        self.play(FadeOut(tex, text2))
        self.play(Write(t3.scale(2)))
        self.wait(2)
        self.play(t3.to_edge, UP)
        self.wait(0.5)
        self.play(ShowCreation(line.next_to(t3, DOWN), run_time=1))
        self.wait(1)
        self.play(Write(t4.next_to(line, DOWN)))
        self.wait(1)
        self.play(Write(t5)), self.wait(2)
        self.play(t5.to_edge, LEFT), self.wait(1)
        self.play(Write(eq1.next_to(t5, DOWN)))

        self.play(ShowCreation(arrw))
        self.play(Write(t6))
        self.wait(1)
        self.play(Write(eq2.next_to(t6, LEFT + DOWN)))

class Study(Scene):
    def construct(self):
        t1 = TextMobject("What do we Study?").set_color_by_gradient(ORANGE, BLUE)
        t2 = TextMobject("Differentiation").set_color(BLUE).to_edge(2*LEFT + UP)
        eq1 = TexMobject(r"f(x) = 6x^3 - 9x+4").scale(1.2)
        t3 = TextMobject("Integration").set_color(ORANGE).to_edge(2*LEFT)
        eq2 = TexMobject(r"18x^2 - 9").scale(1.3)
        t4 = TextMobject("Matrices").set_color(RED).to_edge(2*LEFT + 1*DOWN)
        eq3 = TexMobject(r"\begin{bmatrix}1 & 2 & 3\\5 & 2 & 8\end{bmatrix}").scale(1.3)
        eq4 = TexMobject(r"\begin{bmatrix}1 & 2 & 3\\5 & 2 & 8\end{bmatrix} \cdot \begin{bmatrix}7 & 2 & 1\\9 & 9 & 3\end{bmatrix}").scale(1.3)

        self.play(Write(t1.scale(2)), run_time=4)
        self.wait(3)
        self.play(FadeOut(t1))
        self.wait(2)
        self.play(Write(t2.scale(1.5))), self.wait(1), self.play(Write(eq1.to_edge(UP + RIGHT)))
        self.play(Write(t3.scale(1.5))), self.wait(1), self.play(Write(eq2.to_edge(3*RIGHT)))
        self.play(Write(t4.scale(1.5))), self.wait(1), self.play(Write(eq3.to_edge(3*RIGHT + DOWN)))
        self.wait(2)
        self.play(Transform(eq3, eq4.to_edge(3*RIGHT + DOWN)))
        self.wait(2)

        # NOTE : Fix scaling and positions for t2-eq3 !!

class Advice(Scene):
    def construct(self):
        t1 = TextMobject("Here's some advice...").set_color_by_gradient(ORANGE, BLUE)