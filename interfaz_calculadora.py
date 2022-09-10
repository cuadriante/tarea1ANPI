from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
import funtras


class MainApp(App):
    def build(self):
        self.xoperators = ["senh(x)", "cosh(x)", "tanh(x)", "asen(x)", "acos(x)", "atan(x)",
                           "sec(x)", "csc(x)", "cot(x)", "sen(x)", "cos(x)", "tan(x)", "ln(x)", "log10(x)",
                           "1/x", "rx", "exp(x)"]
        self.xyoperators = ["logy(x)", "yrx", "x*y"]
        self.last_was_xoperator = None
        self.last_was_xyoperator = None
        self.last_button = None
        self.xyop = False
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=35
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

        print(self.button_text)

        if self.button_text == "CLR":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if self.current and (self.last_was_xoperator and self.button_text in (self.xoperators or self.xyoperators)):
                # Don't add two operators right after each other
                return
            elif self.current == "" and self.button_text in (self.xoperators or self.xyoperators):
                # First character cannot be an operator
                return
            elif (self.button_text in self.xoperators) or self.xyop:
                try:
                    self.choose_operation(self.last_button)
                except OverflowError as oe:
                    self.solution.text = "OVERFLOW"
                op = True
            elif self.button_text in self.xyoperators:
                self.xyop = True
            else:
                new_text = self.current + self.button_text
                self.solution.text = new_text
        if not op:
            self.last_button = self.button_text
            self.last_was_xoperator = self.last_button in (self.xoperators or self.xyoperators)

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(self.choose_operation(text))
            self.solution.text = solution

    def choose_operation(self, text):
        match self.button_text:
            case "sen(x)":
                soltext = str(logica.sin_t(float(text)))
            case "cos(x)":
                soltext = str(logica.cos_t(float(text)))
            case "tan(x)":
                soltext = str(logica.tan_t(float(text)))
            case "senh(x)":
                soltext = str(logica.sinh_t(float(text)))
            case "cosh(x)":
                soltext = str(logica.cosh_t(float(text)))
            case "tanh(x)":
                soltext = str(logica.tanh_t(float(text)))
            case "asen(x)":
                soltext = str(logica.asin_t(float(text)))
            case "acos(x)":
                soltext = str(logica.asin_t(float(text)))  # FALTA !!!!!
            case "atan(x)":
                soltext = str(logica.atan_t(float(text)))
            case "sec(x)":
                soltext = str(logica.sec_t(float(text)))
            case "csc(x)":
                soltext = str(logica.csc_t(float(text)))
            case "cot(x)":
                soltext = str(logica.cot_t(float(text)))

            case "x*y":
                soltext = str(logica.cot_t(float(text)))
            case _:
                soltext = "-1"
        self.current = soltext
        self.last_button = self.current
        self.last_was_xoperator = False
        self.button_text = soltext
        self.solution.text = soltext


if __name__ == "__main__":
    app = MainApp()
    app.run()