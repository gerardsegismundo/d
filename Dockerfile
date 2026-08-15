# Use official Python runtime as base image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy the task manager script and data file
COPY task_cli.py .
COPY tasks.json .``



# Run the task manager CLI
CMD ["python", "task_cli.py"]

