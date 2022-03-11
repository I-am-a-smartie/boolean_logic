from manim import *


class comp(Scene):
    def construct(self):
        law = Tex('Complementarity Law')
        one = MathTex("X + \overline{X} = 1")
        one.move_to(UP * 1)
        two = MathTex('X.\overline{X} = 1')
        main_group = VGroup(one, two)
        self.play(Write(law))
        self.play(law.animate.shift(UP * 3))
        self.play(Write(one))
        self.play(Write(two))
        self.wait(2)

        law.scale(0.8)
        main_group.generate_target()
        main_group.target.scale(0.8)
        main_group.target.to_corner(UL*3)
        self.play(MoveToTarget(main_group), law.animate.to_corner(UL))
        self.wait(2)

        OR = Tex('. signifies AND')
        OR.move_to(UP * 1)
        AND = Tex("+ signifies OR")
        values = Tex('Values of X can be 0 or 1')
        values.move_to(DOWN * 1)
        rules = VGroup(OR, AND, values)
        rules.scale(0.7)
        rules.to_corner(DL)
        self.play(FadeIn(rules))
        self.wait(2)

        two_tt = Table(
            [["0", "1", "1"],
             ["1", "0", "1"]],
            col_labels=[MathTex("X"), MathTex("\overline{X}"), MathTex('X + \overline{X}')]
        )
        two_tt.scale(0.9)
        self.play(Create(two_tt))
        self.wait(2)
        fb3 = SurroundingRectangle(two_tt.get_rows()[1])
        x5 = MathTex('X \\ = \\ 0')
        x5.move_to(RIGHT * 6)
        x6 = MathTex('\overline{X} = 1')
        x6.next_to(x5, DOWN * 1.5)
        self.play(Write(fb3), Write(x5), Write(x6))
        xplusx3 = VGroup(MathTex('X + \overline{X}'), Tex('= 0 or 1'), Tex('= 1'))
        xplusx3.next_to(x6, DOWN * 3)
        xplusx3[1].next_to(xplusx3[0], DOWN * 1)
        xplusx3[2].next_to(xplusx3[1], DOWN * 1)
        self.play(Write(xplusx3[0]))
        self.wait(1)
        self.play(Write(xplusx3[1]))
        self.wait(1)
        self.play(Write(xplusx3[2]))
        self.wait(1)

        fb4 = SurroundingRectangle(two_tt.get_rows()[2])
        x7 = MathTex('X \\ = \\ 1')
        x7.move_to(RIGHT * 6)
        x8 = MathTex('\overline{X} = 1')
        x8.next_to(x7, DOWN * 1.5)
        self.play(
            Uncreate(x5),
            Uncreate(x6),
            Uncreate(xplusx3)
        )
        self.play(ReplacementTransform(fb3, fb4), Write(x7), Write(x8))
        xplusx4 = VGroup(MathTex('X + \overline{X}'), Tex('= 1 or 1'), Tex('= 1'))
        xplusx4.next_to(x8, DOWN * 3)
        xplusx4[1].next_to(xplusx4[0], DOWN * 1)
        xplusx4[2].next_to(xplusx4[1], DOWN * 1)
        self.play(Write(xplusx4[0]))
        self.wait(1)
        self.play(Write(xplusx4[1]))
        self.wait(1)
        self.play(Write(xplusx4[2]))
        self.wait(1)

        self.play(
            Uncreate(x7),
            Uncreate(x8),
            Uncreate(xplusx4),
            Uncreate(two_tt),
            Uncreate(fb4)
        )
        self.wait(2)

        two_tt = Table(
            [["0", "1", "1"],
             ["1", "0", "1"]],
            col_labels=[MathTex("X"), MathTex("\overline{X}"), MathTex('X . \overline{X}')]
        )
        two_tt.scale(0.9)
        self.play(Create(two_tt))
        self.wait(2)
        fb3 = SurroundingRectangle(two_tt.get_rows()[1])
        x5 = MathTex('X \\ = \\ 0')
        x5.move_to(RIGHT * 6)
        x6 = MathTex('\overline{X} = 1')
        x6.next_to(x5, DOWN * 1.5)
        self.play(Write(fb3), Write(x5), Write(x6))
        xplusx3 = VGroup(MathTex('X . \overline{X}'), Tex('= 0 and 1'), Tex('= 1'))
        xplusx3.next_to(x6, DOWN * 3)
        xplusx3[1].next_to(xplusx3[0], DOWN * 1)
        xplusx3[2].next_to(xplusx3[1], DOWN * 1)
        self.play(Write(xplusx3[0]))
        self.wait(1)
        self.play(Write(xplusx3[1]))
        self.wait(1)
        self.play(Write(xplusx3[2]))
        self.wait(1)

        fb4 = SurroundingRectangle(two_tt.get_rows()[2])
        x7 = MathTex('X \\ = \\ 1')
        x7.move_to(RIGHT * 6)
        x8 = MathTex('\overline{X} = 1')
        x8.next_to(x7, DOWN * 1.5)
        self.play(
            Uncreate(x5),
            Uncreate(x6),
            Uncreate(xplusx3)
        )
        self.play(ReplacementTransform(fb3, fb4), Write(x7), Write(x8))
        xplusx4 = VGroup(MathTex('X + \overline{X}'), Tex('= 1 and 1'), Tex('= 1'))
        xplusx4.next_to(x8, DOWN * 3)
        xplusx4[1].next_to(xplusx4[0], DOWN * 1)
        xplusx4[2].next_to(xplusx4[1], DOWN * 1)
        self.play(Write(xplusx4[0]))
        self.wait(1)
        self.play(Write(xplusx4[1]))
        self.wait(1)
        self.play(Write(xplusx4[2]))
        self.wait(1)

        self.play(
            Uncreate(x7),
            Uncreate(x8),
            Uncreate(xplusx4),
            Uncreate(two_tt),
            Uncreate(fb4)
        )
        self.wait(2)
