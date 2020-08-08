# creates a layer from the python:3 Docker image
FROM python:3

# copy and install dependencies
COPY requirements.txt /
RUN pip install -r requirements.txt

# add script and environment file
COPY tracker.py /

# define the command to run the script
CMD [ "python", "./tracker.py" ]