# Use official Python 3.11.4 slim image as the base
FROM python:3.11.4-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements.txt to install dependencies
COPY requirements.txt .

# Install system dependencies and Python packages
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --no-cache-dir -r requirements.txt

# Copy the app and model files
COPY app.py .
COPY student_performance_model_tuned.joblib .

# Expose the port Streamlit runs on
EXPOSE 8501

# Set environment variables for Streamlit
ENV PYTHONUNBUFFERED=1

# Command to run the Streamlit app
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
