# Taller - Clase 006 Análisis de Código Limpio

## Aplicando Principios de Clean Code en freeCodeCamp

---
**Integrantes:** Javier Quilumba y Jonathan Tipan

## 🎯 Objetivo

Analizar código real de repositorios públicos para identificar violaciones a principios de código limpio y proponer refactorizaciones que mejoren la mantenibilidad y escalabilidad.



---

## Introducción
Para la actividad práctica, formamos grupos de 2-3 estudiantes y seleccionamos un repositorio público de GitHub/GitLab para analizar. La lista de repositorios sugeridos incluía proyectos en diferentes lenguajes como Python, JavaScript, Java, C++, Go, Rust, PHP, entre otros.

---

| Campo | Detalle |
|-------|---------|
| **Tema** | Aplicando Principios de Código Limpio en Proyectos Reales |
| **Repositorio analizado** | [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) |
| **Directorio base** | `Main` |
| **Descripción** | plataforma educativa de código abierto que ofrece un curriculum completo y gratuito para aprender desarrollo web, ciencia de datos y machine learning. El repositorio contiene tanto el código base de la plataforma como todo el curriculum educativo.
 |
| **Justificación** | Elegimos este repositorio porque es uno de los proyectos de código abierto más grandes y activos en el ámbito educativo, con más de 400,000 estrellas en GitHub. Contiene código real utilizado por millones de usuarios alrededor del mundo. Además, al ser una plataforma educativa, tiene una estructura de código interesante que combina lógica de aplicación, contenido curricular y herramientas de aprendizaje. |

---

## 📂 Archivos Analizados

| Archivo | Ruta | Propósito | LOC |
|---------|------|-----------|-----|
| `ajax.ts` | `/client/src/utils/ajax.ts` | Gestión de comunicación HTTP con la API | ~400 |
| `exam-schemas.ts` | `/api/src/utils/exam-schemas.ts` | Esquemas de validación Joi para exámenes | ~200 |

---

## 🔎 Análisis Detallado

### 📄 Archivo 1: `ajax.ts`

#### ✅ Aspectos Positivos
- Nombres descriptivos siguiendo convenciones RESTful
- TypeScript para type safety
- Documentación JSDoc en funciones clave
- Manejo consistente de respuestas HTTP

#### ⚠️ Problemas Identificados

**1. Violación del Principio de Responsabilidad Única (SRP)**

El archivo maneja múltiples dominios sin separación:

| Dominio | Funciones |
|---------|-----------|
| Usuarios | `getSessionUser`, `getUserProfile`, `putUpdateMyAbout` |
| Donaciones | `addDonation`, `postChargeStripe` |
| Exámenes | `getGenerateExam`, `getExamAttempts` |
| Certificados | `getShowCert`, `putVerifyCert` |

**2. Strings Mágicos (30+ ocurrencias)**

```typescript
// ❌ Endpoints hardcodeados
export function getSessionUser(signal?: AbortSignal) {
  return get('/user/get-session-user', signal);
}

export function postChargeStripe(body: Donation) {
  return post('/donate/charge-stripe', body);
}
```

**3. Nombres Poco Descriptivos**

```typescript
// ❌ Problema
const base = apiLocation;

// ✅ Mejor
const apiBaseUrl = apiLocation;
```

**4. Deuda Técnica Documentada (4+ TODOs)**

```typescript
// TODO: Might want to handle flash messages as close to the request as possible
// TODO: Once DB is migrated, no longer need to parse 'files' -> 'challengeFiles'
```

---

### 📄 Archivo 2: `exam-schemas.ts`

#### ✅ Aspectos Positivos
- Naming consistente con sufijo `Joi`
- Documentación JSDoc clara
- Validaciones robustas con mensajes personalizados

#### ⚠️ Problemas Identificados

**1. Duplicación Masiva de Código (3 veces)**

```typescript
// ❌ Repetido en wrongAnswers, correctAnswers y numberOfQuestionsInExam
const nonDeprecatedCount = value.reduce(
  (count: number, answer: Answer) =>
    answer.deprecated ? count : count + 1,
  0
);
```

**2. Números Mágicos (5+ ocurrencias)**

```typescript
// ❌ Sin contexto
const minimumAnswers = 4;  // ¿Por qué 4?
answers: Joi.array().items(GeneratedAnswerJoi).min(5).required()  // ¿Por qué 5?
```

**3. Abreviaciones Confusas**

```typescript
// ❌ "RE" no es estándar
const nanoIdRE = new RegExp('[a-z0-9]{10}');
const objectIdRE = new RegExp('^[0-9a-fA-F]{24}$');
```

**4. Lógica de Negocio en Validaciones**

```typescript
// ❌ Lógica compleja dentro de esquemas Joi
wrongAnswers: Joi.array()
  .custom((value: Answer[], helpers) => {
    // 10+ líneas de lógica aquí
    const nonDeprecatedCount = value.reduce(...);
    if (nonDeprecatedCount < minimumAnswers) {
      return helpers.message({...});
    }
    return value;
  })
```

---

## 💡 Mejoras Propuestas

### Mejora #1: Extraer Lógica Duplicada

**Principio:** DRY  
**Prioridad:** Alta  
**Archivo:** `exam-schemas.ts`

```typescript
// ✅ Función reutilizable
const countNonDeprecatedItems = <T extends { deprecated?: boolean | null }>(
  items: T[]
): number => {
  return items.reduce(
    (count, item) => (item.deprecated ? count : count + 1),
    0
  );
};

// Uso
const nonDeprecatedCount = countNonDeprecatedItems(value);
```

**Impacto:** Elimina 15 líneas duplicadas y centraliza cambios futuros.

---

### Mejora #2: Constantes para Números Mágicos

**Principio:** Nombres Significativos  
**Prioridad:** Media  
**Archivo:** `exam-schemas.ts`

```typescript
const MINIMUM_WRONG_ANSWERS = 4;
const MINIMUM_CORRECT_ANSWERS = 1;
const MINIMUM_TOTAL_ANSWERS_PER_QUESTION = 5;
const MAXIMUM_PERCENTAGE = 100;

// Uso
wrongAnswers: Joi.array()
  .items(DbAnswerJoi)
  .custom((value: Answer[], helpers) => {
    const count = countNonDeprecatedItems(value);
    if (count < MINIMUM_WRONG_ANSWERS) {
      return helpers.message({
        en: `'wrongAnswers' must have at least ${MINIMUM_WRONG_ANSWERS} non-deprecated answers.`
      });
    }
    return value;
  })
```

---

### Mejora #3: Nombres Descriptivos

**Principio:** Nombres Reveladores de Intención  
**Prioridad:** Media

```typescript
// ajax.ts
const apiBaseUrl = apiLocation;  // Antes: base

// exam-schemas.ts
const NANO_ID_PATTERN = /[a-z0-9]{10}/;  // Antes: nanoIdRE
const MONGODB_OBJECTID_PATTERN = /^[0-9a-fA-F]{24}$/;  // Antes: objectIdRE
```

---

### Mejora #4: Extraer Validaciones Custom

**Principio:** Funciones que Hacen Una Cosa  
**Prioridad:** Media  
**Archivo:** `exam-schemas.ts`

```typescript
const validateMinimumNonDeprecatedAnswers = (
  answers: Answer[],
  minimum: number,
  fieldName: string,
  helpers: Joi.CustomHelpers
) => {
  const count = countNonDeprecatedItems(answers);
  
  if (count < minimum) {
    return helpers.message({
      en: `'${fieldName}' must have at least ${minimum} non-deprecated answers.`
    });
  }
  return answers;
};

// Uso simplificado
wrongAnswers: Joi.array()
  .items(DbAnswerJoi)
  .required()
  .custom((value, helpers) =>
    validateMinimumNonDeprecatedAnswers(
      value,
      MINIMUM_WRONG_ANSWERS,
      'wrongAnswers',
      helpers
    )
  )
```

---

### Mejora #5: Separar Responsabilidades

**Principio:** Single Responsibility Principle  
**Prioridad:** Alta  
**Archivo:** `ajax.ts`

**Estructura propuesta:**

```
utils/api/
├── api-endpoints.ts      // Constantes de rutas
├── api-base.ts           // GET, POST, PUT, DELETE
├── user-api.ts           // APIs de usuarios
├── donations-api.ts      // APIs de donaciones
├── exams-api.ts          // APIs de exámenes
└── certificates-api.ts   // APIs de certificados
```

**Ejemplo de implementación:**

```typescript
// api-endpoints.ts
export const API_ENDPOINTS = {
  USER: {
    SESSION: '/user/get-session-user',
    PROFILE: '/user/profile',
  },
  DONATIONS: {
    CHARGE: '/donate/charge-stripe',
  },
  EXAMS: {
    GENERATE: (id: string) => `/exam/${id}`,
  }
};

// user-api.ts
import { get, post } from './api-base';
import { API_ENDPOINTS } from './api-endpoints';

export function getSessionUser(signal?: AbortSignal) {
  return get(API_ENDPOINTS.USER.SESSION, signal);
}
```
### Hallazgos Principales

**Crítico:**
- Duplicación de código que aumenta deuda técnica
- Archivos monolíticos que violan SRP

**Importante:**
- Números mágicos sin contexto
- Strings hardcodeados dificultan mantenimiento
- Lógica de negocio mezclada con validaciones

---

## 💭 Conclusiones

- Analizar un proyecto real como freeCodeCamp permitió comprender cómo se aplican los principios de código limpio en sistemas de gran escala.

- Se identificó la importancia de mantener consistencia, modularidad y claridad para facilitar el trabajo colaborativo en proyectos con múltiples contribuidores.

- Este ejercicio reforzó la idea de que el código limpio no es solo un estándar técnico, sino una práctica fundamental para asegurar la calidad y sostenibilidad del software.



### Lecciones Aprendidas

1. **El código funcional no es necesariamente código limpio** - El código analizado sirve a millones de usuarios pero tiene áreas de mejora.

2. **La deuda técnica es inevitable** - Los TODOs indican que incluso proyectos bien mantenidos acumulan deuda técnica.

3. **Los principios son universales** - DRY, SRP y nombres significativos aplican a cualquier proyecto.

4. **La refactorización es continua** - El código requiere mantenimiento constante para mantener calidad.



### Reflexión Final

Analizar freeCodeCamp enseña que incluso proyectos exitosos tienen áreas de mejora. La diferencia entre un proyecto mediocre y uno excelente no está en escribir código perfecto desde el inicio, sino en la capacidad de identificar problemas y realizar mejoras continuas.

Como futuros ingenieros, debemos:
- Escribir código que nuestro "yo futuro" agradezca
- Pensar en el próximo desarrollador que lo leerá
- Valorar la legibilidad tanto como la funcionalidad
- Refactorizar antes de que se convierta en deuda técnica

> *"Any fool can write code that a computer can understand. Good programmers write code that humans can understand."* — Martin Fowler

---


## Referencias

[1] Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall.  

[2] GitHub. (2024). *GitHub Documentation - Exploring repositories*. [https://docs.github.com/](https://docs.github.com/)  

[3] Hostinger, 03 Sep 2025. *"Los 15 mejores repositorios GitHub que todo desarrollador debería conocer,"* [https://www.hostinger.com/es/tutoriales/mejores-repositorios-github](https://www.hostinger.com/es/tutoriales/mejores-repositorios-github)  

[4] freeCodeCamp.org, *"freeCodeCamp: The freeCodeCamp codebase and curriculum,"* GitHub. [https://github.com/freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp)  

[5] freeCodeCamp.org, *"devdocs: freeCodeCamp Developer Documentation,"* GitHub. [https://github.com/freeCodeCamp/devdocs](https://github.com/freeCodeCamp/devdocs)  




