FROM node:20

WORKDIR /app

# install npm packages
COPY package*.json ./
RUN npm i

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--", "--host"]