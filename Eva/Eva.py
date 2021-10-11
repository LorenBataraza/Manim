from manimlib.imports import *
from manimlib.my_packages.my_animations import *

class Formulas(Scene):
    def setup(self):
        self.CaCO3=TexMobject("1\quad","CaCO_{3}","\\dashrightarrow", "1\quad", "CaO").scale(1.5)
        self.MgCO3=TexMobject("1\quad", "MgCO_{3}","\\dashrightarrow", "1\quad", "MgO").scale(1.4)
        self.FG_CaCO3=TexMobject("FG =","{","56,08","\\over","100,09","}","=", "0,5603")
        self.FG_MgCO3=TexMobject("FG =","{","40,30","\\over","84,32","}","=", "0,4479")



class TestScene(Formulas):
  def construct(self):
    
    self.play(
            FadeInFromEdges(self.CaCO3),
            run_time=3
        )
    self.play(
                self.CaCO3.shift, UL*2+LEFT,
                run_time=2,
                )
    self.play(
            FadeInFromEdges(self.MgCO3),
            run_time=3
        )
    self.play(
                self.MgCO3.shift, DL*2+LEFT,
                run_time=2,
                )
    self.p_CaCO3=Brace(self.CaCO3[1],DOWN)
    self.p_MgCO3=Brace(self.MgCO3[1],DOWN)
    self.p_MgO=Brace(self.MgCO3[4],DOWN)
    self.p_CaO=Brace(self.CaCO3[4],DOWN)
    self.t_CaCO3 = self.p_CaCO3.get_text("100,09", "g/mol")
    self.t_MgCO3 = self.p_MgCO3.get_text("84,32", " g/mol")
    self.t_MgO = self.p_MgO.get_text("40,30", " g/mol")
    self.t_CaO = self.p_CaO.get_text("56,08", " g/mol")  

    self.play(
                FadeIn(self.p_CaCO3),
                FadeIn(self.p_MgCO3),
                FadeIn(self.p_MgO),
                FadeIn(self.p_CaO),
                )   
    self.play(
            FadeInFromEdges(self.t_CaCO3),
            FadeInFromEdges(self.t_MgCO3),
            FadeInFromEdges(self.t_MgO),
            FadeInFromEdges(self.t_CaO),
            run_time=3
            )
    self.FG_CaCO3.next_to(self.CaCO3,RIGHT*4)
    self.FG_MgCO3.next_to(self.MgCO3,RIGHT*4)
    self.play(
            Write(self.FG_CaCO3[0:1]),
            Write(self.FG_CaCO3[3]),
            Write(self.FG_CaCO3[5]),
            Write(self.FG_MgCO3[0:1]),
            Write(self.FG_MgCO3[3]),
            Write(self.FG_MgCO3[5]),
            )
    self.play(
            ReplacementTransform(self.t_CaO[0].copy(),self.FG_CaCO3[2]),
            ReplacementTransform(self.t_MgO[0].copy(),self.FG_MgCO3[2]),
            run_time=2.5,
        )
    self.play(
        ReplacementTransform(self.t_CaCO3[0].copy(),self.FG_CaCO3[4]),
        ReplacementTransform(self.t_MgCO3[0].copy(),self.FG_MgCO3[4]),
        run_time=3.5,
        )
    self.play(
            Write(self.FG_CaCO3[6]),
            Write(self.FG_CaCO3[7]),
            Write(self.FG_MgCO3[6]),
            Write(self.FG_MgCO3[7]),
            run_time=2.5,
            )
    self.wait(1.5)