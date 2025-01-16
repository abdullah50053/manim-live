from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle() # creates a circle
        circle.set_fill(PINK, opacity=0.5) # setting color and transparecy
        self.play(Create(circle)) # Show circle on screen


transform a square into a circle
class SquaretoCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)

        circle = Circle()
        square.rotate(PI / 4)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))


class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello Hackers!")
        self.play(Write(text))
        self.wait(2)


class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        triangle.shift(RIGHT)

        self.play(Create(circle))
        self.play(Create(square))
        self.play(Create(triangle))
        self.wait(3)


class LatexExample(Scene):
    def construct(self):
        text = Text("Manim Latex Example")
        latex = MathTex("E = mc^2")

        text.shift(UP)
        latex.shift(DOWN)

        self.play(Write(text))
        self.play(Write(latex))
        self.wait(2)


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(LEFT*2)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(RIGHT*2)
        
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait(2)


class GraphingExample(Scene):
    def construct(self):
        axes = Axes (
            x_range = [-3, 3, 1],
            y_range = [-2, 2, 1],
        )

        graph = axes.plot(lambda x: x**2, color=BLUE)
        # graph_labels = axes.get_graph_label(graph)

        self.play(Create(axes), Create(graph))
        self.wait(2)


class ExplainLinearFunction(Scene):
    def construct(self):
        # Axis
        axes = Axes (
            x_range = [-10, 10, 1],
            y_range = [-10, 10, 1],
            x_length = 10,
            y_length = 6,
        )

        # Add the labels
        for x in range(-10, 11, 2):
            x_label = Text(f'{x}', font_size=18).next_to(axes.c2p(x, 0), DOWN, buff=0.1)
            self.add(x_label)

        for y in range(-10, 11, 2):
            y_label = Text(f'{y}', font_size=18).next_to(axes.c2p(0, y), LEFT, buff=0.1)
            self.add(y_label)

        # Axes labels
        x_axis_label = Text("x", font_size=24, color=WHITE).next_to(axes.x_axis.get_end(), RIGHT, buff=0.3)
        y_axis_label = Text("y", font_size=24, color=WHITE).next_to(axes.y_axis.get_end(), UP, buff=0.3)

        self.play(DrawBorderThenFill(axes), Write(x_axis_label), Write(y_axis_label))

        # Slope and y-intercept demo
        explanation_text = Text("Explaining y = mx + b", font_size=36, color=YELLOW)
        explanation_text.to_edge(UP)
        self.play(Write(explanation_text))

        # Line with m = 1, b = 2
        m = 1
        b = 2
        line = axes.plot(lambda x: m*x+b, x_range=[-10, 10], color=BLUE)
        line_label = Text("y = mx + b", font_size=24, color=BLUE).next_to(line, UP, buff=1)
        self.play(Create(line), Write(line_label))
        self.wait(1)

        # Show y - intercept
        b_dot = Dot(axes.c2p(0, b), color=GREEN)
        b_label = Text("y-intercept (b=2)", font_size=24, color=GREEN).next_to(b_dot, RIGHT)
        self.play(FadeIn(b_dot), Write(b_label))
        self.wait(2)

        # Show slope (m)
        slope_line = Line(axes.c2p(0, b), axes.c2p(1, m+b), color=ORANGE, stroke_width=4)
        slope_label = Text("Slope (m=1)", font_size=24, color=ORANGE).next_to(slope_line, UP, buff=0.2)
        self.play(Create(slope_line), Write(slope_label))
        self.wait(1)

        # Animate changing slope
        self.play(FadeOut(slope_line), FadeOut(slope_label))

        new_m = 2
        new_line = axes.plot(lambda x: new_m*x+b, x_range=[-10, 10], color=RED)
        new_slope_label = Text("Slope (m=2)", font_size=24, color=RED).to_edge(DOWN)

        self.play(Transform(line, new_line), Write(new_slope_label))
        self.wait(2)

        # End
        self.play(FadeOut(new_slope_label), FadeOut(b_label), FadeOut(b_dot), FadeOut(line), FadeOut(explanation_text), Uncreate(axes))
