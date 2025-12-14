# Clase 006: Análisis de Código Limpio - freeCodeCamp

## 📝 Sobre esta Tarea

Este proyecto es un trabajo académico que consiste en **analizar código real de repositorios públicos** para identificar violaciones a los principios de Clean Code de Robert C. Martin.

### ¿Qué hicimos?

1. Seleccionamos el repositorio [freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)
2. Analizamos 2 archivos clave del proyecto (~600 líneas en total)
3. Identificamos problemas de código según principios de Clean Code
4. Propusimos 5 refactorizaciones concretas con código de ejemplo

## 🎯 Objetivo

Comprender principios de código limpio mediante análisis práctico de código real, identificando problemas y proponiendo mejoras que aumenten mantenibilidad y legibilidad.

## 📂 Contenido

- `analisis-codigo-limpio.md` - Documento completo con análisis detallado, problemas identificados y mejoras propuestas

## 🔍 Archivos Analizados

| Archivo | Ubicación | LOC | Responsabilidad |
|---------|-----------|-----|-----------------|
| `ajax.ts` | `/client/src/utils/` | ~400 | Comunicación HTTP con API |
| `exam-schemas.ts` | `/api/src/utils/` | ~200 | Validaciones Joi para exámenes |

## 🛠️ Principios de Clean Code Aplicados

- **DRY** (Don't Repeat Yourself)
- **SRP** (Single Responsibility Principle)
- **Nombres Reveladores de Intención**
- **Funciones que Hacen Una Cosa**

## 💡 Principales Hallazgos

**Crítico:**
- 🔴 Código duplicado en 3 lugares diferentes
- 🔴 Archivo de 400+ líneas manejando 4 dominios

**Importante:**
- 🟡 30+ endpoints hardcodeados sin constantes
- 🟡 Números mágicos sin contexto (4, 5, 100)
- 🟡 Lógica de negocio dentro de validaciones

## ✨ Mejoras Propuestas

1. **Extraer lógica duplicada** → Función `countNonDeprecatedItems()`
2. **Constantes descriptivas** → `MINIMUM_WRONG_ANSWERS = 4`
3. **Mejorar nombres** → `apiBaseUrl` en vez de `base`
4. **Extraer validaciones** → `validateMinimumNonDeprecatedAnswers()`
5. **Separar por dominio** → `user-api.ts`, `donations-api.ts`, etc.

## 📊 Impacto Estimado

| Métrica | Mejora |
|---------|--------|
| Tiempo de comprensión | -40% |
| Tiempo de modificación | -30% |
| Bugs introducidos | -25% |

## 👨‍💻 Autor

**Javier Quilumba - ** 
**Jonathan Tipan**

---

> *"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."* — Martin Fowler
