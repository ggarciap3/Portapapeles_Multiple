# 📋 Portapapeles Múltiple

Este programa permite copiar, guardar y reutilizar múltiples fragmentos de texto mediante combinaciones de teclas rápidas. Ideal para usuarios que trabajan con textos repetitivos o datos frecuentes.

## 🧩 Características

- Guarda múltiples contenidos del portapapeles en "casillas" numeradas.
- Pega el contenido de una casilla con una combinación de teclas.
- Interfaz gráfica para visualizar y gestionar los textos guardados.
- Funciona en segundo plano mientras usas otras aplicaciones.
- Puedes activar o desactivar la funcionalidad con un atajo.

---

## 🛠️ Requisitos

- Sistema operativo: **Windows**
- No se requiere tener Python instalado. El ejecutable ya incluye todo lo necesario.

---

## 🚀 Instalación y Uso

1. Descarga el archivo `clip_store.exe` generado.
2. Haz doble clic para ejecutarlo. Se abrirá una ventana con la interfaz.
3. Usa los siguientes atajos globales para interactuar con el portapapeles:

### ⌨️ Atajos de teclado

| Acción                       | Atajo                               |
| ---------------------------- | ----------------------------------- |
| Guardar en casilla `n`       | `Ctrl + C + n` (ej. `Ctrl + C + 1`) |
| Pegar desde casilla `n`      | `Ctrl + n` (ej. `Ctrl + 1`)         |
| Limpiar todo el portapapeles | `Ctrl + J`                          |
| Activar/Desactivar comandos  | `Ctrl + Alt + Z`                    |

> ✅ Puedes almacenar hasta 10 textos, usando los números del 0 al 9 como casillas.

---

## 💾 Datos guardados

Los textos se guardan automáticamente en un archivo llamado `contenidos.json`, en la misma carpeta donde se ejecuta el programa.

---

## 🧼 Botón “Formatear Contenidos”

En la interfaz puedes hacer clic en el botón **"Formatear Contenidos"** para borrar todos los textos guardados.

---

## 🧪 Ejemplo de uso

1. Copia cualquier texto (`Ctrl + C`).
2. Presiona `Ctrl + C + 2` para guardarlo en la casilla 2.
3. Luego, en cualquier otra app, presiona `Ctrl + 2` para pegar ese contenido donde quieras.
4. Presiona `Ctrl + Alt + Z` para activar o desactivar esta funcionalidad si no la necesitas temporalmente.

---

## 🧙 Autor

**Aron García**  
📧 arongarcia558@gmail.com

---

## 🏁 Compilación (solo para desarrolladores)

Si deseas generar el `.exe` tú mismo:

```bash
pyinstaller --clean --onefile --windowed clip_store.py
```
