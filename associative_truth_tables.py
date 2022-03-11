from manim import*

class ALTT(Scene):
    def construct(self):
        tt = Tex("Truth Tables")
        self.play(Write(tt))
        self.play(tt.animate.shift(UP * 3.5))
        add = MathTex("(X + Y) + Z = X + (Y+Z)")
        mult = MathTex("(XY) Z = X (YZ)")
        add.move_to(UP*2.5)
        self.play(Write(add))

        table = Table(
            [["0", "0", '0', '0', '0', '0', '0'],
             ["0", "0", '1', '1', '0', '1', '1'],
             ["0", "1", '0', '1', '1', '1', '1'],
             ["0", "1", '1', '1', '1', '1', '1'],
             ["1", "0", '0', '0', '1', '1', '1'],
             ["1", "0", '1', '1', '1', '1', '1'],
             ["1", "1", '0', '1', '1', '1', '1'],
             ["1", "1", '1', '1', '1', '1', '1']],

            col_labels=[MathTex("X"), MathTex("Y"), MathTex("Z"), MathTex("X + Y"), MathTex("Y + Z"), MathTex("(X + Y) + Z"), MathTex("X + (Y + Z)"), ],
            include_outer_lines=True)
        table.move_to(DOWN*1)
        table.scale(0.5)
        for i in range(0,8):
            for j in range(0,9):
                self.play(Write(table.get_entries((i, j))))
                self.wait()
        #self.play(table.create(), run_time=10)
        #self.wait()
