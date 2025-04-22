FROM ubuntu

WORKDIR /app

# Install Python and pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Check pip is installed
RUN pip3 --version

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]