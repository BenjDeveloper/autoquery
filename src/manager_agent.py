#!/usr/bin/env python3
import os
import pandas as pd
from prettytable import PrettyTable
import sys

def main():
    csv_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data.csv")
    try:
        df = pd.read_csv(csv_file)
    except Exception as e:
        print(f"[ERROR] No se pudo leer el archivo {csv_file}: {e}")
        return
    
    # Crear tabla con PrettyTable
    table = PrettyTable()
    table.field_names = list(df.columns)
    for _, row in df.iterrows():
        table.add_row(row.tolist())
    
    # Imprimir la tabla en terminal
    print("\n=== Datos de la Consulta ===")
    #print(table)
    
    # Guardar la tabla formateada en 'output.txt'
    output_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output.txt")
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(str(table))
        print(f"\n[DEBUG] Tabla guardada en: {output_file}")
        return
    except Exception as e:
        print(f"[ERROR] No se pudo guardar el archivo {output_file}: {e}")

if __name__ == "__main__":
    main()
