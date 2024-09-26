## FRONTEND BUILDER ##
FROM node:20 AS builder
# Set up the React app directory
WORKDIR /app
# Copy package.json and package-lock.json
COPY frontend/package*.json ./
# Install dependencies
RUN npm install
# Copy the rest of the React app source code
COPY frontend/ .
# Build the React app
RUN npm run build


## FINAL ##
FROM python:3.12

# Create a directory for our Django project
WORKDIR /app

COPY api/requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the project files
COPY api/certs/ /etc/ssl/certs/
COPY api/ .

# Copy the Reat static project files
COPY --from=builder /app/build/static /app/static
COPY --from=builder /app/build/index.html /app/templates/index.html

# Set the environment variable for the Django project
ENV PYTHONUNBUFFERED=1
# Make port 80 available to the world outside this container
EXPOSE 80

# Set environment variables for Flask
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:80", "--certfile=/etc/ssl/certs/cert.pem", "--keyfile=/etc/ssl/certs/key.pem", "app:app"]
