FROM node:20.11.1-alpine3.18 as builder

WORKDIR /app

COPY package*.json ./
ARG api_url

ENV NEXT_PUBLIC_API_URL=${api_url}

RUN npm install 

COPY . .

RUN npm run build

CMD [ "npm","start" ]
