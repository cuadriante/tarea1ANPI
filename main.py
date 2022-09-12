from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
import funtras


class MainApp(App):
    def build(self):

        self.xoperators = ["senh(x)", "cosh(x)", "tanh(x)", "asen(x)", "acos(x)", "atan(x)",
                           "sec(x)", "csc(x)", "cot(x)", "sen(x)", "cos(x)", "tan(x)", "ln(x)", "log10(x)",
                           "1/x", "root(x)", "exp(x)", "x!"]
        self.xyoperators = ["logy(x)", "yroot(x)", "x*y", "x+y", "x-y", "x/y"]
        self.last_was_xoperator = None
        self.last_was_xyoperator = None
        self.last_button = ""
        self.xyop = False
        self.operator = ""
        self.x = ""

        main_layout = BoxLayout(orientation="vertical")

        help_button = Button(
            text="HELP",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
        )
        help_button.bind(on_press=self.on_help)

        main_layout.add_widget(help_button)

        self.solution = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=55,
            background_color={0.1, 0.1, 0.7, 0.3}
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["senh(x)", "cosh(x)", "tanh(x)"],
            ["asen(x)", "acos(x)", "atan(x)"],
            ["sec(x)", "csc(x)", "cot(x)"],
            ["sen(x)", "cos(x)", "tan(x)"],
            ["ln(x)", "log10(x)", "logy(x)"],
            ["1/x", "root(x)", "yroot(x)"],
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
                try:
                    int(label)
                    button = Button(
                        text=label,
                        size_hint=(.1, .8),
                        pos_hint={"center_x": .5, "center_y": .5},
                        background_normal='',
                        background_color={0.1, 0.5, 0.6, 1}
                    )
                except:
                    if label == "CLR":
                        button = Button(
                            text=label,
                            size_hint=(.1, .8),
                            pos_hint={"center_x": .5, "center_y": .5},
                            background_normal='',
                            background_color={0.1, 0.5, 0.6, 1}
                        )
                    elif label == ".":
                        button = Button(
                            text=label,
                            size_hint=(.1, .8),
                            pos_hint={"center_x": .5, "center_y": .5},
                            background_normal='',
                            background_color={0.1, 0.5, 0.6, 1}
                        )
                    else:
                        button = Button(
                            text=label,
                            size_hint=(.1, .8),
                            pos_hint={"center_x": .5, "center_y": .5},
                            background_normal='',
                            background_color={1, .3, .4, .85}
                        )

                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            background_normal='',
            background_color={0.1, 0.5, 0.6, 1}
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
            self.x = ""
        else:
            if self.current and (self.last_was_xoperator and self.button_text in (self.xoperators or self.xyoperators)):
                # Don't add two operators right after each other
                return
            elif (self.current == "" or self.last_button == "") and self.button_text in (
                    self.xoperators or self.xyoperators):
                # First character cannot be an operator
                return
            elif self.button_text in self.xyoperators:
                self.xyop = True
                self.operator = self.button_text
                self.x = self.solution.text
                self.solution.text = ""
            elif self.button_text in self.xoperators:

                try:
                    self.choose_operation(self.solution.text)
                except OverflowError as oe:
                    self.solution.text = "OVERFLOW"
                op = True
            else:
                new_text = self.current + self.button_text
                self.solution.text = new_text
        if not op:
            # if self.xyop and not (self.last_button in self.xoperators) or (self.last_button in self.xyoperators):
            #   self.x = self.last_button
            self.last_button = self.button_text
            self.last_was_xoperator = (self.last_button in self.xoperators) or (self.last_button in self.xyoperators)

        print("BUTTON TEXT " + self.button_text)
        print("SOLUTION TEXT " + self.solution.text)
        print("op " + str(op))
        print("xyop " + str(self.xyop))
        print("\n\n")

    def on_help(selfself, instance):
        popup = Popup(title="HELP", content=Label(text="Tecnológico de Costa Rica \n"
                                                       "Análisis Numerico para Ingenieria \n\n"
                                                       "Adriana Calderon Barboza\n"
                                                       "Anthony Chaves Achoy\n"
                                                       "David de la Hoz Aguirre\n\n\n"
                                                        "INSTRUCCIONES:\n"
                                                       "OPERACIONES DE UNA VARIABLE (X): Escriba\n"
                                                       "el numero a operar y seleccione el \n"
                                                       "operador, el resultado se desplegara \n"
                                                       "automaticamente \n\n"
                                                       "OPERACIONES DE DOS VARIABLES (X,Y): \n"
                                                       "Escriba el primer numero a operar \n"
                                                       "y seleccione el operador, escriba el \n"
                                                       "segundo numero a operar y seleccione \n"
                                                       "'=', el resultado se desplegará."),
                      size_hint = (None, None),
                      size = (700, 700))

        popup.open()

    def on_solution(self, instance):
        if self.xyop and (self.x != "") and (
                self.last_button not in self.xyoperators or self.last_button not in self.xoperators):
            print("x " + self.x)
            self.y = self.solution.text
            print("y " + self.y)
            self.choose_xyoperation(self.x, self.y)
            self.xyop = False
            self.operator = ""

        print("BUTTON TEXT " + self.button_text)
        print("SOLUTION TEXT " + self.solution.text)
        print("xyop " + str(self.xyop))
        print("\n\n")

        if self.xyop:
            self.x = self.last_button
        self.last_button = self.button_text
        self.last_was_xoperator = (self.last_button in self.xoperators) or (self.last_button in self.xyoperators)

    def choose_operation(self, text):
        soltext = "-1"
        # match self.button_text:
        if self.button_text == "sen(x)":
            soltext = str(funtras.sin_t(float(text)))

        elif self.button_text == "cos(x)":
            soltext = str(funtras.cos_t(float(text)))

        elif self.button_text == "tan(x)":
            soltext = str(funtras.tan_t(float(text)))
        elif self.button_text == "senh(x)":
            soltext = str(funtras.sinh_t(float(text)))
        elif self.button_text == "cosh(x)":
            soltext = str(funtras.cosh_t(float(text)))
        elif self.button_text == "tanh(x)":
            soltext = str(funtras.tanh_t(float(text)))
        elif self.button_text == "asen(x)":
            soltext = str(funtras.asin_t(float(text)))
        elif self.button_text == "acos(x)":
            soltext = str(funtras.asin_t(float(text)))  # FALTA !!!!!
        elif self.button_text == "atan(x)":
            soltext = str(funtras.atan_t(float(text)))
        elif self.button_text == "sec(x)":
            soltext = str(funtras.sec_t(float(text)))
        elif self.button_text == "csc(x)":
            soltext = str(funtras.csc_t(float(text)))
        elif self.button_text == "cot(x)":
            soltext = str(funtras.cot_t(float(text)))
        elif self.button_text == "ln(x)":
            soltext = str(funtras.ln_t(float(text)))
        elif self.button_text == "log10(x)":
            soltext = str(funtras.log_t(float(text), 10))
        elif self.button_text == "1/x":
            soltext = str(funtras.div_t(float(text)))
        elif self.button_text == "root(x)":
            soltext = str(funtras.root_t(float(text), 2))
        elif self.button_text == "exp(x)":
            soltext = str(funtras.exp_t(float(text)))
        elif self.button_text == "x!":
            try:
                x = int(text)
                soltext = str(funtras.fact(x))
            except ValueError as ve:
                soltext = "INVALID TYPE"
        # case _:
        #    soltext = "-1"

        if soltext == "inf":
            soltext = "MATH ERROR"
        self.current = soltext
        self.last_button = self.current
        self.last_was_xoperator = False
        self.button_text = soltext
        self.solution.text = soltext

    def choose_xyoperation(self, x, text):
        soltext = "-1"
        if self.operator == "logy(x)":
            soltext = str(funtras.log_t(float(text), float(x)))
        elif self.operator == "yroot(x)":
            soltext = str(funtras.root_t(float(text), float(x)))
        elif self.operator == "x*y":
            soltext = str(float(x) * float(text))
            # soltext = str(funtras.log_t(float(text), float(x)))
        elif self.operator == "x+y":
            soltext = str(float(x) + float(text))
            # soltext = str(funtras.log_t(float(text), float(x)))
        elif self.operator == "x-y":
            soltext = str(float(x) - float(text))
            # soltext = str(funtras.log_t(float(text), float(x)))
        elif self.operator == "x/y":
            soltext = str(float(x) / float(text))
            # soltext = str(funtras.log_t(float(text), float(x)))
        # case _:
        #    soltext = "uwu"
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
