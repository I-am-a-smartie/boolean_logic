from manim import*

class CommutativeLaw(Scene):
    def construct(self):
        head = Tex('Commutative Law')
        self.play(Write(head))
        self.play(head.animate.shift(UP*3))
        formula1 = Tex('X + Y = Y + X')
        formula1.move_to(UP*0.5)
        formula2 = Tex('X.Y = Y.X')
        formula2.move_to(DOWN*0.5)
        self.play(Write(formula1))
        self.play(Write(formula2))
        self.wait(3)
        formulae = VGroup(formula1, formula2)
        formulae.generate_target()
        formulae.target.scale(0.7)
        formulae.target.to_corner(UL*4)
        self.play(MoveToTarget(formulae), head.animate.shift(LEFT*4))

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

        one_tt = Table(
            [["0", "0", "0", "0"],
             ["0", "1", "1", "1"],
             ["1", "0", "1", "1"],
             ["1", "1", "1", "1"]],
            col_labels=[Tex("X"), Tex("Y"), Tex('X+Y'), Tex('Y+X')])
        one_tt.scale(0.8)
        one_tt.move_to(RIGHT*3)
        formula1main = Tex('X + Y = Y + X')
        formula1main.to_corner(UR)
        formula2main = Tex('X.Y = Y.X')
        formula2main.to_corner(UR)
        self.play(Write(one_tt), ReplacementTransform(formula1.copy(), formula1main))
        self.wait(5)
        self.play(Uncreate(one_tt), Uncreate(formula1main))

        two_tt = Table(
            [["0", "0", "0", "0"],
             ["0", "1", "0", "0"],
             ["1", "0", "0", "0"],
             ["1", "1", "1", "1"]],
            col_labels=[Tex("X"), Tex("Y"), Tex('X.Y'), Tex('Y.X')])
        two_tt.scale(0.8)
        two_tt.move_to(RIGHT*3)
        self.play(Write(one_tt), ReplacementTransform(formula2.copy(), formula2main))
        self.play(Write(two_tt))
#LHS fade in, move to get RHS, fade out