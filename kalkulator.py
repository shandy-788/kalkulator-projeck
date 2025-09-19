import tkinter as tk
from tkinter import font

class Kalkulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Lengkap")
        self.root.geometry("350x500")
        self.root.resizable(False, False)

        # Variabel untuk menyimpan input dan hasil
        self.current_input = ""
        self.result_var = tk.StringVar(value="0")

        # Font untuk tampilan
        self.display_font = font.Font(size=20, weight="bold")
        self.button_font = font.Font(size=12)

        self._setup_ui()

    def _setup_ui(self):
        """Membuat tampilan GUI kalkulator"""

        # Frame untuk display hasil
        display_frame = tk.Frame(self.root, bg="#2c3e50", height=100)
        display_frame.pack(fill="x", padx=10, pady=10)

        result_label = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=self.display_font,
            bg="#00BCC2",
            fg="white",
            anchor="e",
            padx=20
        )
        result_label.pack(expand=True, fill="both")

        # Frame untuk tombol-tombol
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Definisi tombol-tombol kalkulator
        buttons = [
            ['CA', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '±', '=']
        ]

        # Membuat tombol dan menempatkan di grid
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                btn = tk.Button(
                    button_frame,
                    text=btn_text,
                    font=self.button_font,
                    height=2,
                    command=lambda x=btn_text: self._on_button_click(x)
                )
                # Warna tombol sesuai fungsi
                if btn_text == '=':
                    btn.config(bg="#00BCC2", fg="white")
                elif btn_text in ['C', '⌫', '%', '/', '*', '-', '+']:
                    btn.config(bg="#FDC741", fg="white")
                else:
                    btn.config(bg="#ecf0f1")

                btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)

        # Konfigurasi grid agar tombol responsif
        for i in range(len(buttons)):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(len(buttons[0])):
            button_frame.grid_columnconfigure(j, weight=1)

    def _on_button_click(self, char):
        """Menangani klik tombol"""

        if char == 'C':
            self._clear()
        elif char == '⌫':
            self._backspace()
        elif char == '±':
            self._toggle_sign()
        elif char == '%':
            self._percentage()
        elif char == '=':
            self._calculate()
        else:
            self._append_char(char)

    def _clear(self):
        self.current_input = ""
        self.result_var.set("0")

    def _backspace(self):
        self.current_input = self.current_input[:-1]
        self.result_var.set(self.current_input if self.current_input else "0")

    def _toggle_sign(self):
        if self.current_input.startswith('-'):
            self.current_input = self.current_input[1:]
        else:
            self.current_input = '-' + self.current_input if self.current_input else "-"
        self.result_var.set(self.current_input)

    def _percentage(self):
        try:
            value = eval(self.current_input)
            value /= 100
            self.current_input = str(value)
            self.result_var.set(self.current_input)
        except Exception:
            self._error()

    def _calculate(self):
        try:
            # Evaluasi ekspresi matematika
            result = eval(self.current_input)
            self.current_input = str(result)
            self.result_var.set(self.current_input)
        except Exception:
            self._error()

    def _append_char(self, char):
        if self.result_var.get() == "Error":
            self.current_input = ""
            self.result_var.set("0")

        # Hindari dua operator berturut-turut
        if char in '+-*/':
            if not self.current_input:
                # Tidak boleh mulai dengan operator kecuali minus
                if char != '-':
                    return
            elif self.current_input[-1] in '+-*/':
                # Ganti operator terakhir dengan yang baru
                self.current_input = self.current_input[:-1]

        self.current_input += char
        self.result_var.set(self.current_input)

    def _error(self):
        self.result_var.set("Error")
        self.current_input = ""

def main():
    root = tk.Tk()
    Kalkulator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
