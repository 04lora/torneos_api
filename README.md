# API de Gestión de Torneos Deportivos y Usuarios

API REST desarrollada con **Python** y **FastAPI**, conectada a **PostgreSQL en Neon**, organizada bajo **arquitectura por capas** y desplegada en **Render**[cite: 1, 11]. Implementa el **Ejercicio 13 (Gestión de torneos deportivos)** junto con el módulo independiente de **Usuarios**[cite: 5, 9, 10].

## Enlaces del proyecto
- **Documentación interactiva (Swagger UI):** `https://torneos-api-ewey.onrender.com/docs`
- **API desplegada en Render:** `https://torneos-api-ewey.onrender.com`
- **Repositorio en GitHub:** `https://github.com/04lora/torneos_api`

## Tecnologías utilizadas
- **Lenguaje:** Python 3[cite: 11]
- **Framework:** FastAPI[cite: 11]
- **ORM y validación:** SQLAlchemy y Pydantic[cite: 11]
- **Base de datos:** PostgreSQL alojada en Neon[cite: 1, 11]
- **Seguridad de contraseñas:** Hash con `bcrypt`
- **Control de versiones y despliegue:** Git / GitHub y Render[cite: 11]

## Arquitectura por capas
El proyecto separa responsabilidades para mantener un código limpio, modular y fácil de sustentar[cite: 11, 13]:

- `app/routes/`: Define los endpoints HTTP, recibe parámetros y delega en la capa de servicios[cite: 11].
- `app/services/`: Contiene la lógica de negocio, validaciones de reglas y manejo de errores HTTP[cite: 11].
- `app/repositories/`: Ejecuta las operaciones de lectura, escritura, filtrado y borrado en la base de datos[cite: 11].
- `app/models/`: Define los modelos/tablas de PostgreSQL (`torneos` y `usuarios`)[cite: 9, 11].
- `app/schemas/`: Valida los datos de entrada y formatea las respuestas de la API[cite: 11].
- `app/database/`: Administra el motor de conexión, sesiones y variables de entorno hacia Neon[cite: 11].
- `app/main.py`: Inicializa la aplicación FastAPI, crea las tablas si no existen y registra los routers[cite: 11].

## Estructura del proyecto
```text
proyecto/
├── app/
│   ├── database/
│   │   └── conexion.py
│   ├── models/
│   │   ├── torneo.py
│   │   └── usuario.py
│   ├── schemas/
│   │   ├── torneo_schema.py
│   │   └── usuario_schema.py
│   ├── repositories/
│   │   ├── torneo_repository.py
│   │   └── usuario_repository.py
│   ├── services/
│   │   ├── torneo_service.py
│   │   └── usuario_service.py
│   ├── routes/
│   │   ├── torneos.py
│   │   └── usuarios.py
│   └── main.py
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md