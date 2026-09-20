import tkinter as tk
from tkinter import messagebox
import numpy as np

def borrar_valores():
    for i in range(4):
        for j in range(4):
            entradas_A[i][j].delete(0, tk.END)
        
        entradas_b[i].delete(0, tk.END)
        
        entradas_x[i].config(state=tk.NORMAL)
        entradas_x[i].delete(0, tk.END)
        entradas_x[i].config(state="readonly")
        
    entrada_det.config(state=tk.NORMAL)
    entrada_det.delete(0, tk.END)
    entrada_det.config(state="readonly")

def calcular_determinante():
    try:
        n = dimension_var.get()
        
        matriz_A = []
        for i in range(n):
            fila = []
            for j in range(n):
                valor_texto = entradas_A[i][j].get()
                valor_texto = valor_texto.replace(',', '.') 
                fila.append(float(valor_texto))
            matriz_A.append(fila)
            
        A = np.array(matriz_A)
        det = np.linalg.det(A)
        
        entrada_det.config(state=tk.NORMAL)
        entrada_det.delete(0, tk.END)
        if abs(det) < 1e-10: 
            det = 0.0
        entrada_det.insert(0, f"{det:.4f}")
        entrada_det.config(state="readonly")
        
    except ValueError:
        messagebox.showerror("Error de carga", f"Por favor, ingresá números válidos en todos los campos de la matriz {n}x{n}.")

root = tk.Tk()
root.title("Laboratorio de Matrices")
root.geometry("800x450")
root.configure(padx=20, pady=20)

frame_dimension = tk.LabelFrame(root, text="Dimensión", padx=10, pady=10)
frame_dimension.grid(row=0, column=0, sticky="n", padx=(0, 20))

dimension_var = tk.IntVar(value=3)

radio_2x2 = tk.Radiobutton(frame_dimension, text="2 x 2", variable=dimension_var, value=2)
radio_2x2.pack(anchor="w", pady=5)

radio_3x3 = tk.Radiobutton(frame_dimension, text="3 x 3", variable=dimension_var, value=3)
radio_3x3.pack(anchor="w", pady=5)

radio_4x4 = tk.Radiobutton(frame_dimension, text="4 x 4", variable=dimension_var, value=4)
radio_4x4.pack(anchor="w", pady=5)

frame_matrices = tk.Frame(root)
frame_matrices.grid(row=0, column=1, padx=20, sticky="n")

tk.Label(frame_matrices, text="A", font=("Arial", 10, "bold")).grid(row=0, column=1, columnspan=4)
tk.Label(frame_matrices, text="b", font=("Arial", 10, "bold")).grid(row=0, column=6, padx=10)
tk.Label(frame_matrices, text="x", font=("Arial", 10, "bold")).grid(row=0, column=7, padx=10)

for j in range(4):
    tk.Label(frame_matrices, text=str(j)).grid(row=1, column=j+1)

entradas_A = []
entradas_b = []
entradas_x = []

for i in range(4):
    tk.Label(frame_matrices, text=str(i)).grid(row=i+2, column=0, padx=5)
    
    fila_A = []
    for j in range(4):
        entrada = tk.Entry(frame_matrices, width=5, justify="center")
        entrada.grid(row=i+2, column=j+1, padx=2, pady=2)
        fila_A.append(entrada)
    entradas_A.append(fila_A)
    
    tk.Label(frame_matrices, text="  ").grid(row=i+2, column=5)
    
    entrada_b = tk.Entry(frame_matrices, width=5, justify="center")
    entrada_b.grid(row=i+2, column=6, padx=10, pady=2)
    entradas_b.append(entrada_b)
    
    entrada_x = tk.Entry(frame_matrices, width=5, justify="center", state="readonly")
    entrada_x.grid(row=i+2, column=7, padx=10, pady=2)
    entradas_x.append(entrada_x)

frame_inferior = tk.Frame(root)
frame_inferior.grid(row=1, column=0, columnspan=2, pady=10)

texto_ayuda = "El sistema de ecuaciones permite calcular A.x = b\nSe deben cargar los valores de A y b y luego,\nal calcular, se obtienen los valores de x"
label_ayuda = tk.Label(frame_inferior, text=texto_ayuda, justify="center")
label_ayuda.pack(pady=(0, 15))

frame_botones = tk.Frame(frame_inferior)
frame_botones.pack(pady=5)

btn_borrar = tk.Button(frame_botones, text="Borrar valores", command=borrar_valores)
btn_borrar.grid(row=0, column=0, padx=10)

btn_calcular = tk.Button(frame_botones, text="Calcular")
btn_calcular.grid(row=0, column=1, padx=10)

frame_det = tk.Frame(frame_inferior)
frame_det.pack(pady=15)

tk.Label(frame_det, text="Determinante:").grid(row=0, column=0, padx=5)

entrada_det = tk.Entry(frame_det, width=10, justify="center", state="readonly")
entrada_det.grid(row=0, column=1, padx=5)

btn_calc_det = tk.Button(frame_det, text="Calcular det.", command=calcular_determinante)
btn_calc_det.grid(row=0, column=2, padx=5)

root.mainloop()