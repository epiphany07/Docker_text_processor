# Use a lightweight Python base image
FROM python:3.9-alpine

# Set working directory
WORKDIR /home/data

# Copy the text files and script into the container
COPY scripts.py /home/data/scripts.py
COPY IF-1.txt /home/data/IF-1.txt
COPY AlwaysRememberUsThisWay-1.txt /home/data/AlwaysRememberUsThisWay-1.txt

# Run the script when the container starts
CMD ["python", "/home/data/scripts.py"]