# Base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Install Tesseract OCR
RUN apt-get update && apt-get install -y tesseract-ocr

# Create the uploads directory and update its permissions
RUN mkdir uploads && chown -R 1000:1000 /app/uploads

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the app files to the container
COPY app.py .

# Expose the port
EXPOSE 8501

# Set the entrypoint command
CMD ["streamlit", "run", "--server.enableCORS", "false", "--server.port", "8501", "app.py"]
