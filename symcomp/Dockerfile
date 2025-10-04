# Imagem base
FROM node:lts-alpine3.22

WORKDIR /app

COPY package.json pnpm-lock.yaml* ./

RUN npm install -g pnpm

RUN pnpm install --frozen-lockfile

COPY . .

EXPOSE 3000

RUN pnpm build

CMD ["pnpm", "start"]
