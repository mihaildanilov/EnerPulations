FROM node:20

WORKDIR /app

ARG FRONTEND_URL

COPY package*.json ./

ENV FRONTEND_URL ${FRONTEND_URL}

RUN npm install

COPY . .

RUN npm run build



EXPOSE 3008
CMD [ "npm", "start" ]
