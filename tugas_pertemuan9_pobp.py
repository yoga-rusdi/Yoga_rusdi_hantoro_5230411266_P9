import tkinter as tk
from tkinter import ttk

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Konversi Mata Uang")
        self.root.geometry("500x400")

        self.label_judul = ttk.Label(self.root, text="Konversi Mata Uang", font=("Arial", 16))
        self.label_judul.pack(pady=10)

        self.label_jumlah = ttk.Label(self.root, text="Jumlah:")
        self.label_jumlah.pack(pady=5)
        self.entry_jumlah = ttk.Entry(self.root, width=30)
        self.entry_jumlah.pack(pady=5)

        self.label_mata_uang_input = ttk.Label(self.root, text="Pilih Mata Uang untuk Jumlah:")
        self.label_mata_uang_input.pack(pady=5)
        self.combo_mata_uang_input = ttk.Combobox(self.root, values=["IDR"], state="readonly")
        self.combo_mata_uang_input.pack(pady=5)
        self.combo_mata_uang_input.current(0)

        self.label_mata_uang_output = ttk.Label(self.root, text="Pilih Mata Uang yang Akan Dikeluarkan:")
        self.label_mata_uang_output.pack(pady=5)
        self.combo_mata_uang_output = ttk.Combobox(self.root, values=["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SGD", "NZD"], state="readonly")
        self.combo_mata_uang_output.pack(pady=5)
        self.combo_mata_uang_output.current(0)

        self.tombol_konversi = ttk.Button(self.root, text="Konversi", command=self.konversi)
        self.tombol_konversi.pack(pady=10)

        self.label_hasil = ttk.Label(self.root, text="", font=("Arial", 12))
        self.label_hasil.pack(pady=10)

        self.tree = ttk.Treeview(self.root, columns=("Jumlah", "Mata Uang", "Hasil"), show='headings')
        self.tree.heading("Jumlah", text="Jumlah")
        self.tree.heading("Mata Uang", text="Mata Uang")
        self.tree.heading("Hasil", text="Hasil")
        self.tree.pack(pady=10, fill=tk.BOTH, expand=True)

    def konversi(self):
        jumlah = self.entry_jumlah.get()
        mata_uang_output = self.combo_mata_uang_output.get()

        # Validasi input
        if not jumlah.replace('.', '', 1).isdigit():  # Memungkinkan angka desimal
            self.label_hasil.config(text="Masukkan jumlah yang valid (hanya angka).")
            return

        jumlah = float(jumlah)

        if mata_uang_output == "USD":
            hasil = jumlah / 15000
        elif mata_uang_output == "EUR":
            hasil = jumlah / 16000
        elif mata_uang_output == "GBP":
            hasil = jumlah / 20000
        elif mata_uang_output == "JPY":
            hasil = jumlah / 100
        elif mata_uang_output == "AUD":
            hasil = jumlah / 11000
        elif mata_uang_output == "CAD":
            hasil = jumlah / 12000
        elif mata_uang_output == "CHF":
            hasil = jumlah / 14000
        elif mata_uang_output == "CNY":
            hasil = jumlah / 2300
        elif mata_uang_output == "SGD":
            hasil = jumlah / 11000
        elif mata_uang_output == "NZD":
            hasil = jumlah / 11000

        self.label_hasil.config(text=f"{jumlah} IDR = {hasil:.2f} {mata_uang_output}")

        existing_items = self.tree.get_children()
        already_exists = False
        for item in existing_items:
            if self.tree.item(item)['values'] == (jumlah, "IDR", f"{hasil:.2f} {mata_uang_output}"):
                already_exists = True
                break

        if not already_exists:
            self.tree.insert("", "end", values=(jumlah, "IDR", f"{hasil:.2f} {mata_uang_output}"))

def main():
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()

if __name__ == "__main__":
    main()