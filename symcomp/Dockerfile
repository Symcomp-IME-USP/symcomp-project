FROM node:lts-alpine3.22 AS builder
WORKDIR /app

COPY package.json pnpm-lock.yaml* ./
RUN npm install --frozen-lockfile

USER root

COPY . .
RUN npm build

FROM node:lts-alpine3.22 AS runner
WORKDIR /app
ENV NODE_ENV=production

COPY --from=builder /app/package.json ./
COPY --from=builder /app/.next ./.next
COPY --from=builder /app/public ./public
COPY --from=builder /app/node_modules ./node_modules

EXPOSE 3000

CMD ["npm", "start"]
