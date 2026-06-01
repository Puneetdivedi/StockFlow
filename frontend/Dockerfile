# Use node:20-alpine as base image
FROM node:20-alpine AS build
WORKDIR /app

# Install dependencies
COPY package.json ./
RUN npm install

# Copy source code and build
COPY . ./
RUN npm run build

# Production image
FROM nginx:alpine
COPY --from=build /app/build /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
