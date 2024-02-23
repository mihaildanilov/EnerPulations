# Use the official Node.js 14 image.
FROM node:20

# Create app directory
WORKDIR /app

# Install app dependencies by copying
# package.json and package-lock.json
COPY package*.json ./

RUN npm install

# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
COPY . .

# Build your TypeScript
RUN npm run build



EXPOSE 3008
CMD [ "npm", "start" ]
