# Utilise l'image Python officielle
FROM python:3.13-slim

# Crée un dossier pour le bot
WORKDIR /app

# Copie les fichiers
COPY . .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Définit la commande de lancement du bot
CMD ["python", "detector.py"]
