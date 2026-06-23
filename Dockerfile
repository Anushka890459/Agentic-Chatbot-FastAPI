FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Make the start script executable
RUN chmod +x start.sh

# Expose Streamlit's port
EXPOSE 8501

# Execute the start script to boot both backend and frontend
CMD ["./start.sh"]