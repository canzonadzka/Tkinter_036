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