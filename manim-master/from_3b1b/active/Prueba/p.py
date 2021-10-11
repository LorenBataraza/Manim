from manimlib.imports import *
from manimlib.my_animations import FadeInFromEdges

class TestScene(Scene):
  def construct(self):
    t =TexMobject(r"\int _{ -567 }^{ 263 }{ \frac { { x }^{ 2 } }{ { e }^{ 2 } }  } ")
    t.scale(2)
    self.play(FadeInFromEdges(t))

class IndicateExample(Scene):
    def construct(self):
        #                     0    1   2
        formula = TexMobject("f(","x",")")
        self.add(formula)
        self.play(Indicate(formula[1],run_time=1.5))
