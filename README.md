# 📚 Library Management - Odoo 18 (Prueba Técnica)

Este módulo permite la gestión de una biblioteca en Odoo 18, cumpliendo todos los puntos requeridos en la prueba técnica.

---

## 🚀 Instalación rápida

### Usando Docker (recomendado)

1. **Clona este repositorio**
   ```bash
   git clone https://github.com/mike50561/library_management.git
   cd library_management
   ```

2. **Estructura del proyecto (recomendada):**

   ```
   library_management/
   ├── docker-compose.yml
   └── addons/
       └── library_management/  ← Aquí está el módulo
   ```

3. **Ejecuta Odoo con Docker**
   > Asegúrate de tener Docker Compose instalados.

   Crea este archivo `docker-compose.yml` si no existe:

   ```yaml
   version: '3.1'
   services:
     db:
       image: postgres:15
       environment:
         POSTGRES_DB: odoo
         POSTGRES_USER: odoo
         POSTGRES_PASSWORD: odoo
       volumes:
         - db-data:/var/lib/postgresql/data
       restart: always

     odoo:
       image: odoo:18.0
       depends_on:
         - db
       ports:
         - "8069:8069"
       environment:
         - HOST=db
         - USER=odoo
         - PASSWORD=odoo
       volumes:
         - ./addons:/mnt/extra-addons
         - odoo-data:/var/lib/odoo
       restart: always

   volumes:
     db-data:
     odoo-data:
   ```

   Luego ejecuta:
   ```bash
   docker-compose up -d
   ```

4. **Accede a Odoo:**  
   Ve a [http://localhost:8069](http://localhost:8069)  
   - Crea una base de datos nueva  
   - Activa el modo desarrollador  
   - Ve a Apps > Actualizar lista > Busca **Library Management** e instálalo

---

3. **Activa el modo desarrollador** en Odoo.

4. **Actualiza la lista de aplicaciones**.

5. **Instala el módulo** desde el menú de Apps.

---

## ⚙️ Funcionalidades principales

### 📖 Catálogo de Libros
- Alta y gestión de libros
- Cálculo automático de **antigüedad**
- Visualización de préstamos por libro

### 👤 Gestión de Socios
- Alta de socios con código único y automático
- Control de cantidad de préstamos activos

### 🔄 Préstamos y Devoluciones
- Registro de nuevos préstamos
- **Bloqueo automático** si el socio tiene 5 libros prestados
- Devolución manual del libro

### 🌐 API REST externa
- Consulta externa de disponibilidad por ISBN
- **Método:** `GET`
- **Ruta:** `/library/book/info/<isbn>`
- **Respuesta:** JSON con estado y datos básicos del libro

📌 Ejemplo:
```
GET http://localhost:8069/library/book/info/9781234567890
```

Respuesta esperada:
```json
{
  "isbn": "9781234567890",
  "disponible": true,
  "titulo": "Nombre del Libro",
  "id": 3
}
```

---

## 🖥️ Requisitos

- Odoo 18.0 Community Edition
- Python 3.13+
- PostgreSQL
- Docker 
- Carpeta de `addons` personalizada o acceso al sistema

---

## 📁 Estructura del módulo

```
library_management/
├── controllers/
│   └── main.py
├── data/
│   └── ir_sequence.xml
├── models/
│   ├── book.py
│   ├── loan.py
│   └── member.py
├── security/
│   └── ir.model.access.csv
├── views/
│   ├── book_views.xml
│   ├── loan_views.xml
│   ├── member_views.xml
│   └── menu_views.xml
├── __manifest__.py
├── __init__.py

```
## 📁 Estructura del Raiz Proyecto
```
├── docker-compose.yml
├── odoo.conf
└── addons/
    └── library_management/

```
---

## 📝 Notas

- El módulo incluye reglas básicas de seguridad y accesos.
- Probado en entorno local con Docker y Odoo 18.
- Si tienes errores, revisa los logs del contenedor o servidor.

---


**¡Gracias por revisar esta prueba técnica!**  
Desarrollado Miguel Angel Herrera  [@mike50561](https://github.com/mike50561)
