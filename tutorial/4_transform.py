from manimlib.imports import *

class TransformationText1V1(Scene):
	def construct(self):
		texto1 = TextMobject("First text")
		texto2 = TextMobject("Second text")
		self.play(Write(texto1))
		self.wait()
		self.play(Transform(texto1,texto2))
		self.wait()

class TransformationText1V2(Scene):
	def construct(self):
		texto1 = TextMobject("First text")
		texto1.to_edge(UP)
		texto2 = TextMobject("Second text")
		self.play(Write(texto1))
		self.wait()
		self.play(Transform(texto1,texto2))
		self.wait()

class TransformationText2(Scene):
	def construct(self):
		text1 = TextMobject("Function")
		text2 = TextMobject("Derivative")
		text3 = TextMobject("Integral")
		text4 = TextMobject("Transformation")
		self.play(Write(text1))
		self.wait()
		#Trans text1 -> text2
		self.play(ReplacementTransform(text1,text2))
		self.wait()
		#Trans text2 -> text3
		self.play(ReplacementTransform(text2,text3))
		self.wait()
		#Trans text3 -> text4
		self.play(ReplacementTransform(text3,text4))
		self.wait()

class CopyTextV1(Scene):
	def construct(self):
		formula = TexMobject(
			"\\frac{d}{dx}", #0
			"(", #1
			"u", #2
			"+", #3
			"v", #4
			")", #5
			"=", #6
			"\\frac{d}{dx}", #7
			"u", #8
			"+", #9
			"\\frac{d}{dx}", #10
			"v" #11
			)
		formula.scale(2)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9])
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10])
			)
		self.wait()

class CopyTextV2(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTextV3(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		formula[8].set_color(RED)
		formula[11].set_color(BLUE)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTextV4(Scene):
	def construct(self):
		formula = TexMobject("\\frac{d}{dx}",
			"(","u","+","v",")","=",
			"\\frac{d}{dx}","u","+","\\frac{d}{dx}","v"
			)
		formula.scale(2)
		for letter,color in [("u",RED),("v",BLUE)]:
			formula.set_color_by_tex(letter,color)
		self.play(Write(formula[0:7]))
		self.wait()
		self.play(
			ReplacementTransform(formula[2].copy(),formula[8]),
			ReplacementTransform(formula[4].copy(),formula[11]),
			ReplacementTransform(formula[3].copy(),formula[9]),
			run_time=3
			)
		self.wait()
		self.play(
			ReplacementTransform(formula[0].copy(),formula[7]),
			ReplacementTransform(formula[0].copy(),formula[10]),
			run_time=3
			)
		self.wait()

class CopyTwoFormulas1(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg",		#0
				"\\forall",		#1
				"x",			#2
				":",			#3
				"P(x)"			#4
			)
		formula2 = TexMobject(
				"\\exists",		#0
				"x",			#1
				":",			#2
				"\\neg",		#3
				"P(x)"			#4
			)
		for size,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
			formula.scale(size)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait()
		changes = [
			[(0,1,2,3,4),
			# | | | | |
			# v v v v v
			 (3,0,1,2,4)],
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class CopyTwoFormulas2(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		for tam,pos,formula in [(2,2*UP,formula1),(2,2*DOWN,formula2)]:
			formula.scale(tam)
			formula.move_to(pos)
		self.play(Write(formula1))
		self.wait()
		changes = [
			# First time
			[(2,3,4),
			# | | |
			# v v v
			 (1,2,4)],
			# Second time
			[(0,),
			# | 
			# v
			 (3,)],
			# Third time
			[(1,),
			# | 
			# v
			 (0,)]
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class CopyTwoFormulas2Color(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		parametters = [(2,2*UP,formula1,GREEN,"\\forall"),
					  (2,2*DOWN,formula2,ORANGE,"\\exists")]
		for size,pos,formula,col,sim in parametters:
			formula.scale(size)
			formula.move_to(pos)
			formula.set_color_by_tex(sim,col)
			formula.set_color_by_tex("\\neg",PINK)
		self.play(Write(formula1))
		self.wait()
		changes = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i].copy(),formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class CopyTwoFormulas3(Scene):
	def construct(self):
		formula1 = TexMobject(
				"\\neg","\\forall","x",":","P(x)"
			)
		formula2 = TexMobject(
				"\\exists","x",":","\\neg","P(x)"
			)
		parametters = [(2,2*UP,formula1,GREEN,"\\forall"),
					  (2,2*DOWN,formula2,ORANGE,"\\exists")]
		for size,pos,formula,col,sim in parametters:
			formula.scale(size)
			formula.move_to(pos)
			formula.set_color_by_tex(sim,col)
			formula.set_color_by_tex("\\neg",PINK)
		self.play(Write(formula1))
		self.wait()
		changes = [
			[(2,3,4),(1,2,4)],
			[(0,),(3,)],
			[(1,),(0,)]
		]
		for pre_ind,post_ind in changes:
			self.play(*[
				ReplacementTransform(
					formula1[i],formula2[j]
					)
				for i,j in zip(pre_ind,post_ind)
				],
				run_time=2
			)
			self.wait()

class ChangeTextColorAnimation(Scene):
	def construct(self):
		text = TextMobject("Text")
		text.scale(3)
		self.play(Write(text))
		self.wait()
		self.play(
                text.set_color, YELLOW,
                run_time=2
            )
		self.wait()

class ChangeSizeAnimation(Scene):
	def construct(self):
		text = TextMobject("Text")
		text.scale(2)
		self.play(Write(text))
		self.wait()
		self.play(
                text.scale, 3,
                run_time=2
            )
		self.wait()

class MoveText(Scene):
	def construct(self):
		text = TextMobject("Text")
		text.scale(2)
		text.shift(LEFT*2)
		self.play(Write(text))
		self.wait()
		self.play(
                text.shift, RIGHT*2,
                run_time=2,
                path_arc=0 #Change 0 by -np.pi
            )
		self.wait()

class ChangeColorAndSizeAnimation(Scene):
	def construct(self):
		text = TextMobject("Text")
		text.scale(2)
		text.shift(LEFT*2)
		self.play(Write(text))
		self.wait()
		self.play(
                text.shift, RIGHT*2,
                text.scale, 2,
                text.set_color, RED,
                run_time=2,
            )
		self.wait()


class UpdateValueTracker1(Scene):
    def construct(self):
        theta = ValueTracker(PI/2)
        line_1= Line(ORIGIN,RIGHT*3,color=RED)
        line_2= Line(ORIGIN,RIGHT*3,color=GREEN)

        line_2.rotate(theta.get_value(),about_point=ORIGIN)

        line_2.add_updater(
                lambda m: m.set_angle(
                                    theta.get_value()
                                )
            )

        self.add(line_1,line_2)

        self.play(theta.increment_value,PI/2)

        self.wait()

class UpdateValueTracker2(Scene):
    CONFIG={
        "line_1_color":ORANGE,
        "line_2_color":PINK,
        "lines_size":3.5,
        "theta":PI/2,
        "increment_theta":PI*3,
        "final_theta":PI,
        "radius":0.7,
        "radius_color":YELLOW,
    }
    def construct(self):
        # Set objets
        theta = ValueTracker(self.theta)
        line_1= Line(ORIGIN,RIGHT*self.lines_size,color=self.line_1_color)
        line_2= Line(ORIGIN,RIGHT*self.lines_size,color=self.line_2_color)

        line_2.rotate(theta.get_value(),about_point=ORIGIN)
        line_2.add_updater(
                lambda m: m.set_angle(
                                    theta.get_value()
                                )
            )

        angle= Arc(
                    radius=self.radius,
                    start_angle=line_1.get_angle(),
                    angle =line_2.get_angle(),
                    color=self.radius_color
            )

        # Show the objects

        self.play(*[
                ShowCreation(obj)for obj in [line_1,line_2,angle]
            ])

        # Set update function to angle

        angle.add_updater(
                    lambda m: m.become(
                            Arc(
                                radius=self.radius,
                                start_angle=line_1.get_angle(),
                                angle =line_2.get_angle(),
                                color=self.radius_color
                            )
                        )
            )
        # Remember to add the objects again to the screen 
        # when you add the add_updater method.
        self.add(angle)

        self.play(theta.increment_value,self.increment_theta)
        # self.play(theta.set_value,self.final_theta)

        self.wait()
        