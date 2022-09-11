from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import funtras


class MainApp(App):
    def build(self):
        self.xoperators = ["senh(x)", "cosh(x)", "tanh(x)", "asen(x)", "acos(x)", "atan(x)",
                           "sec(x)", "csc(x)", "cot(x)", "sen(x)", "cos(x)", "tan(x)", "ln(x)", "log10(x)",
                           "1/x", "rx", "exp(x)", "x!"]
        self.xyoperators = ["logy(x)", "yrx", "x*y", "x+y", "x-y", "x/y"]
        self.last_was_xoperator = None
        self.last_was_xyoperator = None
        self.last_button = ""
        self.xyop = False
        self.x = ""
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=25
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["senh(x)", "cosh(x)", "tanh(x)"],
            ["asen(x)", "acos(x)", "atan(x)"],
            ["sec(x)", "csc(x)", "cot(x)"],
            ["sen(x)", "cos(x)", "tan(x)"],
            ["ln(x)", "log10(x)", "logy(x)"],
            ["1/x", "rx", "yrx"],
            ["exp(x)", "x*y", "x!"],
            ["x+y", "x-y", "x/y"],
            ["7", "8", "9"],
            ["4", "5", "6"],
            ["1", "2", "3"],
            ["CLR", "0", "."],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        equals_button.bind(on_press=self.on_solution)

        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        self.current = self.solution.text
        self.button_text = instance.text
        op = False

        print("LAST BUTTON " + self.last_button)
        print("LAST WAS OPERATOR " + str(self.last_was_xoperator))

        if self.button_text == "CLR":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if self.current and (self.last_was_xoperator and self.button_text in (self.xoperators or self.xyoperators)):
                # Don't add two operators right after each other
                return
            elif (self.current == "" or self.last_button == "") and self.button_text in (self.xoperators or self.xyoperators):
                # First character cannot be an operator
                return
            elif self.button_text in self.xyoperators:
                self.xyop = True
            elif self.button_text in self.xoperators:

                try:
                    self.choose_operation(self.last_button)
                except OverflowError as oe:
                    self.solution.text = "OVERFLOW"
                op = True
            elif self.xyop and (self.button_text not in (self.xyoperators or self.xoperators)):
                print("x " + self.x)
                self.choose_xyoperation(self.x, self.button_text)
                self.xyop = False
            else:
                new_text = self.current + self.button_text
                self.solution.text = new_text
        if not op:
            if self.xyop:
                self.x = self.last_button
            self.last_button = self.button_text
            self.last_was_xoperator = (self.last_button in self.xoperators) or (self.last_button in self.xyoperators)



        print("BUTTON TEXT " + self.button_text)
        print("SOLUTION TEXT " + self.solution.text)
        print("op " + str(op))
        print("xyop " + str(self.xyop))
        print("\n\n")


    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(self.choose_operation(text))
            self.solution.text = solution

    def choose_operation(self, text):
        soltext = "-1"
        match self.button_text:
            case "sen(x)":
                soltext = str(funtras.sin_t(float(text)))
            case "cos(x)":
                soltext = str(funtras.cos_t(float(text)))
            case "tan(x)":
                soltext = str(funtras.tan_t(float(text)))
            case "senh(x)":
                soltext = str(funtras.sinh_t(float(text)))
            case "cosh(x)":
                soltext = str(funtras.cosh_t(float(text)))
            case "tanh(x)":
                soltext = str(funtras.tanh_t(float(text)))
            case "asen(x)":
                soltext = str(funtras.asin_t(float(text)))
            case "acos(x)":
                soltext = str(funtras.asin_t(float(text)))  # FALTA !!!!!
            case "atan(x)":
                soltext = str(funtras.atan_t(float(text)))
            case "sec(x)":
                soltext = str(funtras.sec_t(float(text)))
            case "csc(x)":
                soltext = str(funtras.csc_t(float(text)))
            case "cot(x)":
                soltext = str(funtras.cot_t(float(text)))
            case "ln(x)":
                soltext = str(funtras.ln_t(float(text)))
            case "log10(x)":
                soltext = str(funtras.log_t(float(text), 10))
            case "1/x":
                soltext = str(funtras.div_t(float(text)))
            case "rx":
                soltext = str(funtras.root_t(float(text), 2))
            case "exp(x)":
                soltext = str(funtras.exp_t(float(text)))
            case "x!":
                try:
                    x = int(text)
                    soltext = str(funtras.fact(x))
                except ValueError as ve:
                    soltext = "INVALID TYPE"
            case _:
                soltext = "-1"

        if soltext == "inf":
            soltext = "MATH ERROR"
        self.current = soltext
        self.last_button = self.current
        self.last_was_xoperator = False
        self.button_text = soltext
        self.solution.text = soltext


    def choose_xyoperation(self, x, text):
        soltext = "-1"
        match self.last_button:
            case "logy(x)":
                soltext = str(funtras.log_t(float(text), float(x)))
            case "yrx":
                soltext = str(funtras.root_t(float(text), float(x)))
            case "x*y":
                soltext = "multi"
                # soltext = str(funtras.log_t(float(text), float(x)))
            case "x+y":
                soltext = "suma"
                # soltext = str(funtras.log_t(float(text), float(x)))
            case "x-y":
                soltext = "resta"
                # soltext = str(funtras.log_t(float(text), float(x)))
            case "x/y":
                soltext = "divi"
                # soltext = str(funtras.log_t(float(text), float(x)))
            case _:
                soltext = "uwu"
        if soltext == "inf":
            soltext = "MATH ERROR"
        self.current = soltext
        self.last_button = self.current
        self.last_was_xoperator = False
        self.button_text = soltext
        self.solution.text = soltext




if __name__ == "__main__":
    app = MainApp()
    app.run()