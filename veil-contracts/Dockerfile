# Dockerfile
FROM node:16

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy the rest of the app's files
COPY . .

# Expose the Hardhat default port
EXPOSE 8545

# Run the Hardhat network in Docker
CMD ["npx", "hardhat", "node"]
