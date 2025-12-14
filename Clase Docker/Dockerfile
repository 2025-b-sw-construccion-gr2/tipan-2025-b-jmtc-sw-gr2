# 1. Usa una imagen base con Node.js
FROM node:22.19.0

# 2. Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3. Copia los archivos necesarios
COPY package*.json ./

# 4. Instala las dependencias
RUN npm install --production

# 5. Copia el resto del código
COPY . .

# 6. Compila el proyecto NestJS
RUN npm run build

# 7. Expone el puerto en el que corre tu app (por defecto 3000)
EXPOSE 3000

# 8. Comando para iniciar la app
CMD ["node", "dist/main"]