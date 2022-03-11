from manim import *


class AssociativeLaw(Scene):
    def construct(self):
        text = MathTex("(X + Y) + Z =")
        self.play(Write(text))

        self.play(ApplyMethod(text.shift, LEFT * 1.5), run_time=3)
        text2 = MathTex("(", "X", "+", "Y", ")", "+", "Z", "=")
        text2.move_to(LEFT * 1.5)
        self.play(text2[1].animate.shift(RIGHT * 3.4))
        self.play(text2[2].animate.shift(RIGHT * 3.4))
        self.play(text2[3].animate.shift(RIGHT * 3.5))
        self.play(text2[5].animate.shift(RIGHT * 3.3))
        self.play(text2[6].animate.shift(RIGHT * 3.3))
        self.play(text2[0].animate.shift(RIGHT * 4.555))
        self.play(text2[4].animate.shift(RIGHT * 4.5))
        self.wait(3)
        whole = VGroup(text, text2)
        whole.generate_target()
        whole.target.scale(0.7)
        whole.target.to_corner(UL)
        self.play(MoveToTarget(whole))

        text3 = MathTex("(XY) Z =")
        self.play(Write(text3))
        self.play(ApplyMethod(text3.shift, LEFT * 1), run_time=3)
        text4 = MathTex("(", "X", "Y", ")", "Z")
        text4.move_to(LEFT * 1)
        self.play(text4[1].animate.shift(RIGHT * 1.8))
        self.play(text4[2].animate.shift(RIGHT * 2))
        self.play(text4[4].animate.shift(RIGHT * 1.75))
        self.play(text4[0].animate.shift(RIGHT * 2.38))
        self.play(text4[3].animate.shift(RIGHT * 2.34))
        self.wait(3)
        whole2 = VGroup(text3, text4)
        whole2.generate_target()
        whole2.target.scale(0.7)
        whole2.target.to_corner(UR)
        self.play(MoveToTarget(whole2))
        self.wait(3)

        tt = Tex("Truth Tables")
        self.play(Write(tt))
        tt.generate_target()
        tt.target.next_to(text3, LEFT * 5)
        self.play(MoveToTarget(tt))

        table = Table(
            [["0", "0", '0', '0', '0', '0', '0'],
             ["0", "0", '1', '1', '0', '1', '1'],
             ["0", "1", '0', '1', '1', '1', '1'],
             ["0", "1", '1', '1', '1', '1', '1'],
             ["1", "0", '0', '0', '1', '1', '1'],
             ["1", "0", '1', '1', '1', '1', '1'],
             ["1", "1", '0', '1', '1', '1', '1'],
             ["1", "1", '1', '1', '1', '1', '1']],

            col_labels=[MathTex("X"), MathTex("Y"), MathTex("Z"), MathTex("X + Y"), MathTex("Y + Z"),
                        MathTex("(X + Y) + Z"), MathTex("X + (Y + Z)"), ],
            include_outer_lines=True)
        table.move_to(DOWN * 0.5)
        table.scale(0.5)
        self.play(Create(table))

        self.wait(5)
