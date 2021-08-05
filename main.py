import tkinter as tk
from tkinter import ttk


class Calculator:

    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Calculator")

        self.first_operand = ""
        self.second_operand = ""
        self.operator = ""
        self.first_equals_result = False
        self.char_deletion = False

        self.display = tk.StringVar()
        self.display.set("0")

        self.result = ttk.Entry(
                                self.main_window, justify=tk.RIGHT,
                                textvariable=self.display, state="readonly"
                                )
        self.result.grid(
                        column=0, row=0, columnspan=4,
                        sticky=tk.NSEW, padx=2, pady=2
                        )

        self.clear_button = ttk.Button(
                                        self.main_window, text="C",
                                        command=self.clear
                                        )
        self.clear_button.grid(
                                column=0, row=1, padx=2, pady=2
                                )

        self.multiplication = ttk.Button(
                                        self.main_window, text="*",
                                        command=lambda: self.handle_input("*")
                                        )
        self.multiplication.grid(
                                column=1, row=1, padx=2, pady=2
                                )

        self.division = ttk.Button(
                                    self.main_window, text="/",
                                    command=lambda: self.handle_input("/")
                                    )
        self.division.grid(
                            column=2, row=1, padx=2, pady=2
                            )

        self.percentage = ttk.Button(
                                    self.main_window, text="%",
                                    command=lambda: self.handle_input("%")
                                    )
        self.percentage.grid(
                            column=3, row=1, padx=2, pady=2
                            )

        self.seven = ttk.Button(
                                self.main_window, text="7",
                                command=lambda: self.handle_input("7")
                                )
        self.seven.grid(
                        column=0, row=2, padx=2, pady=2
                        )

        self.eight = ttk.Button(
                                self.main_window, text="8",
                                command=lambda: self.handle_input("8")
                                )
        self.eight.grid(
                        column=1, row=2, padx=2, pady=2
                        )

        self.nine = ttk.Button(
                                self.main_window, text="9",
                                command=lambda: self.handle_input("9")
                                )
        self.nine.grid(
                        column=2, row=2, padx=2, pady=2
                        )

        self.addition = ttk.Button(
                                    self.main_window, text="+",
                                    command=lambda: self.handle_input("+")
                                    )
        self.addition.grid(
                            column=3, row=2, padx=2, pady=2
                            )

        self.four = ttk.Button(
                                self.main_window, text="4",
                                command=lambda: self.handle_input("4")
                                )
        self.four.grid(
                        column=0, row=3, padx=2, pady=2
                        )

        self.five = ttk.Button(
                                self.main_window, text="5",
                                command=lambda: self.handle_input("5")
                                )
        self.five.grid(
                        column=1, row=3, padx=2, pady=2
                        )

        self.six = ttk.Button(
                            self.main_window, text="6",
                            command=lambda: self.handle_input("6")
                            )
        self.six.grid(
                    column=2, row=3, padx=2, pady=2
                    )

        self.substraction = ttk.Button(
                                        self.main_window, text="-",
                                        command=lambda: self.handle_input("-")
                                        )
        self.substraction.grid(
                                column=3, row=3, padx=2, pady=2
                                )

        self.one = ttk.Button(
                            self.main_window, text="1",
                            command=lambda: self.handle_input("1")
                            )
        self.one.grid(
                    column=0, row=4, padx=2, pady=2
                    )

        self.two = ttk.Button(
                            self.main_window, text="2",
                            command=lambda: self.handle_input("2")
                            )
        self.two.grid(
                    column=1, row=4, padx=2, pady=2
                    )

        self.three = ttk.Button(
                                self.main_window, text="3",
                                command=lambda: self.handle_input("3")
                                )
        self.three.grid(
                        column=2, row=4, padx=2, pady=2
                        )

        self.plus_minus = ttk.Button(
                                    self.main_window, text="+/-",
                                    command=lambda: self.handle_input("opp")
                                    )
        self.plus_minus.grid(
                            column=0, row=5, padx=2, pady=2
                            )

        self.zero = ttk.Button(
                            self.main_window, text="0",
                            command=lambda: self.handle_input("0")
                            )
        self.zero.grid(
                        column=1, row=5, padx=2, pady=2
                        )

        self.decimal = ttk.Button(
                                self.main_window, text=".",
                                command=lambda: self.handle_input(".")
                                )
        self.decimal.grid(
                        column=2, row=5, padx=2, pady=2
                        )

        self.evaluate_button = ttk.Button(
                                        self.main_window, text="=",
                                        command=self.evaluate
                                        )
        self.evaluate_button.grid(
                                column=3, row=4, rowspan=2,
                                sticky=tk.NSEW, padx=2, pady=2
                                )

        self.main_window.bind("<Key>", self.key_stroke)
        self.main_window.mainloop()

    def handle_input(self, num):
        if not self.first_operand and num.isnumeric():
            print(f"First operand entered: {num}")
            self.first_operand = num
        elif self.first_equals_result and num.isnumeric():
            print(f"Replacing last result with new first operand: {num}")
            self.first_operand = num
        elif self.first_operand and num.isnumeric() and not self.operator:
            if len(self.first_operand) == 16:
                print("First operand reached maximum length (16).")
                return
            else:
                if self.char_deletion:
                    print(f"Replacing 0 with new first operand: {num}")
                    self.first_operand = num
                    self.char_deletion = False
                else:
                    print(f"First operand updated with: {num}")
                    self.first_operand += num
        elif num in ["*", "/", "+", "-"]:
            if self.first_operand[-1] == ".":
                self.first_operand = self.first_operand[:-1]
            if not self.first_operand:
                print("Enter first operand before choosing an operator!")
            elif not self.second_operand:
                print(f"Operator entered: {num}")
                self.operator = num
            else:
                total = str(
                        eval(
                            f"{self.first_operand}{self.operator}{self.second_operand}"
                            )
                        )
                if total[-2:] == ".0":
                    total = total[:-2]
                self.first_operand = total
                self.second_operand = ""
                self.operator = num
        elif num == ".":
            if self.second_operand and "." not in self.second_operand:
                print("Decimal entered for second operand.")
                self.second_operand += "."
            elif self.first_equals_result:
                print("Replacing last result with 0.")
                self.first_operand = "0."
            elif "." not in self.first_operand and not self.operator:
                print("Decimal entered for first operand.")
                if self.first_operand:
                    self.first_operand += "."
                else:
                    self.first_operand = "0."
        elif num == "%" and self.second_operand:
            print("Calculating percentile")
            self.second_operand = str(
                round(
                    float(self.first_operand) * (float(self.second_operand) / 100), 2
                    )
                )
            if self.second_operand[-1] == "0":
                self.second_operand = self.second_operand[:-2]
        elif num == "opp":
            if self.second_operand:
                print("Changing second operand to its opposite value.")
                self.second_operand = str(int(self.second_operand) * -1)
            elif self.first_operand and not self.operator:
                print("Changing first operand to its opposite value.")
                self.first_operand = str(int(self.first_operand) * - 1)
        elif self.operator and num.isnumeric():
            if not self.second_operand and num.isnumeric():
                print(f"Second operand entered: {num}")
                self.second_operand += num
            elif self.second_operand and num.isnumeric():
                if len(self.second_operand) == 16:
                    print("Second operand reached maximum length (16).")
                    return
                else:
                    if self.char_deletion:
                        print(f"Replacing 0 with new second operand: {num}")
                        self.second_operand = num
                        self.char_deletion = False
                    else:
                        print(f"Second operand updated with: {num}")
                        self.second_operand += num
        elif num == "BackSpace":
            if self.operator:
                print("Deleting the last character of the second operand")
                self.second_operand = self.second_operand[:-1]
                if len(self.second_operand) == 0:
                    print("Setting second operand to 0")
                    self.second_operand = "0"
                    self.char_deletion = True
            elif not self.operator:
                if self.first_equals_result:
                    print(
                        "First operand equals result of the previous equation"
                        ", deletion of the last character prohibited"
                    )
                    return
                else:
                    print("Deleting the last character of the first operand")
                    self.first_operand = self.first_operand[:-1]
                    if len(self.first_operand) == 0:
                        print("Setting first operand to 0")
                        self.first_operand = "0"
                        self.char_deletion = True
        elif num == "Delete":
            if self.second_operand:
                self.second_operand = "0"
                self.char_deletion = True
            elif self.first_operand and not self.operator:
                self.first_operand = "0"
                self.char_deletion = True
                if self.first_equals_result:
                    self.first_equals_result = False
        else:
            print("Invalid command")

        self.first_equals_result = False

        if self.first_operand:
            self.set_display()

    def evaluate(self):
        try:
            print(
                "Evaluating result",
                "-" * 20,
                "Commencing new equation",
                sep="\n"
                )
            total = round(
                        eval(
                            f'{self.first_operand}{self.operator}{self.second_operand}'
                            ),
                        6)
            if total >= pow(10, 16):
                total = f"{total:e}"
                print(f"Type of total is {type(total)}")
            else:
                total = f"{total:,}"
                if total[-2:] == ".0":
                    total = total[:-2]
            self.display.set(total)
            self.first_operand = total
            self.second_operand = ""
            self.operator = ""
            self.first_equals_result = True
        except ZeroDivisionError as e:
            print(e)
            self.display.set("You cannot divide by zero!")
            self.first_operand = ""
            self.second_operand = ""
            self.operator = ""
        except SyntaxError as e:
            print(
                f"Caught error: {e}.",
                "Assuming second operand to be equal to the first operand"
                )
            self.second_operand = self.first_operand
            self.evaluate()
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.display.set("Error!")
            self.first_operand = ""
            self.second_operand = ""
            self.operator = ""

    def set_display(self):
        first_operand = ""
        second_operand = ""

        if self.first_operand[-1] == ".":
            first_operand = f"{int(self.first_operand[:-1]):,}."
        elif "." in self.first_operand:
            first_operand = f"{float(self.first_operand):,}"
            dot_unformatted = self.first_operand.index(".")
            dot_formatted = first_operand.index(".")
            first_operand = first_operand[:dot_formatted] +\
                self.first_operand[dot_unformatted:]
        else:
            first_operand = f"{int(self.first_operand):,}"

        if self.second_operand:
            if self.second_operand[-1] == ".":
                second_operand = f"{int(self.second_operand[:-1]):,}."
            elif "." in self.second_operand:
                second_operand = f"{float(self.second_operand):,}"
                dot_unformatted = self.second_operand.index(".")
                dot_formatted = second_operand.index(".")
                second_operand = second_operand[:dot_formatted] +\
                    self.second_operand[dot_unformatted:]
            else:
                second_operand = f"{int(self.second_operand):,}"

        self.display.set(f"{first_operand}{self.operator}{second_operand}")

    def clear(self):
        print("CLEARED!\n")
        self.first_operand = ""
        self.second_operand = ""
        self.operator = ""
        self.display.set("0")

    def key_stroke(self, event):
        print(
            f"\nKey pressed: {event.char}",
            "Key sym: {event.keysym}",
            "Key code: {event.keycode}",
            sep="\n"
            )
        if event.keysym == "Return":
            self.evaluate()
        elif event.keysym == "BackSpace":
            self.handle_input("BackSpace")
        elif event.keysym == "comma":
            self.handle_input(".")
        elif event.keysym == "Delete":
            self.handle_input("Delete")
        else:
            self.handle_input(event.char)


if __name__ == "__main__":
    app = Calculator()
