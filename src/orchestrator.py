#!/usr/bin/env python3
import threading
import subprocess
import os
import time
import sys


dba_sem = threading.Semaphore(1)
dev_sem = threading.Semaphore(0)
manager_sem = threading.Semaphore(0)

success_flag = []
iteration_count = 0


def dba_agent_thread():
    global iteration_count
    while True:
        if success_flag:
            break
        dba_sem.acquire()
        if success_flag:
            break
        iteration_count += 1
        print(f"[Orchestrator] Ejecutando dba_agent.py (Iteración {iteration_count})...")
        subprocess.run(["python", "dba_agent.py"])
        # Si alcanzamos 10 iteraciones sin éxito, preguntamos al usuario
        if iteration_count >= 10:
            while True:
                user_input = input("Se han realizado 10 iteraciones. ¿Desea continuar iterando con la misma consulta? (S/N): ").strip().upper()
                if user_input == "S":
                    iteration_count = 0
                    break
                elif user_input == "N":
                    new_query = input("¿Desea introducir una nueva consulta? (S/N): ").strip().upper()
                    if new_query == "S":
                        # Eliminar 'query.txt' para forzar la solicitud de una nueva consulta
                        query_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "query.txt")
                        if os.path.exists(query_file):
                            os.remove(query_file)
                        iteration_count = 0
                        break
                    elif new_query == "N":
                        print("[Orchestrator] Saliendo del proceso.")
                        success_flag.append(True)
                        # Liberar semáforos para que los hilos puedan salir
                        dev_sem.release()
                        dba_sem.release()
                        return
                    else:
                        print("Entrada inválida. Por favor, ingrese S o N.")
                else:
                    print("Entrada inválida. Por favor, ingrese S o N.")
        dev_sem.release()
        time.sleep(1)


def dev_agent_thread():
    while True:
        dev_sem.acquire()
        if success_flag:
            break
        print("[Orchestrator] Ejecutando dev_agent.py...")
        ret = subprocess.run(["python", "dev_agent.py"]).returncode
        if ret == 0:
            print("[Orchestrator] Consulta exitosa.")
            success_flag.append(True)
            manager_sem.release()
            break
        else:
            print("[Orchestrator] La consulta no fue exitosa, repitiendo ciclo...\n")
            dba_sem.release()
        time.sleep(1)


def manager_agent_thread():
    manager_sem.acquire()
    if success_flag:
        print("[Orchestrator] Ejecutando manager_agent.py...")
        subprocess.run(["python", "manager_agent.py"])


def orchestrate():
    t_dba = threading.Thread(target=dba_agent_thread)
    t_dev = threading.Thread(target=dev_agent_thread)
    t_manager = threading.Thread(target=manager_agent_thread)
    
    t_dba.start()
    t_dev.start()
    t_manager.start()
    
    t_dba.join()
    t_dev.join()
    t_manager.join()
    
    print("[Orchestrator] Proceso finalizado exitosamente.")
    sys.exit(0)  # <--- Fuerza la salida de Python

if __name__ == "__main__":
    orchestrate()
