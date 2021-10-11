from manimlib.imports import *
from manimlib.my_packages.my_animations import *


class FormulaExample1(Scene):
    def setup(self):
        self.tex_example = TexMobject(r"""
                    \oint_C \vec{B}\cdot d\vec{l}=\mu_0\int_S \vec{J}\cdot d \vec{s}+\mu_0\epsilon_0\dfrac{d}{dt}\int_S \vec{E}\cdot d \vec{s}"""  
                )

class FormulaExample3(Scene):
    def setup(self):
        self.tex_example = TexMobject(r" x.a%\quad +",r"\quad (x-1)b%\quad",r"=",r"\quad c%",)

class FormulaExample2(Scene):
    def setup(self):
        self.tex_example = TexMobject(r"La \quad concha\quad de\quad tu\quad madre\quad Messi")       


class TestScene(FormulaExample3):
  def construct(self):
    t=TexMobject(r"x.b%-b%")
    self.play(
            FadeInFromEdges(self.tex_example),
            run_time=3
        )
    self.play(ClockwiseTransform(self.tex_example[2],t))
    self.play(UnderlineIndication(self.tex_example,line_type=DashedLine)