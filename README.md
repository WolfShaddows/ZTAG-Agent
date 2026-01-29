#  ZTAG: Zero-Trust Agentic Guard (NSA Edition) 
## ZTAG es un pipeline de gobernanza autónoma diseñado para auditar y refactorizar aplicaciones legacy bajo los estándares más estrictos de ciberseguridad: el Zero Trust Implementation Guideline (NSA, Enero 2026).

### ¿Para qué es útil?
En el desarrollo moderno, la IA genera código a una velocidad sin precedentes, a menudo introduciendo vulnerabilidades. ZTAG actúa como un "Fiscal Digital" que asegura que ningún código llegue a producción si viola los principios de:

Privileged Access Management: Eliminación de secretos expuestos.

Deny by Default: Verificación estricta de cada flujo de datos.

Soberanía de Datos: Procesamiento local para infraestructuras críticas que no pueden depender de la nube pública.

### Stack Tecnológico
IBM Bob: Socio agentic para la refactorización inteligente de código.

Docling: Motor de ingesta para procesar y comprender manuales técnicos en PDF (IA de diseño de documentos).

Python 3.10+: Lenguaje base para la orquestación soberana.

RapidOCR: Visión artificial para extraer conocimiento de diagramas y tablas normativas.

### Requisitos e Instalación

Requisitos del Sistema

SO: Windows/Linux/macOS.

Python: Versión 3.10 o superior.

Hardware: Se recomienda 8GB de RAM (para el procesamiento de modelos de Docling).

### Instalación de Librerías
Ejecutá el siguiente comando para instalar las dependencias necesarias:
 "pip install docling rapidocr-onnxruntime python-dotenv ibm-watsonx-ai"

### Cómo usarlo
1-Configuración de Normativa: Colocá el manual de la NSA (o cualquier guía de cumplimiento) en la carpeta /knowledge.

2-Preparación de Código: Poné tus archivos vulnerables en la carpeta /tests.

3-Ejecución: Corre el orquestador principal:

4-Bash
python main.py
-Resultados: * Revisá results/audit_report.txt para ver las infracciones detectadas.

-Revisá los archivos fixed_app.py para obtener el código refactorizado por IBM Bob.

### Arquitectura de Replicación
Para que otros desarrolladores escalen este proyecto a IBM Cloud, el sistema está preparado para recibir credenciales mediante un archivo .env:

### Opcional para integracion con Watsonx.ai

#### "IBM_WATSONX_APIKEY=tu_api_key"
#### "IBM_WATSONX_PROJECT_ID=tu_project_id"

#### "Nota: Por diseño, ZTAG prioriza la ejecución Edge-First. Esto permite que el sistema funcione en entornos aislados (Air-gapped), garantizando que el código auditado nunca abandone el perímetro seguro del cliente."

