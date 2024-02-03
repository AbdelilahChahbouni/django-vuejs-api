FROM node:14

WORKDIR /app

COPY ./online-courses/package*.json ./

RUN npm install

COPY ./online-courses .

CMD ["npm", "run", "serve"]