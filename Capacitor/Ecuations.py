from manimlib.imports import *
from manimlib.my_packages.my_animations import *
class Desarrollo(Scene):
    def construct(self):
        Kirchoff=TexMobject("0","=","{ V }_{ C }","+{ V }_{ R }","-\\E ")
        V_capa=TexMobject("V_{ C }=\\int { i(t).dt } ")
        V_resis=TexMobject("V_{ R }=i.R")

        self.play(
        FadeInFromEdges(Kirchoff)
        )

        self.play(
        CounterclockwiseTransform(Kirchoff[0],Kirchoff[4])
        )


