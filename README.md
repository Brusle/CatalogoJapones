# Catálogo de Personajes de Anime con Búsqueda Vectorial

## Descripción General

El **Catálogo Japonés** es una aplicación web desarrollada con Python y Django que funciona como un catálogo interactivo de personajes de anime. Su principal característica es un motor de búsqueda semántica que permite a los usuarios encontrar personajes escribiendo descripciones en lenguaje natural (por ejemplo, "el soldado más fuerte de la humanidad"). La aplicación utiliza una base de datos vectorial (ChromaDB) y modelos de embeddings (`sentence-transformers`) para comparar la similitud entre la consulta del usuario y las biografías de los personajes, ofreciendo resultados precisos y relevantes.

---

## 🚀 Características Principales

- **Búsqueda Semántica Avanzada:** Entiende el significado de las descripciones, no sólo palabras clave.
- **Interfaz de Usuario Interactiva:** Diseño web moderno y atractivo con HTML y CSS.
- **Doble Métrica de Búsqueda:** Permite elegir entre *Similaridad Coseno* y *Distancia Euclidiana* para afinar los resultados.
- **Catálogo Completo de Personajes:** Página dedicada que muestra todos los personajes y animes disponibles, agrupados por serie.
- **Diseño Visual Coherente:** Cada sección tiene un fondo personalizado y una paleta de colores unificada.

---

## 🛠️ Tecnologías Utilizadas

- **Backend:** Python, Django
- **Base de Datos Vectorial:** ChromaDB
- **Modelo de Embeddings:** `sentence-transformers`
- **Análisis de Datos:** Pandas
- **Frontend:** HTML5, CSS3, JavaScript
- **Manejo de Entorno:** `python-dotenv`

---

## ⚙️ Guía de Instalación y Puesta en Marcha

### 1. Prerrequisitos

- Python 3.8 o superior (recomendado Python 3.11)
- `pip` (gestor de paquetes de Python)

### 2. Clonación del Proyecto

```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio
```

### 3. Creación y Activación del Entorno Virtual

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Instalación de Dependencias

Crea un archivo `requirements.txt` con el siguiente contenido:

```
Django
pandas
chromadb
sentence-transformers
python-dotenv
```

Instala las dependencias:

```bash
pip install -r requirements.txt
```

### 5. Configuración del Entorno

Asegúrate de tener un archivo `.env.dev` en la raíz del proyecto con las variables de entorno necesarias (rutas, datos sensibles, configuraciones de la base de datos, etc.).

### 6. Generación de la Base de Datos Vectorial

La primera vez que se realice una búsqueda, el sistema generará automáticamente la base de datos `chroma_db`. También puedes crearla manualmente ejecutando:

```bash
python vector_db.py
```

### 7. Aplicar Migraciones de Django

```bash
python manage.py migrate
```

### 8. Iniciar el Servidor de Desarrollo

```bash
python manage.py runserver
```

### 9. Acceso a la Aplicación

Abre tu navegador y visita: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🗂️ Estructura del Proyecto

- `manage.py` : Script principal de Django.
- `vector_db.py` : Genera e indexa la base de datos vectorial con ChromaDB.
- `requirements.txt` : Lista de dependencias necesarias.
- `.env.dev` : Variables de entorno para configuración local.
- `/catalogo/` : Módulo principal de Django (vistas, modelos, urls, etc.).
- `/templates/` : Archivos HTML de las diferentes páginas.
- `/static/` : Archivos estáticos (imágenes, CSS, JS).
- `/data/` : Archivos CSV/JSON con los datos de personajes y animes.
- `chroma_db/` : Carpeta donde se almacena la base de datos vectorial generada.

---

## 🖥️ Flujo de la Aplicación y Descripción de Páginas

- **Página de Bienvenida (`welcome.html`):**
  - **Fondo:** `fondo1.png`
  - **Descripción:** Página minimalista con un solo botón para "Iniciar Búsqueda".

- **Página de Selección de Búsqueda (`search_selection.html`):**
  - **Fondo:** `fondo2.png`
  - **Descripción:** Barra de navegación superior para elegir la métrica de búsqueda. Área central para escribir la descripción del personaje y buscar. Incluye enlace para ver el catálogo completo.

- **Página de Catálogo de Personajes (`character_list.html`):**
  - **Fondo:** `fondo3.png`
  - **Descripción:** Lista completa de personajes agrupados por anime. Incluye botón para regresar a la búsqueda.

- **Página de Resultados (`search_results.html`):**
  - **Fondo:** `fondo4.png`
  - **Descripción:** Muestra las 3 tarjetas de personajes más relevantes a la consulta, ordenadas por afinidad. Cada tarjeta contiene imagen, nombre, anime y puntuación de similitud.

---

## 📝 Notas sobre Configuración

- Verifica y ajusta las rutas en el archivo `.env.dev` según tu entorno local.
- Si cambias la ubicación de los datos de personajes/animes, actualiza las rutas en los scripts que los cargan.
- La base de datos vectorial se crea en la carpeta `chroma_db` por defecto. Puedes modificar esta ruta en el código si lo requieres.

---

## 🤝 Contribución

¡Las contribuciones son bienvenidas! Para colaborar:

1. Haz un fork del repositorio.
2. Crea una rama con tus mejoras:
   ```bash
   git checkout -b mi-feature
   ```
3. Realiza tus cambios y haz commits descriptivos.
4. Envía un pull request detallando tus aportaciones.

Por favor, sigue el estilo y estructura del código existente y agrega pruebas si es posible.

---

## 👤 Autor

**Mauricio González Sánchez**

