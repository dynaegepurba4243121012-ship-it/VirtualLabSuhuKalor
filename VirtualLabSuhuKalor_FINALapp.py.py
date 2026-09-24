import tkinter as tk
from tkinter import ttk, messagebox

# ==========================
# WARNA
# ==========================
BG = "#071426"
CARD = "#0d2745"
ACCENT = "#1da1f2"
TEXT = "white"

root = tk.Tk()
root.title("Virtual Lab Suhu & Kalor")
root.geometry("1100x650")
root.configure(bg=BG)

# ==========================
# SIDEBAR
# ==========================
sidebar = tk.Frame(root, bg="#06111f", width=220)
sidebar.pack(side="left", fill="y")

title = tk.Label(
    sidebar,
    text="🧪\nVIRTUAL LAB\nSUHU & KALOR",
    fg="white",
    bg="#06111f",
    font=("Segoe UI", 18, "bold"),
)
title.pack(pady=25)

# ==========================
# AREA UTAMA
# ==========================
main = tk.Frame(root, bg=BG)
main.pack(fill="both", expand=True)


def clear():
    for widget in main.winfo_children():
        widget.destroy()


# ==========================
# BERANDA
# ==========================
def beranda():
    clear()

    tk.Label(
        main,
        text="Virtual Lab Suhu & Kalor",
        bg=BG,
        fg="white",
        font=("Segoe UI", 26, "bold"),
    ).pack(pady=20)

    tk.Label(
        main,
        text="Media pembelajaran fisika interaktif berbasis Python.",
        bg=BG,
        fg="#9fc5e8",
        font=("Segoe UI", 12),
    ).pack()

    frame = tk.Frame(main, bg=BG)
    frame.pack(pady=35)

    data = [
        ("🌡️", "Termometer", "#1976d2"),
        ("🔥", "Kalor", "#ef6c00"),
        ("⚖️", "Asas Black", "#7e57c2"),
        ("💧", "Perubahan Wujud", "#00897b"),
    ]

    for i, (icon, nama, warna) in enumerate(data):
        card = tk.Frame(frame, bg=warna, width=180, height=180)
        card.grid(row=0, column=i, padx=15)
        card.pack_propagate(False)

        tk.Label(card, text=icon, bg=warna, fg="white",
                 font=("Segoe UI Emoji", 40)).pack(pady=12)
        tk.Label(card, text=nama, bg=warna, fg="white",
                 font=("Segoe UI", 13, "bold")).pack()


# ==========================
# TERMOMETER
# ==========================
def termometer():
    clear()

    tk.Label(main, text="🌡️ Termometer Interaktif",
             bg=BG, fg="white",
             font=("Segoe UI", 22, "bold")).pack(pady=15)

    suhu = tk.IntVar(value=25)

    nilai = tk.Label(main, text="25 °C", bg=BG, fg="#5de6ff",
                     font=("Segoe UI", 30, "bold"))
    nilai.pack()

    canvas = tk.Canvas(main, width=120, height=320,
                       bg=BG, highlightthickness=0)
    canvas.pack(pady=15)

    canvas.create_oval(35, 250, 85, 300,
                       fill="red", outline="white", width=3)
    canvas.create_rectangle(52, 40, 68, 250,
                            outline="white", width=3)

    mercury = canvas.create_rectangle(
        54, 230, 66, 250, fill="red", outline="red")

    def update(v):
        t = int(float(v))
        nilai.config(text=f"{t} °C")
        tinggi = 230 - (t + 20) / 140 * 170
        canvas.coords(mercury, 54, tinggi, 66, 250)

    tk.Scale(
        main,
        from_=-20,
        to=120,
        orient="horizontal",
        variable=suhu,
        command=update,
        length=400,
        bg=BG,
        fg="white",
        troughcolor="#1f3d5b",
        highlightthickness=0,
    ).pack()

    update(25)


# ==========================
# KALOR
# ==========================
def kalor():
    clear()

    tk.Label(main, text="🔥 Percobaan Kalor",
             bg=BG, fg="white",
             font=("Segoe UI", 22, "bold")).pack(pady=15)

    form = tk.Frame(main, bg=CARD, padx=20, pady=20)
    form.pack()

    labels = ["Massa (kg)", "Kalor Jenis (J/kg°C)",
              "Suhu Awal (°C)", "Suhu Akhir (°C)"]
    defaults = [1, 4200, 25, 75]
    entries = []

    for i, (lab, val) in enumerate(zip(labels, defaults)):
        tk.Label(form, text=lab, bg=CARD,
                 fg="white").grid(row=i, column=0, sticky="w", pady=5)
        e = ttk.Entry(form)
        e.insert(0, str(val))
        e.grid(row=i, column=1, pady=5)
        entries.append(e)

    hasil = tk.Label(main, bg=BG, fg="#5de6ff",
                     font=("Segoe UI", 24, "bold"))
    hasil.pack(pady=20)

    def hitung():
        try:
            m = float(entries[0].get())
            c = float(entries[1].get())
            t1 = float(entries[2].get())
            t2 = float(entries[3].get())

            q = m * c * (t2 - t1)

            hasil.config(text=f"Q = {abs(q):,.0f} Joule")

            if q > 0:
                messagebox.showinfo("Hasil", "Kalor diserap benda.")
            else:
                messagebox.showinfo("Hasil", "Kalor dilepaskan benda.")

        except:
            messagebox.showerror("Error", "Masukkan angka yang benar.")

    ttk.Button(main, text="Hitung Kalor",
               command=hitung).pack()


# ==========================
# ASAS BLACK
# ==========================
def asas_black():
    clear()

    tk.Label(main, text="⚖️ Percobaan Asas Black",
             bg=BG, fg="white",
             font=("Segoe UI", 22, "bold")).pack(pady=15)

    frame = tk.Frame(main, bg=CARD, padx=20, pady=20)
    frame.pack()

    labels = [
        "Massa Panas", "Kalor Jenis Panas", "Suhu Panas",
        "Massa Dingin", "Kalor Jenis Dingin", "Suhu Dingin"
    ]

    defaults = [0.5, 4200, 80, 0.5, 4200, 20]
    ent = []

    for i, (lab, val) in enumerate(zip(labels, defaults)):
        tk.Label(frame, text=lab, bg=CARD,
                 fg="white").grid(row=i, column=0, sticky="w", pady=5)
        e = ttk.Entry(frame)
        e.insert(0, str(val))
        e.grid(row=i, column=1)
        ent.append(e)

    hasil = tk.Label(main, bg=BG, fg="#5de6ff",
                     font=("Segoe UI", 24, "bold"))
    hasil.pack(pady=20)

    def hitung():
        try:
            m1 = float(ent[0].get())
            c1 = float(ent[1].get())
            t1 = float(ent[2].get())

            m2 = float(ent[3].get())
            c2 = float(ent[4].get())
            t2 = float(ent[5].get())

            tm = (m1*c1*t1 + m2*c2*t2)/(m1*c1+m2*c2)

            hasil.config(text=f"Suhu Akhir = {tm:.2f} °C")

        except:
            messagebox.showerror("Error", "Masukkan angka yang benar.")

    ttk.Button(main, text="Campurkan",
               command=hitung).pack()


# ==========================
# PERUBAHAN WUJUD
# ==========================
def perubahan():
    clear()

    tk.Label(main, text="💧 Perubahan Wujud",
             bg=BG, fg="white",
             font=("Segoe UI", 22, "bold")).pack(pady=15)

    ikon = tk.Label(main, text="💧", bg=BG,
                    fg="white", font=("Segoe UI Emoji", 80))
    ikon.pack()

    fase = tk.Label(main, text="CAIR", bg=BG,
                    fg="#5de6ff",
                    font=("Segoe UI", 24, "bold"))
    fase.pack()

    def ubah(v):
        t = int(float(v))

        if t < 0:
            ikon.config(text="🧊")
            fase.config(text="PADAT")

        elif t == 0:
            ikon.config(text="🧊💧")
            fase.config(text="TITIK LEBUR")

        elif t < 100:
            ikon.config(text="💧")
            fase.config(text="CAIR")

        elif t == 100:
            ikon.config(text="💧💨")
            fase.config(text="TITIK DIDIH")

        else:
            ikon.config(text="💨")
            fase.config(text="GAS")

    tk.Scale(main, from_=-20, to=120,
             orient="horizontal",
             command=ubah,
             length=450,
             bg=BG,
             fg="white",
             troughcolor="#1f3d5b",
             highlightthickness=0).pack()

    ubah(25)


# ==========================
# TOMBOL MENU
# ==========================
menu = [
    ("🏠 Beranda", beranda),
    ("🌡️ Termometer", termometer),
    ("🔥 Kalor", kalor),
    ("⚖️ Asas Black", asas_black),
    ("💧 Perubahan Wujud", perubahan),
]

for nama, fungsi in menu:
    tk.Button(
        sidebar,
        text=nama,
        command=fungsi,
        bg="#102640",
        fg="white",
        activebackground=ACCENT,
        relief="flat",
        font=("Segoe UI", 11),
        padx=10,
        pady=8,
    ).pack(fill="x", padx=12, pady=5)

beranda()
root.mainloop()