from manimlib.imports import *
from manimlib.my_packages.my_animations import *

class Grafico(GraphScene):
    CONFIG = {
        "y_max" : 0.58,
        "y_min" : 0.38,
        "x_max" : 1.1,
        "x_min" : 0,
        "y_tick_frequency" : 0.02,
        "x_tick_frequency" : 0.1,
        "x_axis_label" : "${ X }_{ CaC{ O }_{ 3 } }$",
        "y_axis_label" : "$FG$",
        "axes_color" : BLUE, 
        "x_labeled_nums":list(np.arange(0, 1.1, 0.2)),
        "exclude_zero_label": False,
        "y_labeled_nums":[0.5271],
        "x_axis_width": 7,
        "y_axis_height": 5,
        "y_label_decimal":4,
        "graph_origin": 3.2 * DOWN + 1.3 *LEFT,
        "x_label_decimal":1,
        "x_label_direction":DOWN,
        "y_label_direction":LEFT,        
    }
    def construct(self):
        Ecuacion_1=TexMobject("x",".0,5603","+","(1-","x",").0,4479","=","{(100-47,29) \\over (100)}")
        Ecuacion_1.set_color_by_tex("x",RED)
        Ecuacion_1.move_to(UP*3+LEFT*3).scale(0.8)
        self.play(
            ShowCreation(Ecuacion_1),
            run_time = 2
        )
        t=TexMobject("0,5271").scale(0.8)
        t.next_to(Ecuacion_1[6],RIGHT,buff=0.2)
        self.play(
            ReplacementTransform(Ecuacion_1[7],t),
            run_time = 2
        )
      
        self.setup_axes(animate=False)
        self.x_axis.shift(LEFT*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))
        self.y_axis.shift(DOWN*abs(self.y_axis[0].points[0]-self.x_axis[0].points[0]))          
        self.y_axis_label_mob.next_to(self.y_axis[0].get_end(),UP)
        
        linea = self.get_graph(lambda x : x*0.5603+(1-x)*0.4479,
            x_min= 0,
            x_max=1)
        linea.set_color(color=[RED, ORANGE, YELLOW, GREEN, PURPLE])
        self.play(
            ShowCreation(linea),
            run_time = 3.5
        )
        a=self.coords_to_point(1,0.5603)
        b=self.coords_to_point(0,0.5603)
        c=self.coords_to_point(0,0.4479)
        d=self.coords_to_point(1,0.379)
        horz_line= DashedLine(a,b, color=GREY,dash_spacing=0.16)
        vert_line= DashedLine(a,d, color=GREY,dash_spacing=0.16)
        self.play(
            ShowCreation(horz_line),
            ShowCreation(vert_line),
            run_time = 2
        )
        T_Ca=TexMobject("{ FG }_{ { CaCO }_{ 3 } }").scale(0.8)
        T_Mg=TexMobject("{ FG }_{ { MgCO }_{ 3 } }").scale(0.8)

        T_Ca.move_to(b+LEFT)
        T_Mg.move_to(c+LEFT)
        self.play(
            ShowCreation(T_Ca),
            ShowCreation(T_Mg),
            run_time = 2
        )
        
        e=self.coords_to_point(0,0.5271)
        f=self.coords_to_point(0.7046,0.5271)
        g=self.coords_to_point(0.7046,0.379)
        horz_line2= DashedLine(e,f, color=YELLOW,dash_spacing=0.16)
        vert_line2= DashedLine(f,g, color=YELLOW,dash_spacing=0.16)
        self.play(
            ShowCreation(horz_line2),
            run_time = 2
        )
        self.play(
            ShowCreation(vert_line2),
            run_time = 2
        )
        x=TexMobject("x").scale(1.5)
        x.next_to(g,DOWN*0.4)
        x.set_color_by_tex("x",RED)
        self.play(
            ShowCreation(x),
            run_time = 2
        )
        Flecha=TexMobject("\\underrightarrow { Despejando } ").next_to(t,RIGHT*0.7).scale(0.7)
        Ecuacion_casi=TexMobject("0,1124","x","=","0,0792").next_to(Flecha, RIGHT*0.5)
        Ecuacion_casi.set_color_by_tex("x",RED)
        Dividido=TexMobject("{0,0792 \\over 0,1124}").next_to(Ecuacion_casi[2],RIGHT*0.1)
        Result=TexMobject("0,7056").next_to(Ecuacion_casi[2],RIGHT*0.15)
        self.play(
            ShowCreation(Flecha),
            FadeInFromEdges(Ecuacion_casi),
            run_time = 2
        )
        self.wait(1.5)
        self.remove(Ecuacion_casi[3]) 

        self.play(
            CounterclockwiseTransform(Ecuacion_casi[0],Dividido),
            run_time = 2
        )
        self.wait(1.5)
        self.remove(Ecuacion_casi[0]) 
        self.play(
            ReplacementTransform(Dividido,Result),
            run_time = 2
        )
        self.wait(1.5)
        self.play(
            Ecuacion_casi[1].shift,LEFT*0.8,
            Ecuacion_casi[2].shift,LEFT*0.8,
            Result.shift,LEFT*0.7,
            run_time = 2
        )
        self.wait(2)