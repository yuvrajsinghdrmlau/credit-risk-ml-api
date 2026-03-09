# Use official Python image
FROM python:3.11

# Set working directory inside container
WORKDIR /app

# Copy all project files
COPY . .

# Install required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]