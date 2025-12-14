
---

# 🚀 TALLER 008-009-010: SCM EN EL MUNDO REAL

**Estudiantes:** Javier Esteban Quilumba Lema – Jonathan Tipan  
**Curso:** Construcción y Evolución de Software – GR2SW  
**Fecha:** 22/NOV/2025  
**Caso Analizado:** Healthcare.gov (2013)

---

## 1. Alcance y Caso Analizado

El objetivo del taller fue analizar un caso real donde el **SCM** y los tipos de mantenimiento fueron decisivos. Seleccionamos el desastre del lanzamiento de **Healthcare.gov**, el cual colapsó el 1 de octubre de 2013 debido a fallas críticas:

| Métrica             | Resultado                                                          |
| ------------------- | ------------------------------------------------------------------ |
| Inscripciones día 1 | 6 de 250.000 intentos                                              |
| Tiempo de carga     | 71 segundos                                                        |
| Costo               | $1.7B (sobrepasando los $93.7M iniciales)                          |
| Causa raíz          | Ausencia de SCM, nula integración continua, sin pruebas end-to-end |

El sistema fue recuperado en 6 semanas por un *Tiger Team* aplicando buenas prácticas de SCM.

---

## 2. Metodología

La tarea se completó mediante análisis del caso usando reportes oficiales, artículos técnicos y el archivo entregado en la actividad. Para guiar el proceso usamos prompts diseñados para cada etapa del taller.

### 📌 *Prompts Clave Utilizados*

| # | Prompt Utilizado                                                                                       | Objetivo                                                                                   |
| - | ------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| 1 | **“Explícame cómo abordar un taller basado en SCM usando un caso real de la industria.”**              | Obtener una guía inicial y estructura del análisis.                                        |
| 2 | **“¿Es adecuado analizar Healthcare.gov para este taller? ¿Dónde encuentro información confiable?”**   | Validar el caso y ubicar fuentes oficiales (informes del HHS, Harvard, análisis técnicos). |
| 3 | **“Tengo estas fuentes, ayúdame a identificar el problema principal y los puntos críticos del caso.”** | Sintetizar el evento y los fallos relacionados a SCM.                                      |
| 4 | **“Clasifica el tipo de mantenimiento aplicado en este caso y justifica cada categoría.”**             | Determinar la predominancia del mantenimiento correctivo.                                  |
| 5 | **“Ahora redacta el documento final del taller con conclusiones claras y concisas.”**                  | Generar el entregable final con estructura coherente.                                      |

---

## 3. Conclusión Clave

El caso demuestra que la falta de SCM puede llevar a fallas masivas incluso en sistemas gubernamentales críticos. El mantenimiento aplicado fue **Correctivo (85%)**, debido a defectos críticos en producción desde el primer día. Con la implementación adecuada de SCM (ramas, CI/CD, code reviews y control de cambios), el sistema pasó de 71s → 1s en tiempo de carga y logró más de **1.2 millones de inscripciones**.

**Lección central:**
➡️ *El SCM no es un trámite: es el pilar que garantiza estabilidad, trazabilidad y la capacidad de recuperar un sistema en crisis.*

---
