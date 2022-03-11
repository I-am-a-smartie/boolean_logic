from manim import*

class intro(Scene):
    def construct(self):
        title = Tex("DeMorgan's Second Theorem")
        self.play(Write(title))
        self.wait()
        self.play(title.animate.shift(UP * 3.5))
        LHS = MathTex("\overline{X.Y} =")
        self.play(Write(LHS))
        self.play(LHS.animate.shift(LEFT * 0.5))
        #transform while moving
        RHS = MathTex("\overline{X.Y}")
        RHS.move_to(LEFT*0.5)
        fRHS = MathTex("\overline{X}" '+' "\overline{Y}")
        fRHS.move_to(LEFT*0.5)
        self.play(Transform(RHS, fRHS), fRHS.animate.shift(RIGHT*1))
        #Transform(RHS, fRHS)
        #self.play(fRHS.animate.shift(RIGHT * 1.25))
        #formula = VGroup(LHS, fRHS)
        #formula.generate_target()
        #formula.target.to_corner(UP*0.5)
        #formula.target.to_corner(RIGHT * 3)
        #self.play(title.animate.shift(LEFT*3), MoveToTarget(formula))
        self.play(FadeOut(LHS, RHS, title))

class border(Scene):
    def construct(self):
        formula = MathTex("\overline{X.Y} = \overline{X} + \overline{Y}")
        formula.to_corner(UR)
        title = Tex("DeMorgan's Second Theorem")
        title.to_corner(UL)
        self.play(Write(title))
        self.play(Write(formula))
        values = Tex('Values of X and Y can be 0 or 1')
        self.play(Write(values))
        self.wait()
        self.play(values.animate.shift(UP*1))
        OR = Tex('. signifies AND')
        self.play(Write(OR))
        self.wait()
        #self.play(OR.animate.shift(UP*1), values.animate.shift(UP*1))
        AND = Tex("+ signifies OR")
        AND.move_to(DOWN*1)
        self.play(Write(AND))
        self.wait()
        rules = VGroup(values, OR, AND)
        rules.generate_target()
        rules.target.scale(0.7)
        rules.target.to_corner(UP * 3)
        rules.target.to_corner(LEFT * 1.5)
        self.play(MoveToTarget(rules))
        #table in left bottom, right side we do lhs and top and rhs down when we show lhs, that block glows and so on
        #too fast? let's go slow

#class truthtable(Scene):
 #   def construct(self):
        truthtable = Table(
            [["0", "0", "1", "1"],
             ["1", "1", "1", "1"],
             ["0", "1", "0", "0"],
             ["1", "0", "0", "0"]],
            col_labels=[Text("X"), Text("Y"), MathTex("\overline{X.Y}"), MathTex("\overline{X} + \overline{Y}")])
        truthtable.scale(0.6)
        truthtable.to_corner(DL)
        self.play(truthtable.animate)
        wot = Text("wOt??")
        wot.move_to(RIGHT*3)
        self.play(FadeIn(wot))
        self.wait()
        #after this ask why other combos not in table? cuz its the same
        dw = Tex("Don't worry")
        dw.move_to(RIGHT*3)
        self.play(ReplacementTransform(wot, dw))
        self.wait()
        self.play(FadeOut(dw))
        fb1 = SurroundingRectangle(truthtable.get_entries((2, 1)))
        x21 = Tex("X = 0")
        x21.move_to(RIGHT*3)
        self.play(Create(fb1), Write(x21))
        self.play(x21.animate.shift(UP*1.35))
        self.wait(2)

        fb2 = SurroundingRectangle(truthtable.get_entries((2, 2)))
        x22 = Tex("Y = 0")
        x22.move_to(RIGHT * 3)
        self.play(ReplacementTransform(fb1, fb2), Write(x22))
        self.play(x22.animate.to_corner(UR * 5), x21.animate.shift(LEFT * 2))
        self.wait(2)

        fb3 = SurroundingRectangle(truthtable.get_entries((2, 3)))

#class layer1(Scene):
 #   def construct(self):
        x23 = MathTex("\overline{X.Y}")
        x23.move_to(RIGHT * 3)
        exp231 = MathTex("=\ \overline{ X \ and \ Y}")
        exp231.next_to(x23, DOWN * 1.5)
        exp232 = MathTex("=\ \overline{ 0 \ and \ 0}")
        exp232.next_to(exp231, DOWN * 1.5)
        exp233 = MathTex("=\ \overline{0}")
        exp233.next_to(exp231, DOWN * 4.5)
        exp234 = MathTex("=\ 1")
        exp234.next_to(exp231, DOWN * 7)
        exp23 = VGroup(exp231, exp232, exp233, exp234)#.arrange_in_grid(cols=3, buff=0.1)


        self.play(ReplacementTransform(fb2, fb3), Write(x23))
        #self.play(Write(x23))

        for i in range(0,4):
            self.wait(3)
            self.play(Write(exp23[i]))
        self.wait(2)

        self.play(exp23.animate.shift(LEFT*1.5), x23.animate.shift(LEFT*1.5))
        #transform lhs and rhs at the same time, looks like they come together to form it or convert to
        #words lhs = rhs or bring zeroes to centre add equals and then convert to lhs and rhs, transform to header
        #then fade it out and go all over again:))))

        fb4 = SurroundingRectangle(truthtable.get_entries((2, 4)))
        x24 = MathTex("\overline{X} \ + \ \overline{Y}")
        x24.move_to(RIGHT * 5)
        exp241 = MathTex("= \ \overline{0} \ or \ \overline{0}")
        exp241.next_to(x24, DOWN * 1.5)
        exp242 = MathTex("= \ 1 \ or \ 1")
        exp242.next_to(exp241, DOWN * 1.5)
        exp243 = MathTex("= \ 1")
        exp243.next_to(exp241, DOWN * 4.5)

        exp24 = VGroup(exp241, exp242, exp243)
        self.play(ReplacementTransform(fb3, fb4), Write(x24))
        #self.play(Write(exp24))
        for j in range(0,3):
            self.wait(3)
            self.play(Write(exp24[j]))

        self.wait(2)

        endL = Tex('LHS')
        endR = Tex('RHS')
        end = VGroup(endL, endR)
        end.scale(0.7)
        endL.next_to(exp234, RIGHT*5.5)
        endR.next_to(exp243, DOWN*1.4)
        eq = Tex('=')
        self.play(ReplacementTransform(exp234.copy(), endL), ReplacementTransform(exp243.copy(), endR))
        eq.next_to(endL, RIGHT*0.79)
        self.play(Write(eq))
        end = VGroup(endL, endR, eq)
        endfb = SurroundingRectangle(end)
        self.play(Create(endfb))
        self.wait(5)

        self.play(Uncreate(x21), Uncreate(x22), Uncreate(exp232), Uncreate(exp233), Uncreate(exp234), Uncreate(exp242), Uncreate(exp243), Uncreate(end), Uncreate(endfb))
        self.wait(1)
        share = Tex('Share your answers!')
        share.next_to(AND, RIGHT*15)
        self.play(Write(share))

