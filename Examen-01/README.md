# 🔬 EXAMEN 001: INGENIERÍA INVERSA - EL ARTE DEL DETECTIVE DE SOFTWARE

**Estudiantes:** Javier Quilumba – Jonathan Tipan
**Curso:** Construcción y Evolución de Software – GR2SW  
**Fecha:** 14 deDiciembre 2024  
**Aplicación Analizada:** Notion

---

## 1. Alcance y Aplicación Seleccionada

El objetivo del examen fue aplicar **Ingeniería Inversa de Caja Negra** sobre una aplicación real. Seleccionamos **Notion**, una plataforma todo-en-uno de productividad y gestión del conocimiento, por su complejidad arquitectónica:

| **Métrica** | **Resultado** |
|-------------|---------------|
| **Usuarios activos** | 35+ millones (2024) |
| **Modelo de negocio** | Freemium (Personal Free → Enterprise) |
| **Arquitectura inferida** | Microservicios + Colaboración en tiempo real (CRDT/OT) |
| **Diferenciador clave** | Sistema de bloques modulares + bases de datos relacionales integradas |
| **Tecnologías deducidas** | React + TypeScript, Node.js/Go, PostgreSQL, Redis, WebSocket |

Notion combina funcionalidades de Google Docs + Airtable + Trello + Wiki en una sola plataforma, con desafíos técnicos interesantes: sincronización multi-dispositivo, edición concurrente y bases de datos dentro de documentos.

---

## 2. Metodología

El análisis se realizó mediante **Ingeniería Inversa de Caja Negra** (sin acceso al código fuente), observando comportamiento en web, móvil y desktop. Probamos funcionalidades principales, casos límite y dedujimos la arquitectura backend basándonos en patrones observables.

### 📌 Prompts Clave Utilizados

| # | **Prompt Utilizado** | **Objetivo** |
|---|---------------------|--------------|
| 1 | "Dame ideas de apps interesantes para hacer ingeniería inversa, preferiblemente relacionadas con salud o productividad." | Seleccionar aplicación apropiada con lógica de negocio rica. |
| 2 | "Ayúdame a estructurar el análisis de Notion: ¿qué funcionalidades debo explorar primero?" | Obtener guía de análisis sistemático. |
| 3 | "Basándome en este comportamiento observable, ¿qué arquitectura backend deduzco? Genera un diagrama Mermaid." | Inferir arquitectura de microservicios. |
| 4 | "Convierte estas observaciones en historias de usuario formales con el formato: 'Como [usuario], quiero [acción], para [beneficio].'" | Formalizar 24 requisitos funcionales. |
| 5 | "¿Qué modelo de datos necesitaría Notion para soportar bloques anidados y bases de datos relacionales?" | Diseñar modelo entidad-relación con 12 entidades. |
| 6 | "Genera el documento final con diagramas, reglas de negocio, conclusiones y referencias IEEE." | Producir entregable completo. |

---

## 3. Hallazgos Principales

### Requisitos Funcionales
Extrajimos **24 historias de usuario** en 6 categorías:
- **Gestión de Bloques** (5): Crear, transformar, arrastrar, anidar, markdown
- **Bases de Datos** (5): Tablas/kanban, propiedades, filtros, vistas, fórmulas
- **Colaboración** (5): Permisos, tiempo real, menciones, comentarios, notificaciones
- **Plantillas** (3): Crear, duplicar, galería pública
- **Sincronización** (3): Guardado auto, offline, multi-dispositivo
- **Navegación** (3): Favoritos, búsqueda global, anidamiento

### Arquitectura Inferida
Identificamos **8 microservicios principales**:
```
📱 Clientes → 🌐 API Gateway + WebSocket → 
🔧 Auth • Workspace • Block • Database • 
   Collaboration • Search • File • Notification →
💾 PostgreSQL + Redis + S3 + ElasticSearch
```

### Modelo de Datos
**12 entidades clave**, destacando:
- `BLOCK` (recursivo): Bloques pueden contener bloques infinitamente
- `DATABASE` → `DATABASE_ROW` → `PROPERTY_VALUE`: Bases de datos relacionales dentro de documentos
- `WORKSPACE_MEMBER`: Sistema de permisos granular (ver/comentar/editar/admin)

### Reglas de Negocio
- Plan Free: límite de almacenamiento (5MB/archivo), historial (7 días)
- Toda base de datos requiere exactamente UNA propiedad "title"
- Sincronización offline usa last-write-wins para resolver conflictos
- Las menciones (@) solo funcionan con usuarios que tienen acceso a la página

---

## 4. Conclusión Clave

El análisis demuestra que **la complejidad técnica puede esconderse detrás de una UX simple**. Notion ejemplifica principios modernos de ingeniería:

**Lecciones centrales:**

➡️ **Modularidad:** Un solo concepto ("bloque") se extiende a 20+ tipos diferentes sin romper consistencia.

➡️ **Microservicios:** Separar concerns (auth, bloques, bases de datos) permite escalabilidad independiente para 35M+ usuarios.

➡️ **Tiempo Real es Crítico:** CRDT/Operational Transformation resuelve edición concurrente, pero requiere inversión arquitectónica significativa.

➡️ **Freemium Inteligente:** No limita funcionalidades core, sino escala (bloques, historial, storage), maximizando adopción.

➡️ **Ingeniería Inversa como Habilidad:** Analizar sistemas sin código fuente es esencial para mantenimiento de legacy code, análisis competitivo y troubleshooting en el mundo real.

**Impacto:** Las habilidades practicadas (descomposición de sistemas complejos, inferencia arquitectónica, extracción de requisitos) son directamente aplicables a escenarios profesionales donde la documentación es inexistente o el código es inaccesible.

---

**Disclaimer:** Este análisis fue realizado con fines exclusivamente educativos. Todo el análisis se basó en observación de comportamiento público (caja negra) sin acceso a código propietario ni violación de términos de servicio.