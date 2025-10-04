#!/bin/sh
set -e

if [ ! -d ".next" ]; then
  echo "Build não encontrado, rodando npm run build..."
  npm run build
fi

echo "Iniciando servidor Next.js..."
exec npm start
