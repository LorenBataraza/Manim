from manimlib.imports import *

class VerticalBarChart(VGroup):
    CONFIG = {
        "is_add_bars": False, # False: not add, later want to do animation
        "title": "Bar Chart", # or None
        "title_color": WHITE,
        "title_size": 0.6,
        "title_buff": 0.5,
        "title_font": None,

        "x_axis_length": 10,
        "x_min":0,
        "x_max":100,

        "x_axis_title": 'X values',
        "x_axis_title_color": WHITE,
        "x_axis_title_size": 0.4,
        "x_axis_title_buff": 0.2,

        "y_axis_title": 'Y values',
        "y_axis_title_color": WHITE,
        "y_axis_title_size": 0.4,
        "y_axis_title_buff": 0.2,

        "y_min": 0,
        "y_max": 100,
        "y_tick_frequency": 20,
        "y_axis_length": 5,


        "y_labels_color": WHITE,
        "y_labels_size": 0.3,
        "y_labels_buff": 0.2,
        "y_labels_decimal_places": 0,

        "graph_origin": np.array([-5,-2, 0]),

        "bar_names": ["A", "B", "C", "D", "E"],
        "bar_names_color": WHITE,
        "bar_names_buff": 0.2,
        "bar_names_size": 0.3,

        "bar_values": [30, 50, 80, 60, 40],
        "bar_values_position": UP, # UP: above the bar,  DOWN: below the bar
        "bar_values_buff": 0.3,  #buff to the bar edge
        "gap_ratio": 0.2,  # gap ratio with the rectangle's width -> gap_width / rect_width
        "edge_buff": 0.5,  # for the space between x_axis's start and first rectangle, last rect and the end

        "bar_colors": [RED, RED, RED, RED, RED],
        "bar_fill_opacity": 1.0,
        "bar_stroke_width": 0,
    }

    def __init__(self, data=[], **kwargs):
        digest_config(self, kwargs, locals())
        super().__init__(**kwargs)

        self.read_data(data)
        self.setup_axes()   #x, y axis
        self.add_lines()    # background line and value text
        self.add_titles()
        self.add_bars()     # draw rectangle
        self.add_bar_names()    # name of bars below x_axis
        self.add_axes_titles()  # x/y axis title

    def read_data(self, data):
        # data = [("A", 10, RED), ...]
        if len(data) == 0:
            return

        self.bar_names = [d[0] for d in data]
        self.bar_values = [d[1] for d in data]
        self.bar_colors = [d[2] for d in data]


    def setup_axes(self):
        # 1. generate x_axis, y_axis (not display itself)
        x_axis = NumberLine(
            x_min=self.x_min,
            x_max=self.x_max,
            unit_size=self.x_axis_length / 100,
        )
        x_axis.shift(self.graph_origin - x_axis.number_to_point(0))

        y_axis = NumberLine(
            x_min=self.y_min,
            x_max=self.y_max,
            unit_size=self.y_axis_length / (self.y_max - self.y_min),
        )
        y_axis.shift(self.graph_origin - y_axis.number_to_point(0))
        y_axis.rotate(np.pi / 2, about_point=y_axis.number_to_point(0))  # to y_min

        self.x_axis = x_axis
        self.y_axis = y_axis

    def add_lines(self):
        def get_num_text(val):
            num=0
            if self.y_labels_decimal_places == 0:
                num = int(round(val))    # no floating point i.e 2
            else:
                num = round(val, self.y_labels_decimal_places)
            return Text(str(num), stroke_width=0, color=self.y_labels_color, size=self.y_labels_size)

        lines = VGroup()
        line_texts = VGroup()
        for y in np.arange(self.y_min, self.y_max+(self.y_tick_frequency/2), self.y_tick_frequency):
            sp = self.x_axis.number_to_point(self.x_min) * RIGHT
            sp += self.y_axis.number_to_point(y) * UP

            ep = self.x_axis.number_to_point(self.x_max) * RIGHT
            ep += self.y_axis.number_to_point(y) * UP

            line = Line(sp, ep, buff=0, color=GREY)
            line_text = get_num_text(y)
            line_text.next_to(sp, LEFT, buff=self.y_labels_buff)

            line_texts.add(line_text)
            lines.add(line)

        self.lines, self.line_texts = lines, line_texts
        self.add(self.lines, self.line_texts)

    def add_titles(self):
        if self.title == None:
            return

        if self.title_font == None:
            title_text = Text(self.title, stroke_width=0, color=self.title_color, size=self.title_size)
        else:
            title_text = Text(self.title, stroke_width=0, color=self.title_color, size=self.title_size, font=self.title_font)

        title_text.next_to(self.lines[-1], UP, buff=self.title_buff)

        self.title_text = title_text
        self.add(self.title_text)

    def add_bars(self):
        # n: number of bars, l:x_axis lenght, e: start/end edge, r: gap/width
        # Basic Idea: l = nw + (n-1)g + 2e  and w=rg
        def cal_width(n, l, e, r):
            w = (l - 2*e) / (n + r*n - r)
            g = r*w
            return (w, g)

        def cal_height():
            zero_point = self.y_axis.number_to_point(0)
            return [(self.y_axis.number_to_point(val) - zero_point)[1] for val in self.bar_values]

        def get_bar(idx, val, bar_w, bar_h):
            return Bar(id=idx, num_val=val, width=bar_w, height=bar_h,
                       decimal_position=self.bar_values_position, decimal_buff=self.bar_values_buff,
                       fill_color=self.bar_colors[idx], fill_opacity=self.bar_fill_opacity,
                       )

        #1. calculate the width/height for the bars and make bars
        bar_cnt = len(self.bar_names)
        bar_w, gap  = cal_width(bar_cnt, self.x_axis_length, self.edge_buff, self.gap_ratio)
        bar_h_list = cal_height()

        bars = VGroup(*[get_bar(idx, val, bar_w, bar_h)
                        for (idx, val), bar_h in zip(enumerate(self.bar_values), bar_h_list)])

        #2. arrange bars onto the axes
        bars.arrange(RIGHT, aligned_edge=DOWN ,buff=gap)
        shift_down_val = (bars.get_bottom() - self.x_axis.get_start())[1]
        shift_left_val = (bars.get_left() - self.x_axis.get_start())[0] - self.edge_buff
        bars.shift(DOWN * shift_down_val + LEFT * shift_left_val)

        self.bar_heights = bar_h_list
        self.bars = bars
        if self.is_add_bars:  # otherwise animates the bars with get_bar_animation
            self.add(self.bars)

    def add_bar_names(self):
        def get_bar_names_text(str):
            return Text(str, stroke_width=0, size=self.bar_names_size, color=self.bar_names_color)

        bar_texts = VGroup(*[get_bar_names_text(name) for name in self.bar_names])

        for idx, bar_text in enumerate(bar_texts):
            bar_text.next_to(self.bars[idx], DOWN, buff=self.bar_names_buff)

        self.bar_texts = bar_texts
        self.add(self.bar_texts)


    def add_axes_titles(self):

        def get_x_text(str):
            return Text(str, stroke_width=0, color=self.x_axis_title_color, size=self.x_axis_title_size)

        def get_y_text(str):
            t = Text(str, stroke_width=0, color=self.y_axis_title_color, size=self.y_axis_title_size)
            return t.rotate(90 * DEGREES)

        x_title = get_x_text(self.x_axis_title)
        y_title = get_y_text(self.y_axis_title)

        x_title.next_to(self.bar_texts, DOWN, buff=self.x_axis_title_buff)
        y_title.next_to(self.line_texts, LEFT, buff=self.y_axis_title_buff)

        self.x_title, self.y_title = x_title, y_title
        self.add(self.x_title, self.y_title)

    def get_bar_animation(self, ani_type='GrowFromBottomLine', lag_ratio=0.2, run_time=4):
        group = AnimationGroup()

        # function for GrowFromBottom animation
        def func(bar, alpha):
            # should be avoid zero case. if zero never displyed
            tgt_h = self.bar_heights[bar.id] * alpha + 0.01
            tgt_val = self.bar_values[bar.id] * alpha

            new_bar = bar.set_value_height(tgt_val, tgt_h)
            bar.become(new_bar)

        if ani_type == 'GrowFromEdgePoint':  # grow from bottom point
            group = AnimationGroup(
                *[GrowFromEdge(bar, edge=DOWN) for bar in self.bars],
                lag_ratio = lag_ratio,
                run_time=run_time,
            )
        elif ani_type == 'GrowFromBottomLine': # grow from bottom line
            group = AnimationGroup(
                # *[UpdateFromAlphaFunc(bar, func, remover=True) for bar in self.bars],
                *[UpdateFromAlphaFunc(bar, func) for bar in self.bars],
                lag_ratio=lag_ratio,
                run_time=run_time,
            )

        self.animation_group = group
        return group

    def remove_bars(self, scene):
        scene.remove(self.animation_group.get_all_mobjects())

    def fadeout_bars(self, scene, run_time=1):
        scene.play(FadeOut(self.animation_group.get_all_mobjects()), run_time=run_time)


# Bar = (rectangle + decimal) with id
class Bar(VGroup):
    CONFIG ={
        "width": 1.0,
        "height": 2.5,

        "fill_color": RED,
        "fill_opacity": 1,
        "stroke_width": 0,
        "stroke_opacity": 0,
        "stroke_color": GREY,

        "decimal_scale": 0.8,
        "decimal_color": YELLOW,
        "decimal_buff": 0.3,
        "decimal_position": UP,
        "num_decimal_places": 0,

        "id": 0,
        "num_val": 10,
    }

    def __init__(self, id=0, num_val=10, **kwargs):
        # digest_config(self, kwargs, locals())
        super().__init__(**kwargs)
        self.id = id
        self.num_val = num_val
        self.generate_objects()

    def generate_objects(self):
        #1. rectangle
        rect = Rectangle(
            width=self.width, height=self.height, fill_color=self.fill_color, fill_opacity=self.fill_opacity,
            stroke_opacity=self.stroke_opacity, stroke_color=self.stroke_color,
        )
        self.add(rect)

        #2. decimal number
        decimal = DecimalNumber(number=self.num_val, color=self.decimal_color, num_decimal_places=self.num_decimal_places,
                                background_stroke_color=self.decimal_color, background_stroke_opacity=0.4)
        decimal.scale(self.decimal_scale)

        self.move_decimal_pos(decimal, rect)
        self.add(decimal)

        self.rect = rect
        self.decimal = decimal

    def set_value_height(self, decimal_value, rect_height ):
        self.rect.set_height(rect_height, stretch=True, about_edge=DOWN)
        self.decimal.set_value(decimal_value)

        self.move_decimal_pos(self.decimal, self.rect)
        return self

    # move decimal to rect according to decimal_position. Reason to make method: called twice in other place
    def move_decimal_pos(self, decimal, rect):
        decimal.next_to(rect.get_top(), self.decimal_position, buff=self.decimal_buff)