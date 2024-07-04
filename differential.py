from manim import *

# class Move(Animation):
    # def __init__(self, number:)

class SecGraph(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()
        #Make  graph
        axes = Axes(
            x_range=(-10,10,1),
            y_range=(-1,9,1),
            x_length=10,
            y_length=5,
            axis_config={"tip_shape":StealthTip},
            # x_axis_config={"label":"$x$"},
            # y_axis_config={"label":"f(x)"},
        )
        label_x = Tex(r"$x$").next_to(axes.x_axis.get_end(), RIGHT)
        label_y = Tex(r"$f(x)$").next_to(axes.y_axis.get_end(), UP)
        graph =  axes.plot(
            lambda x: np.square(x), 
            color=YELLOW,
            x_range=[-3,3],
            )
        graph_title = Tex(r"$f(x)=x^2$")
        graph_title.scale(1.5)
        # graph_title.to_corner(UP + LEFT)

        tangent_line_dot = Dot(axes.i2gp(0, graph), color=BLUE)
        # a_line = Line(
        #     start=np.array([0.5,-2,0]),
        #     end=np.array([0.5,-1.5,0]),
        # )
        # b_line = Line(
        #     start=np.array([1,-2,0]),
        #     end=np.array([1,0,0]),
        # )


        self.play(Write(graph_title))
        self.wait(0.5)
        self.play(graph_title.animate.to_corner(UP+LEFT), run_time=1.5)
        self.play(
            # Write(axes), 
            Write(label_x), 
            Write(label_y), 
            Create(graph), 
            run_time=1.5)
        self.play(self.camera.frame.animate.scale(0.5).move_to(tangent_line_dot))

        # self.wait(0.5)
        # self.play(Create(func_graph),run_time=5)
        # self.wait(1)
        # self.play(Write(a_line), Write(b_line))
        # self.add(graph_title)
        # self.wait(1)
        # self.play(FadeOut(graph_title))
        # self.play(Create(func_graph_2))
        # self.add(graph_title_2)
        # self.wait(1)
        # self.play(FadeOut(graph_title_2))
        # self.play(Create(func_graph_3))
        # self.add(graph_title_3)
        # self.wait(2)

class FollowingGraphCamera(MovingCameraScene):
    def construct(self):
        self.camera.frame.save_state()

        # create the axes and the curve
        ax = Axes(x_range=[-1, 10], y_range=[-1, 10])
        graph = ax.plot(lambda x: np.sin(x), color=BLUE, x_range=[0, 3 * PI])

        # create dots based on the graph
        moving_dot = Dot(ax.i2gp(graph.t_min, graph), color=ORANGE)
        dot_1 = Dot(ax.i2gp(graph.t_min, graph))
        dot_2 = Dot(ax.i2gp(graph.t_max, graph))

        self.add(ax, graph, dot_1, dot_2, moving_dot)
        self.play(self.camera.frame.animate.scale(0.5).move_to(moving_dot))

        def update_curve(mob):
            mob.move_to(moving_dot.get_center())

        self.camera.frame.add_updater(update_curve)
        self.play(MoveAlongPath(moving_dot, graph, rate_func=linear))
        self.camera.frame.remove_updater(update_curve)

        self.play(Restore(self.camera.frame))