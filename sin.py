from manim import *

TIME = 5

class SinCurve(Scene):
    def construct(self):
        # 関数定義
        # 点に円の周りを走らせる
        def go_around_circle(mob, dt):
            self.t_offset += (dt * rate)
            mob.move_to(circle.point_from_proportion(self.t_offset % 1))
        
        # 点から曲線までの直線を引く
        def get_line_to_curve():
            x = origin_point[1]+self.t_offset * 2 * np.pi
            y = dot.get_center()[1]
            return Line(dot.get_center(), ax.coords_to_point(x, y), color=YELLOW, stroke_width=3)
        

        # 変数等設定

        text = Tex(r"$\sin{}$ Curve").scale(2)
        # 軸を追加
        # 詳しくはManim公式ドキュメントのAxesまで
        ax = Axes(
            x_range=(-1, 7, np.pi/2),
            y_range=(-2,2,1),
            x_length=8,
            y_length=4,
            axis_config={"tip_shape":StealthTip},
        )
        ax.to_corner(RIGHT)

        # 軸に合わせてsinカーブを生成
        sincurve =  ax.plot(
            lambda x: np.sin(x), 
            color=YELLOW,
            x_range=[0,2 * np.pi],
            )

        # 各種ラベルなど
        origin = MathTex(r"\mathrm{O}").next_to(ax.coords_to_point(0,0), LEFT+DOWN)
        x_labels = [
            MathTex(r"\tfrac{\pi}{2}"), 
            MathTex(r"\pi"), 
            MathTex(r"\tfrac{3}{2}\pi"), 
            MathTex(r"2\pi")
        ]
        for i in range(len(x_labels)):
            x_labels[i].next_to(ax.coords_to_point(np.pi*(1+i)/2, 0), DOWN)

        # 原点
        origin_point = ax.coords_to_point(0,0)

        # 単位円
        circle = Circle(radius=1, color=BLUE).move_to(ax.coords_to_point(-2.5,0))

        # 円周上の点を表示
        dot = Dot(radius=0.08, color=YELLOW)
        # point_from_proportionを使うことでいい感じに周り動いてくれる
        dot.move_to(circle.point_from_proportion(0))
        # 時間関連の何か
        self.t_offset = 0
        # 上を制御するため的な
        rate = 1/TIME
        
        # 点とsinカーブを結ぶ直線
        dot_to_curve_line = always_redraw(get_line_to_curve)

        # アニメーション関連

        # 各要素を表示
        self.play(Write(text), run_time=2)
        self.wait(1)
        # self.play(text.animate.to_corner(UP + LEFT), run_time=1)
        self.play(
            Create(ax), 
            Write(origin), 
            Write(x_labels[0]),
            Write(x_labels[1]),
            Write(x_labels[2]),
            Write(x_labels[3]),
            FadeOut(text),
            Create(circle),
            Create(dot), 
            Create(dot_to_curve_line), 
            run_time=2
            )
        self.wait(0.5)
        
        dot.add_updater(go_around_circle)

        self.play(Create(sincurve), run_time=TIME, rate_func=linear)
        
        dot.remove_updater(go_around_circle)

        self.wait(1)

scene = SinCurve()
scene.render(preview=False)