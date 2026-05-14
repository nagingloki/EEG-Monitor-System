# 🧠 NeuralActPro: EEG Data Monitoring & Persistence System
Sistema integral para la gestión, persistencia y análisis de señales electroencefalográficas (EEG), diseñado bajo una arquitectura relacional robusta en **SQL Server** y una interfaz de monitoreo en tiempo real con **Python (Streamlit)**.
## 🚀 Descripción del Proyecto
Este proyecto soluciona el problema de la persistencia de datos fisiológicos de alta frecuencia. Permite registrar pacientes, iniciar sesiones de grabación de señales cerebrales, procesar métricas en tiempo real y disparar alertas críticas basadas en umbrales médicos configurables.
## 🛠️ Stack Tecnológico
 * **Base de Datos:** SQL Server (Relacional).
 * **Modelado:** Oracle SQL Developer Data Modeler.
 * **Lenguaje:** Python 3.x.
 * **Interfaz:** Streamlit.
 * **Librerías Clave:** pyodbc, pandas, numpy, matplotlib.
## 📊 Arquitectura de Datos
El diseño se basa en una jerarquía de dependencias lineal en **Tercera Forma Normal (3FN)** para garantizar la integridad referencial y evitar redundancias:
 1. **Pacientes:** Entidad raíz con identificadores únicos (CURP).
 2. **Sesiones:** Agrupación cronológica de grabaciones por paciente.
 3. **Canales EEG:** Segregación física de electrodos (Fp1, Fp2, etc.).
 4. **Métricas:** Datos procesados (Potencias Alpha, Beta, Theta, Delta; Entropía).
 5. **Alertas:** Eventos disparados por anomalías en las métricas.
## ⚙️ Características Principales
 * **Integridad Referencial Total:** Implementación de ON DELETE CASCADE para mantener la base de datos libre de registros huérfanos.
 * **Inyector de Datos:** Script automatizado para la simulación de entrada de señales EEG mediante lotes de datos.
 * **Dashboard en Tiempo Real:** Visualización dinámica de métricas y estados del paciente mediante Streamlit.
 * **Trazabilidad Algorítmica:** Registro de versiones de algoritmos para auditoría de resultados médicos.
## 📝 Reglas de Negocio
 * Cada sesión de grabación debe estar vinculada obligatoriamente a un paciente registrado.
 * Las alertas críticas no pueden existir sin una métrica de origen que las respalde.
 * El sistema permite la trazabilidad completa desde una alerta hasta el electrodo específico que capturó la señal.
## 🏁 Instalación y Uso
 1. Clonar el repositorio.
 2. Ejecutar el script DDL en tu instancia de **SQL Server** para crear la estructura.
 3. Configurar el archivo de conexión (pyodbc) con tus credenciales locales.
 4. Lanzar la aplicación:
   ```bash
   streamlit run app.py
   
   ```
**Autor:** Daniel Lopez – Estudiante de Ingeniería Biomédica @ Instituto Tecnológico de Tijuana.
```

```
