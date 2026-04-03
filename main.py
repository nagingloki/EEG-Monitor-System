import pyodbc
import numpy as np
import time

# 1. Configuración de la conexión basada en tu captura de pantalla
# Usamos 'NeuronalActPro' porque es donde se visualizan tus tablas en la imagen
config_db = {
    'server': 'DESKTOP-AKNI7PU',
    'database': 'NeuronalActPro', 
    'trusted_connection': 'yes'
}

# Cadena de conexión para SQL Server con Autenticación de Windows
conn_str = (
    f"Driver={{SQL Server}};"
    f"Server={config_db['server']};"
    f"Database={config_db['database']};"
    f"Trusted_Connection={config_db['trusted_connection']};"
)

def simular_monitoreo_eeg(canal_id, version_id):
    try:
        # Establecer conexión
        print(f"Conectando al servidor {config_db['server']}...")
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        print("--- Sistema Neuronal Act. Pro: Nodo Fog Activo ---")
        
        # Simularemos 3 ráfagas de datos
        for i in range(1, 11):
            print(f"\n[Lectura #{i}] Analizando señal...")
            
            # Simulación de procesamiento en el "Borde" (Fog Computing)
            # En la lectura 2 y 8 forzaremos una anomalía para activar tu Trigger
            if i == 2:
                ratio_ta = 1.85 # Valor alto (> 1.5)
                entropia = 0.35 # Valor bajo (< 0.4)
                
            elif i == 8:
                ratio_ta = 1.92 # Valor alto (> 1.5)
                entropia = 0.28 # Valor bajo (< 0.4)
                
            else:
                ratio_ta = round(np.random.uniform(0.8, 1.2), 4)
                entropia = round(np.random.uniform(0.5, 0.8), 4)
            
            # INSERTAR EN SQL SERVER
            # Nota: Los nombres de columnas deben coincidir con tu diseño relacional
            sql = """
            INSERT INTO Metricas_Analisis 
            (canal_id, version_id, ratio_ta, entropia_senal)
            VALUES (?, ?, ?, ?)
            """
            cursor.execute(sql, (canal_id, version_id, ratio_ta, entropia))
            conn.commit()
            
            print(f" > Métricas enviadas: Ratio T/A: {ratio_ta} | Entropía: {entropia}")

            # VERIFICACIÓN DE ALERTAS EN TIEMPO REAL
            # Consultamos la tabla que tu Trigger llena automáticamente
            cursor.execute("""
                SELECT TOP 1 mensaje, prioridad 
                FROM Alertas_Criticas 
                ORDER BY fecha_alerta DESC
            """)
            alerta = cursor.fetchone()
            
            # Si el ratio fue alto, el trigger debió generar la alerta
            if alerta and ratio_ta > 1.5:
                print(f" >> ALERTA DEL SISTEMA: {alerta[0]}")
                print(f" >> PRIORIDAD: {alerta[1]}")
            
            time.sleep(1.5)

        print("\n--- Simulación completada. Datos persistidos en SQL Server ---")

    except Exception as e:
        print(f"Error de conexión: {e}")
        print("Asegúrate de que el servidor 'DESKTOP-AKNI7PU' esté encendido y pyodbc instalado.")
    finally:
        if 'conn' in locals():
            conn.close()

# Ejecución (Usamos los IDs que ya existen en tu base de datos según tu captura)
# canal_id=1 (el Fp1 que insertaste) y version_id=1
simular_monitoreo_eeg(canal_id=1, version_id=1)