# PokeApp — Explorador de Pokémon

Una aplicación web interactiva desarrollada con **Flask** y **PokéAPI**, que permite buscar información detallada de cualquier Pokémon: su imagen, tipos y movimientos principales.  
Diseñada con un enfoque **UX/UI moderno**, totalmente **responsive** y con una interfaz inspirada en la estética de la **Pokédex**.
Demo aquí: https://api-project-ji18.onrender.com

---

##  Características principales

- **Búsqueda dinámica** de Pokémon por nombre.  
- **Visualización de imagen oficial** del Pokémon.  
- **Tipos y movimientos** obtenidos directamente desde la PokéAPI.  
- **Diseño moderno y translúcido**, con fondo temático del mundo Pokémon.  
- **Responsive** para móviles, tablets y escritorio.  
- **Favicon personalizado** con una Pokébola.

---

## Tecnologías utilizadas

| Categoría | Herramienta |
|------------|--------------|
| Backend | Python 3 + Flask |
| API | [PokéAPI](https://pokeapi.co/) |
| Frontend | HTML5, CSS3 (Flexbox, Responsive Design) |
| Estilo | Google Fonts (Poppins), efectos blur y chips dinámicos |
| Servidor local | Flask Development Server |

---

## Estructura del proyecto

```
API-Project/
│
├── app.py                  # Lógica principal de Flask
├── templates/
│   └── index.html          # Interfaz web con Jinja2
├── static/
│   ├── style.css           # Estilos y diseño responsive
│   ├── pokemon_world.jpeg  # Fondo temático Pokémon
│   └── pokeball.png        # Favicon (Pokébola)
└── README.md               # Documentación del proyecto
```

---

## Instalación y ejecución

### Clonar el repositorio
```bash
git clone https://github.com/tuusuario/pokeapp.git
cd pokeapp
```

### Instalar dependencias
```bash
pip install flask requests
```

### Ejecutar la aplicación
```bash
python app.py
```

### Abrir en el navegador
```
http://127.0.0.1:5000
```

---

## Uso de la PokéAPI

La aplicación consume la **PokéAPI** mediante solicitudes HTTP con la librería `requests`.  
Cada búsqueda se realiza con la siguiente estructura:

```python
URL = "https://pokeapi.co/api/v2/pokemon"
response = requests.get(f"{URL}/{pokemon}")
```

La respuesta JSON incluye toda la información del Pokémon, de la cual se extraen:

| Campo | Descripción |
|--------|--------------|
| `sprites.front_default` | Imagen oficial del Pokémon |
| `types` | Lista de tipos (agua, fuego, planta, etc.) |
| `moves` | Lista de movimientos disponibles |

Ejemplo de respuesta simplificada:
```json
{
  "name": "pikachu",
  "sprites": {"front_default": "https://..."},
  "types": [{"type": {"name": "electric"}}],
  "moves": [{"move": {"name": "thunder-shock"}}, ...]
}
```

---

## Diseño UX/UI

- **Cards translúcidas:** integradas con el fondo mediante `backdrop-filter: blur()`.  
- **Movimientos tipo chips:** etiquetas interactivas con hover animado.  
- **Scroll invisible:** mantiene la estética limpia.  
- **Responsive:** adaptado con media queries para pantallas pequeñas.  
- **Fondo temático:** imagen del mundo Pokémon (`pokemon_world.jpeg`).  
- **Favicon:** ícono de Pokébola (`pokeball.png`).

---

## Mejoras futuras

- Cambiar color dinámicamente según el tipo del Pokémon.  
- Mostrar estadísticas base (HP, ataque, defensa).  
- Integrar búsqueda por ID o generación.  
- Añadir traducción de nombres y descripciones en español.

---

## Licencia

Este proyecto utiliza la **PokéAPI** bajo licencia abierta para uso educativo y no comercial.  
Pokémon y sus elementos visuales son propiedad de **The Pokémon Company**.

---
