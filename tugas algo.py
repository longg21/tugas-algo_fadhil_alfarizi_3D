import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung Permeabilitas
def hitung_permeabilitas():
    try:
        # Ambil nilai input
        Q = float(entry_q.get())  # Debit (m³/s)
        mu = float(entry_mu.get())  # Viskositas (Pa.s)
        L = float(entry_l.get())  # Panjang (m)
        A = float(entry_a.get())  # Luas (m²)
        dp = float(entry_dp.get())  # Perbedaan Tekanan (Pa)

        # Perhitungan Permeabilitas
        K = (Q * mu * L) / (A * dp)
        label_result_permeabilitas.config(text=f"Permeabilitas: {K:.4e} m²")
    except ValueError:
        messagebox.showerror("Input Error", "Mohon masukkan nilai yang valid.")

# Fungsi untuk menghitung Porositas
def hitung_porositas():
    try:
        # Ambil nilai input
        V_void = float(entry_v_void.get())  # Volume Void (m³)
        V_total = float(entry_v_total.get())  # Volume Total (m³)

        # Perhitungan Porositas
        porositas = (V_void / V_total) * 100
        label_result_porositas.config(text=f"Porositas: {porositas:.2f} %")
    except ValueError:
        messagebox.showerror("Input Error", "Mohon masukkan nilai yang valid.")

# Inisialisasi Window
root = tk.Tk()
root.title("Aplikasi Permeabilitas dan Porositas By ALpezz")

# Frame untuk Permeabilitas
frame_permeabilitas = tk.Frame(root)
frame_permeabilitas.pack(pady=10)

label_permeabilitas = tk.Label(frame_permeabilitas, text="Perhitungan Permeabilitas", font=("Arial", 14))
label_permeabilitas.grid(row=0, column=0, columnspan=2)

tk.Label(frame_permeabilitas, text="Debit Q (m³/s)").grid(row=1, column=0)
entry_q = tk.Entry(frame_permeabilitas)
entry_q.grid(row=1, column=1)

tk.Label(frame_permeabilitas, text="Viskositas µ (Pa.s)").grid(row=2, column=0)
entry_mu = tk.Entry(frame_permeabilitas)
entry_mu.grid(row=2, column=1)

tk.Label(frame_permeabilitas, text="Panjang L (m)").grid(row=3, column=0)
entry_l = tk.Entry(frame_permeabilitas)
entry_l.grid(row=3, column=1)

tk.Label(frame_permeabilitas, text="Luas A (m²)").grid(row=4, column=0)
entry_a = tk.Entry(frame_permeabilitas)
entry_a.grid(row=4, column=1)

tk.Label(frame_permeabilitas, text="Perbedaan Tekanan ∆P (Pa)").grid(row=5, column=0)
entry_dp = tk.Entry(frame_permeabilitas)
entry_dp.grid(row=5, column=1)

button_hitung_permeabilitas = tk.Button(frame_permeabilitas, text="Hitung Permeabilitas", command=hitung_permeabilitas)
button_hitung_permeabilitas.grid(row=6, column=0, columnspan=2, pady=10)

label_result_permeabilitas = tk.Label(frame_permeabilitas, text="Permeabilitas: -", font=("Arial", 12))
label_result_permeabilitas.grid(row=7, column=0, columnspan=2)

# Frame untuk Porositas
frame_porositas = tk.Frame(root)
frame_porositas.pack(pady=10)

label_porositas = tk.Label(frame_porositas, text="Perhitungan Porositas", font=("Arial", 14))
label_porositas.grid(row=0, column=0, columnspan=2)

tk.Label(frame_porositas, text="Volume Void V_void (m³)").grid(row=1, column=0)
entry_v_void = tk.Entry(frame_porositas)
entry_v_void.grid(row=1, column=1)

tk.Label(frame_porositas, text="Volume Total V_total (m³)").grid(row=2, column=0)
entry_v_total = tk.Entry(frame_porositas)
entry_v_total.grid(row=2, column=1)

button_hitung_porositas = tk.Button(frame_porositas, text="Hitung Porositas", command=hitung_porositas)
button_hitung_porositas.grid(row=3, column=0, columnspan=2, pady=10)

label_result_porositas = tk.Label(frame_porositas, text="Porositas: -", font=("Arial", 12))
label_result_porositas.grid(row=4, column=0, columnspan=2)

# Jalankan aplikasi
root.mainloop()
