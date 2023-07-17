FROM node:18.9.0-alpine 

WORKDIR /usr/src/app

RUN apk add make g++ py3-pip

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

EXPOSE 8000

CMD [ "npm", "run", "start" ]
