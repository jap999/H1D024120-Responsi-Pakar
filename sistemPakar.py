import tkinter as tk
from tkinter import messagebox

# Knowledge Base
kb_lab = {
    "Asam Kuat": "Bilas dengan air mengalir selama 15 menit, jangan dinetralkan dengan basa kuat.",
    "Basa Kuat": "Cuci dengan air mengalir, lalu bilas dengan larutan asam borat 1%.",
    "Logam Natrium": "Jangan gunakan air! Gunakan pemadam api kelas D atau pasir kering.",
    "Gas Beracun": "Segera pindahkan korban ke area terbuka berudara segar dan hubungi medis."
}

def diagnosa():
    zat = entry_zat.get()
    solusi = kb_lab.get(zat, "Zat tidak dikenal. Segera hubungi tim medis darurat!")
    messagebox.showinfo("Prosedur Darurat", f"Tindakan: {solusi}")

root = tk.Tk()
root.title("Safe-Treat Expert System")
root.geometry("350x200")

tk.Label(root, text="Masukkan Jenis Zat Pencemar:", font=("Arial", 10, "bold")).pack(pady=10)
entry_zat = tk.Entry(root, width=30)
entry_zat.pack()
tk.Label(root, text="(Contoh: Asam Kuat, Basa Kuat, Logam Natrium)").pack()

tk.Button(root, text="Dapatkan Solusi", command=diagnosa, bg="red", fg="white").pack(pady=20)
root.mainloop()
