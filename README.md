# 🤖 AutoQuery

**AutoQuery** es un sistema automatizado impulsado por inteligencia artificial que permite transformar preguntas en lenguaje natural sobre una base de datos en consultas SQL ejecutables. Ideal para entornos donde se requiere agilidad en el análisis de datos sin necesidad de conocimientos técnicos avanzados en SQL. El flujo del sistema está dividido en tres agentes que trabajan coordinadamente que trabajan con una base de datos para consultas SQL, utilizando un modelo de lenguaje (LLM) y validación automatizada.

---

## 🚀 Características

- 🔄 Ejecución iterativa de consultas hasta obtener resultados válidos.
- 🧠 Generación de consultas SQL utilizando un modelo LLM (`llama3:8b` con LangChain + Ollama).
- 🧪 Validación automática contra una base de datos MySQL (antes PostgreSQL).
- 📊 Visualización de resultados en consola y exportación a archivos.
- 👥 Sistema modular con agentes dedicados: DBA, Dev y Manager.

---

## 🧩 Estructura del Proyecto

```
AutoQuery/
├── orchestrator.py         # Coordina la ejecución de los agentes
├── dba_agent.py            # Genera la consulta SQL a partir de lenguaje natural
├── dev_agent.py            # Ejecuta la consulta y guarda los resultados
├── manager_agent.py        # Muestra los datos resultantes en una tabla
├── db_schema.sql           # Esquema de la base de datos (definido por el usuario)
├── query.txt               # Pregunta del usuario en lenguaje natural
├── respuesta.txt           # Respuesta generada por el modelo (SQL + explicación)
├── respuesta_existosa.txt  # Consulta SQL que funcionó correctamente
├── data.csv                # Resultados en formato CSV
├── output.txt              # Tabla legible con los datos
```

---

## ⚙️ Requisitos

- Python 3.8+
- PostgreSQL (con base de datos accesible desde el script)
- Dependencias de Python:

```bash
pip install -r requirements.txt
```

Ejemplo de `requirements.txt`:
```text
psycopg2
pandas
prettytable
langchain
ollama
```

- Tener corriendo [Ollama](https://ollama.com/) y tener descargado el modelo `llama3:8b`.

---

## ▶️ Cómo usar

1. Asegúrate de tener configurado `Ollama` con el modelo adecuado (`ollama run llama3:8b`).
2. Define el esquema de tu base de datos en `db_schema.sql`.
3. Ejecutá el orquestador:

```bash
python orchestrator.py
```

4. El sistema te pedirá que ingreses una consulta en lenguaje natural (ejemplo: `¿Cuántos usuarios activos hay en el sistema?`).
5. El proceso se ejecutará automáticamente hasta generar y ejecutar correctamente la consulta.

---

## 🎯 Ejemplo de uso

```
Ingrese la consulta DBA: Lista los productos más vendidos este mes

[Orchestrator] Ejecutando dba_agent.py...
[Orchestrator] Ejecutando dev_agent.py...
[Orchestrator] Consulta exitosa.
[Orchestrator] Ejecutando manager_agent.py...

=== Datos de la Consulta ===
| producto | ventas |
|----------|--------|
| Café     | 123    |
| Té       | 87     |
```

---

## 📌 Notas

- Tras 10 intentos fallidos, el sistema permite cambiar la consulta o salir del proceso.
- Las consultas exitosas se almacenan automáticamente para referencia futura.
- Pensado para entornos de desarrollo, pruebas o como asistente para analistas de datos.

---

---

## 🛠️ Configuración Adicional

### 1. Instalar Ollama

Para ejecutar este proyecto necesitas tener [Ollama](https://ollama.com/library) instalado en tu máquina. Puedes seguir las instrucciones oficiales aquí:  
🔗 https://ollama.com/library

### 2. Descargar el modelo LLM

El modelo utilizado en este proyecto es `llama3:8b`. Una vez tengas instalado Ollama, puedes descargarlo con:

```bash
ollama run llama3:8b
```

### 3. Python

Este proyecto fue probado con **Python 3.10**. Se recomienda usar esa versión para garantizar compatibilidad.

### 4. Crear archivo requirements.txt

Si no lo tienes aún, puedes crear un archivo llamado `requirements.txt` con este contenido:

```text
pymysql
pandas
prettytable
langchain
ollama
```

Y luego instalar las dependencias con:

```bash
pip install -r requirements.txt
```

---


## 📜 Licencia

Este proyecto está licenciado bajo los términos de la [MIT License](LICENSE).

---

## 🧑‍💻 Autor

Desarrollado por Ben — si te resulta útil, ¡no olvides dar una ⭐ en GitHub!
