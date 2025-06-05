import keyboard
import pyperclip
import pyautogui
import time
import json
import os
import tkinter as tk

# Nombre del archivo donde se guardan los contenidos
ARCHIVO_CONTENIDOS = 'contenidos.json'

# Cargar contenidos guardados
def cargar_contenidos():
    if os.path.exists(ARCHIVO_CONTENIDOS):
        with open(ARCHIVO_CONTENIDOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    else:
        return {}

# Guardar contenidos en archivo
def guardar_contenidos(contenidos):
    with open(ARCHIVO_CONTENIDOS, 'w', encoding='utf-8') as f:
        json.dump(contenidos, f, indent=4, ensure_ascii=False)

# Función para pegar contenido
def pegar_contenido(numero):
    if numero in contenidos:
        pyperclip.copy(contenidos[numero])
        time.sleep(0.05)
        pyautogui.hotkey('ctrl', 'v')
    else:
        print(f"[!] No hay contenido guardado en la casilla {numero}")

# Función para guardar nuevo contenido
def guardar_nuevo_contenido(numero):
    texto_actual = pyperclip.paste()
    contenidos[numero] = texto_actual
    guardar_contenidos(contenidos)
    print(f"[+] Guardado en casilla {numero}: {texto_actual[:30]}...")

# Función para formatear (limpiar) todo el contenido
def formatear_contenidos():
    contenidos.clear()
    guardar_contenidos(contenidos)
    actualizar_interfaz()
    print("[+] Todos los contenidos han sido eliminados.")

# Función para actualizar la interfaz gráfica
def actualizar_interfaz():
    for widget in contenido_frame.winfo_children():
        widget.destroy()  # Eliminar los widgets anteriores

    for idx, (key, value) in enumerate(contenidos.items()):
        label = tk.Label(contenido_frame, text=f"Casilla {key}: {value[:30]}...")  # Mostrar solo los primeros 30 caracteres
        label.grid(row=idx, column=0, sticky="w", padx=10, pady=5)

    for key in contenidos:
        button = tk.Button(contenido_frame, text=f"Pegar {key}", command=lambda k=key: pegar_contenido(k))
        button.grid(row=int(key), column=1, padx=10, pady=5)

# Crear la ventana de la interfaz
window = tk.Tk()
window.title("Portapapeles Múltiple")

# Frame para los contenidos
contenido_frame = tk.Frame(window)
contenido_frame.pack(padx=10, pady=10)

# Botón para limpiar todos los contenidos
formatear_button = tk.Button(window, text="Formatear Contenidos", command=formatear_contenidos)
formatear_button.pack(pady=5)

# Estado de los comandos
comandos_activos = False

# Botón para activar/desactivar comandos
def alternar_comandos():
    global comandos_activos
    comandos_activos = not comandos_activos
    if comandos_activos:
        activar_comandos()
        toggle_button.config(text="Desactivar Comandos")
        print("[+] Comandos ACTIVADOS")
    else:
        desactivar_comandos()
        toggle_button.config(text="Activar Comandos")
        print("[-] Comandos DESACTIVADOS")

# Activar comandos
def activar_comandos():
    numeros_validos = ['1','2','3','4','5','6','7','8','9','0']
    for numero in numeros_validos:
        keyboard.add_hotkey(f'ctrl+c+{numero}', lambda n=numero: (guardar_nuevo_contenido(n), actualizar_interfaz()))
        keyboard.add_hotkey(f'ctrl+{numero}', lambda n=numero: pegar_contenido(n))
    keyboard.add_hotkey('ctrl+j', lambda: (formatear_contenidos(), actualizar_interfaz()))

# Desactivar comandos
def desactivar_comandos():
    keyboard.clear_all_hotkeys()
    # Volver a registrar el atajo para alternar (después del clear)
    keyboard.add_hotkey('ctrl+alt+z', alternar_comandos)

# Crear botón para ON/OFF
toggle_button = tk.Button(window, text="Activar Comandos", command=alternar_comandos)
toggle_button.pack(pady=5)

# Programa principal
contenidos = cargar_contenidos()

def main():
    print("Portapapeles múltiple activo.")
    print("Presiona el botón o usa Ctrl+Alt+Z para ACTIVAR/DESACTIVAR los comandos.\n")

    # Valores predeterminados
    contenidos['1'] = "1er atraso"
    contenidos['2'] = "302015"
    contenidos['3'] = "Asunto Personal"

    actualizar_interfaz()

    # Registrar el atajo Ctrl + Alt + Z para alternar comandos
    keyboard.add_hotkey('ctrl+alt+z', alternar_comandos)

    # Ejecutar la ventana principal
    window.mainloop()

if __name__ == "__main__":
    main()
