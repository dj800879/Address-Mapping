# Base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy all other files
COPY . .

# Build app
RUN npm run build

# Start the frontend (uses preview server)
EXPOSE 5173
CMD ["npm", "run", "preview", "--", "--host"]