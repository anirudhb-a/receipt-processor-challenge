# Use whichever Python base image you prefer
FROM python:3.9-slim
 
# Create a working directory
WORKDIR /app
 
# Copy only the requirements file first to leverage Docker layer caching
COPY requirements.txt .
 
# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
 
# Copy in the rest of your code
COPY . .
 
# Expose the port Flask will run on
EXPOSE 5000
 
# Start the app using your main script
CMD ["python", "main.py"]