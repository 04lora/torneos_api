
# API de Gestión de Torneos Deportivos y Usuarios

API REST desarrollada con **Python y FastAPI**, conectada a **PostgreSQL en Neon**, organizada bajo arquitectura por capas y desplegada en Render.

Implementa el **Ejercicio 13 (Gestión de torneos deportivos)** junto con el módulo independiente de Usuarios.

---

## Enlaces del proyecto

- **Documentación interactiva (Swagger UI):** https://torneos-api-ewey.onrender.com/docs
- **API desplegada en Render:** https://torneos-api-ewey.onrender.com
- **Repositorio en GitHub:** https://github.com/04lora/torneos_api

---

## Tecnologías utilizadas

- **Python 3:** Lenguaje principal de programación.
- **FastAPI:** Framework web utilizado para construir los endpoints REST y generar la documentación automática en Swagger.
- **SQLAlchemy y Pydantic:** Herramientas para el mapeo objeto-relacional (ORM), consultas a PostgreSQL y validación de datos.
- **PostgreSQL en Neon:** Base de datos relacional en la nube.
- **psycopg (psycopg[binary]):** Driver de conexión entre Python y PostgreSQL.
- **python-dotenv:** Gestión de variables de entorno.
- **bcrypt:** Librería utilizada para hashear las contraseñas de los usuarios.
- **Uvicorn:** Servidor ASGI para ejecutar la aplicación.
- **Git y GitHub:** Control de versiones y almacenamiento del código.
- **Render:** Plataforma utilizada para el despliegue de la API.

---

## Módulos desarrollados

### 1. Módulo de Torneos Deportivos (torneos) — Ejercicio 13

Permite administrar torneos deportivos completos mediante operaciones CRUD y un filtro de búsqueda según la disciplina deportiva.

**Archivos asociados:**

- `app/models/torneo.py`
- `app/schemas/torneo_schema.py`
- `app/repositories/torneo_repository.py`
- `app/services/torneo_service.py`
- `app/routes/torneos.py`

**Funcionalidades principales:**

- Registrar torneos deportivos.
- Validar que la fecha de finalización no sea anterior a la fecha de inicio.
- Consultar todos los torneos registrados.
- Filtrar torneos por disciplina deportiva mediante `?disciplina=...`.
- Realizar búsquedas flexibles sin distinguir entre mayúsculas y minúsculas.
- Consultar un torneo por su ID.
- Actualizar los datos de un torneo.
- Eliminar torneos registrados.

### 2. Módulo de Usuarios — Requerimiento obligatorio

Módulo independiente encargado del registro y administración de usuarios, sin relaciones con los torneos ni inicio de sesión obligatorio.

**Archivos asociados:**

- `app/models/usuario.py`
- `app/schemas/usuario_schema.py`
- `app/repositories/usuario_repository.py`
- `app/services/usuario_service.py`
- `app/routes/usuarios.py`

**Funcionalidades principales:**

- Registrar usuarios.
- Validar que el correo electrónico no esté duplicado.
- Almacenar las contraseñas mediante hash con bcrypt.
- Consultar todos los usuarios.
- Buscar usuarios por ID.
- Evitar exponer las contraseñas en las respuestas de la API.
- Actualizar información de usuarios.
- Eliminar usuarios registrados.

### 3. Módulo de Base de Datos y Configuración

**Archivos asociados:**

- `app/database/conexion.py`
- `app/main.py`

**Funcionalidades principales:**

- Cargar la variable de entorno `DATABASE_URL`.
- Configurar el motor de conexión con PostgreSQL en Neon.
- Administrar las sesiones de SQLAlchemy.
- Crear automáticamente las tablas si no existen.
- Registrar los routers de torneos y usuarios en FastAPI.

---

## Arquitectura por capas

El proyecto implementa una arquitectura por capas para separar responsabilidades y evitar mezclar rutas HTTP, reglas de negocio y consultas SQL en un solo archivo.

### Routes (`app/routes/`)

Es la capa de presentación y entrada.

Define los endpoints HTTP (POST, GET, PUT, DELETE), recibe los datos del cuerpo de las peticiones o parámetros de consulta y delega el procesamiento a la capa de servicios.

### Services (`app/services/`)

Contiene la lógica de negocio y las validaciones funcionales.

Por ejemplo:

- Validar las fechas de los torneos.
- Verificar que el correo de un usuario no esté duplicado.
- Hashear las contraseñas con bcrypt.
- Gestionar excepciones HTTP (400 y 404).

### Repositories (`app/repositories/`)

Es la capa de acceso a datos.

Ejecuta las operaciones CRUD y consultas sobre PostgreSQL utilizando los modelos ORM.

### Models (`app/models/`)

Define la estructura de las tablas de la base de datos, sus columnas, tipos de datos y restricciones mediante SQLAlchemy.

### Schemas (`app/schemas/`)

Define los contratos de entrada y salida de la API utilizando Pydantic.

Valida los tipos de datos, las longitudes mínimas y máximas, y asegura que las respuestas de usuarios nunca expongan contraseñas.

### Database (`app/database/`)

Administra la configuración de conexión con Neon, crea el motor (`engine`), gestiona las sesiones (`SessionLocal`) y proporciona la dependencia `get_db()` a los endpoints.

---

## Diagrama de las tablas de la base de datos

Los módulos son independientes entre sí. No requieren llaves foráneas ni relaciones directas entre las tablas.

```text
+-----------------------------------+
|              torneos              |
+-----------------------------------+
| PK | id                   | INT   |
|    | nombre_torneo        | VARCHAR |
|    | disciplina           | VARCHAR |
|    | fecha_inicio         | DATE  |
|    | fecha_finalizacion   | DATE  |
|    | numero_participantes | INT   |
+-----------------------------------+

+-----------------------------------+
|              usuarios             |
+-----------------------------------+
| PK | id              | INT        |
|    | nombre          | VARCHAR    |
| UQ | correo          | VARCHAR    |
|    | password_hash   | VARCHAR    |
+-----------------------------------+
```

## Descripción de las tablas

### Tabla: torneos

Almacena la información de los torneos deportivos registrados en el sistema.

| Campo | Tipo de dato | Restricciones | Descripción |
|---|---|---|---|
| id | INTEGER | Primary Key, Autoincremental, Index | Identificador único del torneo. |
| nombre_torneo | VARCHAR(150) | Not Null | Nombre oficial del torneo. |
| disciplina | VARCHAR(100) | Not Null, Index | Deporte o disciplina del torneo. |
| fecha_inicio | DATE | Not Null | Fecha de inicio del torneo. |
| fecha_finalizacion | DATE | Not Null | Fecha de finalización del torneo. |
| numero_participantes | INTEGER | Not Null | Cantidad de equipos o participantes. |

### Tabla: usuarios

Almacena los datos básicos de los usuarios registrados en el sistema.

| Campo | Tipo de dato | Restricciones | Descripción |
|---|---|---|---|
| id | INTEGER | Primary Key, Autoincremental, Index | Identificador único del usuario. |
| nombre | VARCHAR(120) | Not Null | Nombre completo del usuario. |
| correo | VARCHAR(150) | Not Null, Unique, Index | Correo electrónico único. |
| password_hash | VARCHAR(255) | Not Null | Contraseña protegida mediante hash bcrypt. |

---

## Listado de endpoints implementados

### Módulo de Torneos Deportivos (`/torneos`)

| Método | Endpoint | Parámetros | Descripción | Código HTTP |
|---|---|---|---|---|
| POST | `/torneos/` | Body JSON | Registra un nuevo torneo. | 201 Created |
| GET | `/torneos/` | Query opcional: disciplina | Lista todos los torneos o filtra por disciplina. | 200 OK |
| GET | `/torneos/{torneo_id}` | Path: torneo_id | Consulta un torneo por ID. | 200 OK / 404 |
| PUT | `/torneos/{torneo_id}` | Path y Body JSON | Actualiza un torneo existente. | 200 OK / 404 |
| DELETE | `/torneos/{torneo_id}` | Path: torneo_id | Elimina un torneo. | 200 OK / 404 |

### Módulo de Usuarios (`/usuarios`)

| Método | Endpoint | Parámetros | Descripción | Código HTTP |
|---|---|---|---|---|
| POST | `/usuarios/` | Body JSON | Registra un usuario con contraseña hasheada. | 201 Created |
| GET | `/usuarios/` | Ninguno | Consulta todos los usuarios. | 200 OK |
| GET | `/usuarios/{usuario_id}` | Path: usuario_id | Consulta un usuario por ID. | 200 OK / 404 |
| PUT | `/usuarios/{usuario_id}` | Path y Body JSON | Actualiza los datos de un usuario. | 200 OK / 404 |
| DELETE | `/usuarios/{usuario_id}` | Path: usuario_id | Elimina un usuario. | 200 OK / 404 |

---

## Evidencias de pruebas en Swagger

Las pruebas funcionales de los endpoints se realizaron desde la interfaz interactiva Swagger UI:

https://torneos-api-ewey.onrender.com/docs

### 1. Registro y consulta de usuarios

Pruebas realizadas:

- Registro de usuarios mediante POST `/usuarios/`.
- Consulta de usuarios mediante GET `/usuarios/`.
- Verificación de respuesta `201 Created`.
- Comprobación de que las contraseñas no se exponen.
- Validación del error `400 Bad Request` ante correos duplicados.

**Evidencia:**

![Pruebas de Usuarios en Swagger](docs/swagger_usuarios.png)

### 2. Registro de torneos

Pruebas realizadas:

- Inserción de torneos de distintas disciplinas deportivas.
- Ejemplos: Fútbol, Baloncesto y Voleibol.
- Verificación del código `201 Created`.
- Validación de las fechas del torneo.

**Evidencia:**

![Registro de Torneos en Swagger](docs/swagger_post_torneos.png)

### 3. Filtro por disciplina

Prueba realizada mediante:

`GET /torneos/?disciplina=Fútbol`

Se verifica que la consulta retorne únicamente los torneos correspondientes a la disciplina indicada.

**Evidencia:**

![Filtro por Disciplina en Swagger](docs/swagger_filtro_disciplina.png)

### 4. Operaciones CRUD

Pruebas realizadas:

- GET `/torneos/{id}`: consulta por identificador.
- PUT `/torneos/{id}`: actualización de información.
- DELETE `/torneos/{id}`: eliminación de registros.

Se verifica la persistencia de los datos en Neon y el manejo de respuestas `200 OK` y `404 Not Found`.

**Evidencia:**

![Operaciones CRUD en Swagger](docs/swagger_crud.png)

**Nota:** Las capturas deben guardarse dentro de la carpeta `docs/` en la raíz del repositorio con los nombres indicados anteriormente. Si tienen otros nombres, se deben ajustar las rutas de las imágenes.

---

## Conexión con Neon PostgreSQL

La persistencia de datos se realiza mediante una base de datos PostgreSQL serverless alojada en Neon.

### Configuración de la conexión

**1. Cadena de conexión segura**

Desde el panel de Neon se obtiene la URI de conexión PostgreSQL con SSL habilitado mediante:

`?sslmode=require`

**2. Variables de entorno**

En el entorno local, las credenciales se almacenan en el archivo `.env`, excluido del control de versiones mediante `.gitignore`.

En producción, la variable `DATABASE_URL` se configura desde el panel de Render.

**3. Configuración en SQLAlchemy**

El archivo `app/database/conexion.py` realiza las siguientes funciones:

- Carga las variables de entorno mediante `python-dotenv`.
- Adapta el prefijo de conexión a `postgresql+psycopg://` para utilizar el driver psycopg v3.
- Crea el motor de conexión mediante `create_engine(url)`.
- Configura las sesiones independientes mediante `SessionLocal`.
- Proporciona la dependencia `get_db()` para gestionar las conexiones en cada petición HTTP.

**4. Creación automática de tablas**

Al iniciar `app/main.py`, se ejecuta:

```python
Base.metadata.create_all(bind=engine)
```

Esta instrucción verifica y crea automáticamente las tablas `torneos` y `usuarios` en Neon si todavía no existen.

---

## Estructura del proyecto

```text
torneos_api/
│
├── app/
│   ├── database/
│   │   └── conexion.py
│   │
│   ├── models/
│   │   ├── torneo.py
│   │   └── usuario.py
│   │
│   ├── schemas/
│   │   ├── torneo_schema.py
│   │   └── usuario_schema.py
│   │
│   ├── repositories/
│   │   ├── torneo_repository.py
│   │   └── usuario_repository.py
│   │
│   ├── services/
│   │   ├── torneo_service.py
│   │   └── usuario_service.py
│   │
│   ├── routes/
│   │   ├── torneos.py
│   │   └── usuarios.py
│   │
│   └── main.py
│
├── docs/
│   ├── swagger_usuarios.png
│   ├── swagger_post_torneos.png
│   ├── swagger_filtro_disciplina.png
│   └── swagger_crud.png
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Ejecución del proyecto en local

**1. Clonar el repositorio**

```bash
git clone https://github.com/04lora/torneos_api.git
```

**2. Ingresar a la carpeta**

```bash
cd torneos_api
```

**3. Crear un entorno virtual**

```bash
python -m venv venv
```

**4. Activar el entorno virtual en Windows**

```bash
venv\Scripts\activate
```

**5. Instalar las dependencias**

```bash
pip install -r requirements.txt
```

**6. Configurar las variables de entorno**

Crear un archivo `.env` en la raíz del proyecto:

```env
DATABASE_URL=postgresql+psycopg://usuario:contraseña@host/base_de_datos?sslmode=require
```

Reemplazar los datos de ejemplo por las credenciales reales de Neon.

**7. Ejecutar la aplicación**

```bash
uvicorn app.main:app --reload
```

**8. Abrir la documentación interactiva**

http://127.0.0.1:8000/docs

---

## Seguridad

El proyecto implementa medidas básicas de seguridad:

- Contraseñas almacenadas mediante hash bcrypt.
- Validación de datos con Pydantic.
- Correos electrónicos únicos para los usuarios.
- Protección de credenciales mediante variables de entorno.
- Exclusión del archivo `.env` del repositorio mediante `.gitignore`.
- Respuestas de usuarios sin exposición de contraseñas.

---

## Despliegue

La API se encuentra desplegada en **Render** y utiliza una base de datos PostgreSQL alojada en **Neon**.

- **Render:** alojamiento y ejecución de la API.
- **Neon:** almacenamiento persistente de los datos.
- **GitHub:** repositorio del código fuente.

---

## Autor

**Jhon Lora**

Proyecto desarrollado con Python, FastAPI y PostgreSQL como implementación del Ejercicio 13: Gestión de Torneos Deportivos, incluyendo el módulo obligatorio de Usuarios.
