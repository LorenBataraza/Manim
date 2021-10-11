from manimlib.imports import *

class Circuit(Scene):
    def construct(self):
        tex_circuit="""\\begin{circuitikz}[american]
                   \\draw[ultra thin](-2,-2) to [vsourcesin,invert,f<,o-,l=$V$] (-2,2);
                   \\draw[ultra thin](-2,2) to [R,v^=$ $,l_,o-*] (0,2) to [cute inductor,v_=$ $,l^,*-*] (2,2);
                   \\draw[ultra thin](2,2) to [C,l^] (2,-2) to[lamp,*-] (-2,-2);
                   \\draw[-stealth] ([shift=(20:1cm)]0,0) arc (20:300:1cm) node [above] {$i$};
                   \\end{circuitikz}"""

        circuit=TextMobject(tex_circuit,stroke_width=2,fill_opacity=0)
 
        self.play(Write(circuit))
        self.wait()

class TestSVG(Scene):
    def construct(self):
        circuit=SVGMobject("d")
        self.play(FadeIn(circuit))

class TikzMobject(TextMobject):
    CONFIG = {
        "stroke_width": 3,
        "fill_opacity": 0,
        "stroke_opacity": 1,
    }

class ExampleTikz(Scene):
    def construct(self):
        circuit = TikzMobject(r"""
            \begin{tikzpicture}
                \draw (0,0) -- (1,0);
                \node at (1,0) {sometext};
            \end{tikzpicture}
            """
            )
        self.play(Write(circuit))            
class Example(Scene):
    def construct(self):

        self.wait()
        TEMPLATE_TEX_FILE_TIKZ = os.path.join(
        THIS_DIR,"tex_files", "tex_template_tikz.tex")
        with open(TEMPLATE_TEX_FILE_TIKZ, "r") as infile:
            TEMPLATE_TEXT_FILE_BODY_TIKZ = infile.read()
            TEMPLATE_TEX_FILE_BODY_TIKZ = TEMPLATE_TEXT_FILE_BODY_TIKZ.replace(
              TEX_TEXT_TO_REPLACE,
             "\\begin{tikzpicture}\n" + TEX_TEXT_TO_REPLACE + "\n\\end{tikzpicture}",
            )
        self.play(Write(TEMPLATE_TEX_FILE_TIKZ))