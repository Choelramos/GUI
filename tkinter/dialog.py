import tkinter as tk
from tkinter import messagebox as mb


def resposta():
    mb.showerror("Resposta", "Desculpe, resposta indisponível")


def verificacao():
    if mb.askyesno('Verificar', 'Realmente quer sair?'):
        mb.showwarning("Sim", "Ainda não foi implementado")
    else:
        mb.showinfo("Não", "A opção de Sair foi cancelada")


tk.Button(text="Sair", command=verificacao).pack(fill=tk.X)
tk.Button(text="Resposta", command=resposta).pack(fill=tk.X)
tk.mainloop()