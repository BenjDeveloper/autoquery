#!/usr/bin/env python3
from langchain_ollama import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import os
import sys


dba_prompt_template = PromptTemplate(
    template=(
        "Eres un DBA experto en SQL y estructuras relacionales. "
        "A continuación tienes el esquema completo de una base de datos. "
        "Tu tarea es generar una consulta SQL correcta, precisa y útil para responder a la petición del usuario.\n\n"
        "ESQUEMA DE BASE DE DATOS:\n{schema}\n\n"
        "CONSULTA DEL USUARIO:\n{query}\n\n"
        "INSTRUCCIONES:\n"
        "- Lee y analiza completamente el esquema antes de generar la consulta.\n"
        "- Detecta claves foráneas, nombres de columnas y relaciones entre tablas.\n"
        "- Si el usuario **no especifica qué columnas quiere**, devuelve **todas las columnas relevantes de las tablas involucradas** usando SELECT * o nombres explícitos.\n"
        "- Si menciona nombres como 'sección A', verifica si hay un campo que contenga ese valor ('tag', 'name', etc.).\n"
        "- Si el valor pertenece a otra tabla relacionada, haz un JOIN correctamente.\n"
        "- NO inventes columnas ni tablas. Usa solo las que existen en el esquema.\n"
        "- Usa LIKE, condiciones, JOINs y alias según sea necesario.\n"
        "- Tu objetivo es que la consulta sea ejecutable y devuelva datos reales.\n"
        "- Devuelve solo la consulta SQL, con comentarios opcionales si ayudan a entenderla.\n\n"
        "-- CONSULTA SQL --"
    ),
    input_variables=["schema", "query"]
)

# dba_chain = LLMChain(llm=OllamaLLM(model="gemma3:1b"), prompt=dba_prompt_template)
dba_chain = LLMChain(llm=OllamaLLM(model="llama3:8b"), prompt=dba_prompt_template) 


def load_schema(schema_file):
    """
    Lee y retorna el contenido del archivo que contiene el esquema de la base de datos.
    """
    try:
        with open(schema_file, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Error al leer el fichero {schema_file}: {e}", file=sys.stderr)
        sys.exit(1)


def get_query():
    # Si ya existe el archivo 'query.txt', lo lee y devuelve su contenido;
    # en caso contrario, solicita la consulta al usuario y la guarda.
    query_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "query.txt")
    if os.path.exists(query_file):
        with open(query_file, "r", encoding="utf-8") as f:
            query_text = f.read().strip()
        print(f"[DEBUG] Usando consulta guardada: {query_text}")
    else:
        query_text = input("Ingrese la consulta DBA (por ejemplo, 'Extrae todos los registros de clientes activos'): ").strip()
        with open(query_file, "w", encoding="utf-8") as f:
            f.write(query_text)
    return query_text


def generate_dba_response():
    # Solicita la consulta (o la usa si ya fue ingresada), carga el esquema desde 'db_schema.sql'
    # y genera la respuesta del DBA, que se guarda en 'respuesta.txt'.
    schema_file_name = "db_schema.sql"
    schema_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), schema_file_name)
    query_text = get_query()
    schema = load_schema(schema_file)
    
    print("\n[DEBUG] Generando la respuesta del DBA...")
    response = dba_chain.invoke({"schema": schema, "query": query_text})
    response_text = response["text"] if isinstance(response, dict) and "text" in response else str(response)
    
    print("\n=== Respuesta del DBA ===")
    print(response_text)
    output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "respuesta.txt")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(response_text)
        print(f"\nFichero generado: {output_file}")
    except Exception as e:
        print(f"\n[ERROR] Error al escribir el fichero {output_file}: {e}", file=sys.stderr)


if __name__ == "__main__":
    generate_dba_response()
