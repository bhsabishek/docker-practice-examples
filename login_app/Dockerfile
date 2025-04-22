FROM ubuntu

WORKDIR . /app

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Check pip is installed
RUN pip3 --version

EXPOSE 5000

CMD ["python3", "app.py"]