from manim import *


class properties(Scene):
    def construct(self):
        law = Tex('Properties of 0 and 1')
        one = Tex('0 + X = X')
        one.move_to(UP * 1.5)
        two = Tex('1 + X = 1')
        two.move_to(UP * 0.5)
        three = Tex('0.X = 0')
        three.move_to(DOWN * 0.5)
        four = Tex('1.X = 1')
        four.move_to(DOWN * 1.5)
        main_group = VGroup(law, one, two, three, four)

        self.play(Write(law))
        self.play(law.animate.shift(UP * 3))
        self.play(Write(one))
        self.play(Write(two))
        self.play(Write(three))
        self.play(Write(four))
        self.wait(2)

        main_group.generate_target()
        main_group.target.scale(0.7)
        main_group.target.to_corner(UL)
        self.play(MoveToTarget(main_group))
        self.wait(2)

        OR = Tex('. signifies AND')
        OR.move_to(UP * 1)
        AND = Tex("+ signifies OR")
        # AND.move_to(UP * 1)
        values = Tex('Values of X can be 0 or 1')
        values.move_to(DOWN * 1)
        rules = VGroup(OR, AND, values)
        rules.scale(0.7)
        rules.to_corner(DL)
        self.play(FadeIn(rules))
        self.wait(2)

        one_main = Tex('0 + X = X')
        one_main.to_corner(UR)
        self.play(ReplacementTransform(one.copy(), one_main))
        # class tt(Scene):
        #     def construct(self):
        one_tt = Table(
            [["0", "0", "0"],
             ["1", "1", "1"]],
            col_labels=[Text("0"), Text("X"), Text('R')])
        # one_tt.move_to(UP*2)
        # one_tt.scale(0.8)

        self.play(Create(one_tt))
        self.wait(2)
        l1 = Tex('R = 0 + X')
        l1.to_corner(UR * 3)
        l2 = Tex('= 0 or 0')
        l2.next_to(l1, DOWN * 1)
        l3 = Tex('= 0')
        l3.next_to(l2, DOWN * 1)
        l4 = Tex('= X')
        l4.next_to(l3, DOWN * 1)
        fb1 = SurroundingRectangle(one_tt.get_rows()[1])
        self.play(
            Write(fb1),
            Write(l1)
        )
        self.play(Write(l2))
        self.play(Write(l3))
        self.play(Write(l4))
        self.wait(2)

        l5 = l1.copy()
        l5.next_to(l1, DOWN * 9)
        l6 = Tex('= 0 or 1')
        l6.next_to(l5, DOWN * 1)
        l7 = Tex('= 1')
        l7.next_to(l6, DOWN * 1)
        l8 = Tex('= X')
        l8.next_to(l7, DOWN * 1)
        fb2 = SurroundingRectangle(one_tt.get_rows()[2])
        self.play(
            ReplacementTransform(fb1, fb2),
            Write(l5)
        )
        self.play(Write(l6))
        self.wait(1)
        self.play(Write(l7))
        self.wait(1)
        self.play(Write(l8))
        self.wait(2)

        two_main = Tex('1 + X = 1')
        two_main.to_corner(UR)

        two_tt = Table(
            [["1", "0", "1"],
             ["1", "1", "1"]],
            col_labels=[Text("1"), Text("X"), Text('R')])

        self.play(ReplacementTransform(two.copy(), two_main), ReplacementTransform(one_tt, two_tt), Unwrite(one_main),
                  Unwrite(l1), Unwrite(l2), Unwrite(l3), Unwrite(l4), Unwrite(l5), Unwrite(l6), Unwrite(l7),
                  Unwrite(l8), Unwrite(fb2))
        self.wait(2)

        l11 = Tex('R = 1 + X')
        l11.to_corner(UR * 3)
        l12 = Tex('= 1 or 0')
        l12.next_to(l1, DOWN * 1)
        l13 = Tex('= 1')
        l13.next_to(l2, DOWN * 1)
        fb3 = SurroundingRectangle(two_tt.get_rows()[1])
        self.play(
            Write(fb3),
            Write(l11)
        )
        self.play(Write(l12))
        self.play(Write(l13))
        self.wait(2)

        l15 = l11.copy()
        l15.next_to(l11, DOWN * 9)
        l16 = Tex('= 0 or 1')
        l16.next_to(l15, DOWN * 1)
        l17 = Tex('= 1')
        l17.next_to(l16, DOWN * 1)
        fb4 = SurroundingRectangle(two_tt.get_rows()[2])
        self.play(
            ReplacementTransform(fb3, fb4),
            Write(l15)
        )
        self.play(Write(l16))
        self.wait(1)
        self.play(Write(l17))
        self.wait(2)

        three_main = Tex('0.X = 0')
        three_main.to_corner(UR)

        three_tt = Table(
            [["0", "0", "0"],
             ["0", "1", "0"]],
            col_labels=[Text("0"), Text("X"), Text('R')])

        self.play(ReplacementTransform(three.copy(), three_main), ReplacementTransform(two_tt, three_tt),
                  Unwrite(two_main), Unwrite(l11), Unwrite(l12), Unwrite(l13), Unwrite(l15), Unwrite(l16), Unwrite(l17),
                  Unwrite(fb4))
        self.wait(2)

        l21 = Tex('R = 1 + X')
        l21.to_corner(UR * 3)
        l22 = Tex('= 0 and 0')
        l22.next_to(l1, DOWN * 1)
        l23 = Tex('= 0')
        l23.next_to(l2, DOWN * 1)
        fb5 = SurroundingRectangle(three_tt.get_rows()[1])
        self.play(
            Write(fb5),
            Write(l21)
        )
        self.play(Write(l22))
        self.play(Write(l23))
        self.wait(2)

        l25 = l21.copy()
        l25.next_to(l21, DOWN * 9)
        l26 = Tex('= 0 and 1')
        l26.next_to(l25, DOWN * 1)
        l27 = Tex('= 0')
        l27.next_to(l26, DOWN * 1)
        fb6 = SurroundingRectangle(three_tt.get_rows()[2])
        self.play(
            ReplacementTransform(fb5, fb6),
            Write(l25)
        )
        self.play(Write(l26))
        self.wait(1)
        self.play(Write(l27))
        self.wait(2)

        four_main = Tex('1.X = 1')
        four_main.to_corner(UR)

        four_tt = Table(
            [["1", "0", "1"],
             ["1", "1", "1"]],
            col_labels=[Text("1"), Text("X"), Text('R')])

        self.play(ReplacementTransform(four.copy(), four_main), ReplacementTransform(three_tt, four_tt),
                  Unwrite(three_main), Unwrite(l21), Unwrite(l22), Unwrite(l23), Unwrite(l25), Unwrite(l26),
                  Unwrite(l27), Unwrite(fb6))
        self.wait(2)

        l31 = Tex('R = 1 + X')
        l31.to_corner(UR * 3)
        l32 = Tex('= 0 and 0')
        l32.next_to(l31, DOWN * 1)
        l33 = Tex('= 0')
        l33.next_to(l32, DOWN * 1)
        fb7 = SurroundingRectangle(four_tt.get_rows()[1])
        self.play(
            Write(fb7),
            Write(l31)
        )
        self.play(Write(l32))
        self.play(Write(l33))
        self.wait(2)

        l35 = l31.copy()
        l35.next_to(l31, DOWN * 9)
        l36 = Tex('= 1 and 1')
        l36.next_to(l35, DOWN * 1)
        l37 = Tex('= 1')
        l37.next_to(l36, DOWN * 1)
        fb8 = SurroundingRectangle(four_tt.get_rows()[2])
        self.play(
            ReplacementTransform(fb7, fb8),
            Write(l35)
        )
        self.play(Write(l36))
        self.wait(1)
        self.play(Write(l37))
        self.wait(2)
