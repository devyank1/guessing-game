import tkinter as tk
import random

# GENERATE AN ALEATORY NUMBER
aleatory_number = random.randint(1, 1000)

def verify_guess():
    try:
        guess = int(entry_guess.get())
        if guess < aleatory_number:
            label_result.config(text="⬆️ Tente um número maior! ⬆️", fg="blue")
        elif guess > aleatory_number:
            label_result.config(text="⬇️ Tente um número menor! ⬇️", fg="purple")
        else:
            label_result.config(text=f"🎉 Parabéns! Você acertou! 🎉\nO número era {aleatory_number}", fg="green")
            window.after(5000, reset_game)
    except ValueError:
        label_result.config(text="Por favor, insira um número válido.")

def reset_game():
    global aleatory_number
    aleatory_number = random.randint(1,1000)
    entry_guess.delete(0, tk.END)
    label_result.config(text="")

# CONFIGURATION OF MAIN WINDOW
window = tk.Tk()
window.title("Jogo de Adivinhação de Números")
window.geometry("300x200")
window.config(bg="#FFEBCC")

# Instructions
label_instruction = tk.Label(
    window,
    text="🎲 Adivinhe o número entre 1 e 1000 🎲",
    font=("Arial", 16, "bold"),
    bg="#FFEBCC",
    fg="#333"
)
label_instruction.pack(pady=20)

# Entry field for the guess
entry_guess = tk.Entry(window, font=("Arial", 14), width=10, justify="center")
entry_guess.pack(pady=10)

# Button to submit the guess
button_verify = tk.Button(
    window,
    text="Verificar",
    font=("Arial", 14, "bold"),
    bg="#FFDD57",  # Yellow button color
    fg="black",
    command=verify_guess
)
button_verify.pack(pady=10)

# Label to display the result
label_result = tk.Label(window, text="", font=("Arial", 14), bg="#FFEBCC")
label_result.pack(pady=20)

# Main loop of the application
window.mainloop()