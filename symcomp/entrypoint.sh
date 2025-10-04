#!/bin/sh
set -e

# Garante que o build existe
if [ ! -d ".next" ]; then
  echo "Build não encontrado, rodando npm run build..."
  npm run build
fi

echo "Iniciando servidor Next.js..."
exec npm start
