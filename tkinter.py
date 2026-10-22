import tkinter as tk
root = tk.Tk()
root.mainloop()
root.title("Prediksi Prodi Pilihan")
root.geometry("520x420")
root.resizable(False, False)
root.configure(bg="#f0f4f8")
label_judul = tk.Label(root, text="Aplikasi Prediksi Prodi Pilihan",
                       font=("Arial", 16, "bold"), bg="#f0f4f8", fg="#1e3a8a")
label_judul.pack(pady=(20, 10))
MAPEL = ["Matematika", "Bahasa Indonesia", "Bahasa Inggris", "Fisika", "Kimia",
         "Biologi", "Ekonomi", "Sejarah", "Geografi", "Sosiologi"]
frame_input = tk.Frame(root, bg="#f0f4f8")
frame_input.pack(pady=10)
entries = []
for i, mapel in enumerate(MAPEL):
    kolom = (i // 5) * 2
    baris = i % 5
    tk.Label(frame_input, text=mapel, bg="#f0f4f8", font=("Arial", 10)).grid(
        row=baris, column=kolom, padx=(10, 5), pady=5, sticky="e")
    entry = tk.Entry(frame_input, width=10, justify="center")
    entry.grid(row=baris, column=kolom + 1, padx=(0, 15), pady=5)
    entries.append(entry)
    button = tk.Button(root, text="Hasil Prediksi", font=("Arial", 11, "bold"),
                   bg="#2563eb", fg="white", padx=20, pady=5)
button.pack(pady=15)
label_hasil = tk.Label(root, text="", font=("Arial", 14, "bold"),
                       bg="#f0f4f8", fg="#15803d")
label_hasil.pack(pady=10)
def hasil_prediksi():
    label_hasil.config(text="Prodi Prediksi: Teknologi Informasi")
    button = tk.Button(root, text="Hasil Prediksi", command=hasil_prediksi,
                   font=("Arial", 11, "bold"), bg="#2563eb", fg="white",
                   padx=20, pady=5)
                lebar, tinggi = 520, 420
x = (root.winfo_screenwidth() - lebar) // 2
y = (root.winfo_screenheight() - tinggi) // 2
root.geometry(f"{lebar}x{tinggi}+{x}+{y}")
entries[0].focus()