from os import write
from numpy.lib.function_base import gradient
from manimlib.imports import *
import numpy as np

# To watch one of these scenes, run the following:
# python -m manim FurtherMaths.py Open -pl
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
        eq2 = TexMobject(r"\int_{0}^{\infty} sin(x^2) dx").set_color(RED)

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
        self.play(t5.to_edge, LEFT)
        self.play(t5.shift, 0.5*UP)   
        self.wait(1)         
        self.play(Write(eq1.next_to(t5, 1*DOWN)))

        self.play(ShowCreation(arrw))
        self.play(Write(t6))
        self.wait(1)
        self.play(Write(eq2.next_to(t6, LEFT + DOWN)))

class Study(Scene):
    def construct(self):
        t1 = TextMobject("What do we Study?").set_color_by_gradient(ORANGE, BLUE)
        t2 = TextMobject("Differentiation").set_color(BLUE).to_edge(2*LEFT + UP)
        eq1 = TexMobject(
            r"f(x)",  #[0]
            "=",      #[1]
            "6x^3",   #[2]
            "- 9x",   #[3]
            "+4").scale(1.2).set_color(BLUE_A)    #[4]
        eq1_2 = TexMobject(
            r"f(x_d)",  #[0]
            "=",        #[1]
            "18x^2",    #[2]
            "- 9").scale(1.2).set_color_by_gradient(BLUE, TEAL) #[3]
        t3 = TextMobject("Integration").set_color(ORANGE).to_edge(2*LEFT)
        eq2 = TexMobject(r"18x^2 - 9").scale(1.3).set_color(BLUE_A)
        eq2_2 = TexMobject(r"6x^3 - 9x + dx").scale(1.3).set_color_by_gradient(BLUE, TEAL)
        t4 = TextMobject("Matrices").set_color(RED).to_edge(2*LEFT + 1*DOWN)
        eq3 = TexMobject(r"\begin{bmatrix}1 & 2 & 3\\5 & 2 & 8\end{bmatrix}").scale(1.3).set_color(BLUE_A)
        eq4 = TexMobject(r"\begin{bmatrix}1 & 2 & 3\\5 & 2 & 8\end{bmatrix} \cdot \begin{bmatrix}7 & 2 & 1\\9 & 9 & 3\end{bmatrix}").scale(1.3).set_color_by_gradient(BLUE, TEAL)
        t5 = TextMobject("?").set_color(RED).scale(2.5)
        t6 = TextMobject("Further Maths is a challenge!").scale(2).set_color_by_gradient(MAROON, RED)

        self.play(Write(t1.scale(2)), run_time=4)
        self.wait(3)
        self.play(FadeOut(t1))
        self.wait(2)
        self.play(Write(t2.scale(1.5))), self.wait(1), self.play(Write(eq1[0:4].to_edge(UP + RIGHT)))
        self.play(Write(t3.scale(1.5))), self.wait(1), self.play(Write(eq2.to_edge(3*RIGHT).shift(0.5*UP)))
        self.play(Write(t4.scale(1.5))), self.wait(1), self.play(Write(eq3.to_edge(3*RIGHT + DOWN)))
        self.wait(2)
        self.play(ReplacementTransform(eq1[0].copy(), eq1_2[0].next_to(eq1[0], 1*DOWN)))
        self.wait(1)
        self.play(ReplacementTransform(eq1[1].copy(), eq1_2[1].next_to(eq1_2[0], RIGHT)))
        self.wait(1)
        self.play(ReplacementTransform(eq1[2].copy(), eq1_2[2].next_to(eq1_2[1], RIGHT)))
        self.wait(1)
        self.play(ReplacementTransform(eq1[3].copy(), eq1_2[3].next_to(eq1_2[2], RIGHT)))
        self.wait(1)
        self.play(ReplacementTransform(eq2.copy(), eq2_2.next_to(eq2, 1*DOWN)))
        self.wait(1)
        self.play(Transform(eq3, eq4.to_edge(3*RIGHT + DOWN)))
        self.wait(2)
        self.play(Transform(t2, t5))
        self.play(Transform(t3, t5))
        self.play(Transform(t4, t5))
        self.play(Transform(eq1[0:4], t5))
        self.play(Transform(eq1_2[0:4], t5))
        self.play(Transform(eq2, t5))
        self.play(Transform(eq2_2, t5))
        self.play(Transform(eq3, t5))
        self.wait(2)
        self.play(
            FadeOut(t2),
            FadeOut(t3),
            FadeOut(t4),
            FadeOut(eq1[0:4]),
            FadeOut(eq1_2[0:4]),
            FadeOut(eq2),
            FadeOut(eq2_2),
            FadeOut(eq3)
        )
        self.wait(2)
        self.play(Write(t6))
        self.wait(2)



class Advice(Scene):
    def construct(self):
        t1 = TextMobject("Here's some advice...").set_color_by_gradient(ORANGE, BLUE).scale(2)
        t2 = TextMobject("Further Maths is A LOT of work").scale(1.5)
        t3 = TextMobject("1. Be Willing to work your best!").scale(1.5).set_color(BLUE_B)
        t4 = TextMobject("2. Be Intrested in Maths!").scale(1.5).set_color(BLUE_B)
        t5 = TextMobject("Be Intrested in whatever your doing!").scale(1.7).set_color_by_gradient(BLUE, MAROON)


        self.play(Write(t1), run_time=4)
        self.wait(2)
        self.play(FadeOut(t1))
        self.wait(1)
        self.play(Write(t2))
        self.wait(2)
        self.play(FadeOut(t2))
        self.wait(2)
        self.play(Write(t3.shift(UP)))
        self.wait(1)
        self.play(Write(t4.shift(DOWN)))
        self.wait(2)
        self.play(
            FadeOut(t3),
            ReplacementTransform(t4, t5, run_time=3)
        )
        self.wait()

class Graph(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -10,
        "y_max": 10,
        "graph_origin": ORIGIN
    }
    def construct(self):
        self.setup_axes(animate=True)
        func1 = self.get_graph(lambda x: x**3 - 3*x**2 - 2*x + 1, x_min=-2, x_max=4, color=BLUE)
        func2 = self.get_graph(lambda x: x**2 +2, x_min=-3, x_max=3, color=RED)
        func3 = self.get_graph(lambda x: np.sin(x)*np.log(x), x_min=0.5, x_max=10, color=GREEN)
        t1 = TexMobject(r"f(x) = x^3 - 3x^2 - 2x + 1").set_color_by_gradient(BLUE_B, TEAL).scale(0.8)
        t2 = TexMobject(r"f(x) = x^2 + 2").set_color_by_gradient(RED, MAROON)
        t3 = TexMobject(r"f(x) = \sin{x} \cdot \log{x}").set_color_by_gradient(GREEN_B, GREEN_D)

        self.play(ShowCreation(func1), run_time=3)
        self.play(Write(t1.next_to(func1, UP + RIGHT)))
        self.play(ShowCreation(func2), run_time=4)
        self.play(Write(t2.next_to(func2, LEFT)))
        self.play(ShowCreation(func3), run_time=3)
        self.play(Write(t3.next_to(func3, DOWN)))
