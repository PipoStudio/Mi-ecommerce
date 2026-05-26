from pathlib import Path

# =========================================================
# CONFIGURA TU RUTA
# =========================================================

PROJECT = Path(
    r"C:\Users\Douglas Osorio 666\Documents\Amplify-chat-main (1)\Amplify-chat-main\Amplify_Limpio"
)

js_file = PROJECT / "js" / "app.js"

# =========================================================
# LEER ARCHIVO
# =========================================================

content = js_file.read_text(encoding="utf-8")

# =========================================================
# FIX #1
# Separar escalas
# =========================================================

content = content.replace(
    'let currentScale = 1;',
    '''let currentScale = 1;

    let interactiveScale = 4;

    let magnifierScale = 1;'''
)

# =========================================================
# FIX #2
# Restaurar escala editorial del cursor interactivo
# =========================================================

old_interactive = '''
currentScale = Math.min(
                Math.max(rect.height / 18, 3),
                6
            );
'''

new_interactive = '''
interactiveScale = Math.min(
                Math.max(rect.height / 8, 4),
                10
            );

            currentScale = interactiveScale;
'''

content = content.replace(
    old_interactive,
    new_interactive
)

# =========================================================
# FIX #3
# Reducir gigantismo del magnifier
# =========================================================

old_magnifier = '''
currentScale = Math.min(
                Math.max(rect.width / 160, 4),
                8
            );
'''

new_magnifier = '''
magnifierScale = Math.min(
                Math.max(rect.width / 320, 2.2),
                4.5
            );

            currentScale = magnifierScale;
'''

content = content.replace(
    old_magnifier,
    new_magnifier
)

# =========================================================
# FIX #4
# Evitar mezcla de active + zoom-mode
# =========================================================

old_zoom = '''
cursor.classList.add("zoom-mode");

            activeImage = el;
'''

new_zoom = '''
cursor.classList.add("zoom-mode");

            cursor.classList.remove("active");

            activeImage = el;
'''

content = content.replace(
    old_zoom,
    new_zoom
)

# =========================================================
# FIX #5
# Limpiar backgroundImage al volver a modo interactivo
# =========================================================

old_active = '''
cursor.classList.add("active");

            const rect = el.getBoundingClientRect();
'''

new_active = '''
cursor.classList.add("active");

            cursor.style.backgroundImage = "none";

            const rect = el.getBoundingClientRect();
'''

content = content.replace(
    old_active,
    new_active
)

# =========================================================
# FIX #6
# Reducir zoom exagerado
# =========================================================

content = content.replace(
    'zoomLevel = Math.max(1.5, Math.min(6, zoomLevel));',
    'zoomLevel = Math.max(1.8, Math.min(4, zoomLevel));'
)

# =========================================================
# GUARDAR
# =========================================================

js_file.write_text(content, encoding="utf-8")

print("✅ Cursor system corregido correctamente.")
print("✅ Hover editorial restaurado.")
print("✅ Magnifier reducido.")
print("✅ Estados active / zoom separados.")
print("✅ Zoom wheel optimizado.")