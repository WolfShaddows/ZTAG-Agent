# ZTAG: Zero-Trust Agentic Guard (NSA Edition)

**ZTAG** es un pipeline de gobernanza autonoma diseñado para modernizar aplicaciones legacy bajo el estandar **Zero Trust Implementation Guideline (NSA, Enero 2026)**.

##  Como funciona
El sistema separa la **Auditoria de Cumplimiento** de la **Remediacion de Codigo**, asegurando que cada cambio este respaldado por normativas oficiales.

1. **Ingesta de Conocimiento:** Usamos **Docling** para procesar el manual de la NSA y convertirlo en un cerebro de reglas.
2. **Auditoria (El Fiscal):** Analiza el codigo fuente y genera un reporte de fallos citando actividades especificas de la NSA (1.4.1, 2.4.1, etc.).
3. **Remediacion (IBM Bob):** El agente de codificacion recibe el reporte y refactoriza el codigo para eliminar vulnerabilidades de confianza implicita.



##  Stack Tecnico
- **IBM Bob:** Agentic coding partner para refactorizacion.
- **Watsonx.ai (Granite):** Motor de razonamiento para auditoria.
- **Docling:** Extraccion inteligente de documentos tecnicos.
- **Python:** Orquestacion local y soberana.

##  Estructura del Proyecto
- `/knowledge`: Manuales oficiales de la NSA.
- `/src`: Logica del Auditor y del Fixer.
- `/tests`: Codigo legacy vulnerable.
- `/results`: Reportes de cumplimiento y codigo refactorizado.

##  Uso
1. Colocar el manual NSA en `/knowledge/1769475823091.pdf`
2. Ejecutar `python main.py`
3. Revisar resultados en `/results`

##  Matriz de Cumplimiento (NSA v1.0)

| Actividad NSA | Riesgo Detectado | Remediacion ZTAG | Estado |
| :--- | :--- | :--- | :--- |
| **1.4.1 PAM** | Credenciales Hardcodeadas | Inyeccion de Env Vars |  Corregido |
| **2.4.1 Trust** | SQL & Command Injection | Parametrizacion Estricta |  Corregido |
| **7.3.1 Logs** | Falta de Auditoria | Estructura para Logging |  Listo |