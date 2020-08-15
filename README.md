
# CronJob to get SMS updates for Starlink satellites 🛰️

- [Docker image](https://hub.docker.com/repository/docker/joycelin79/python-starlink)
- [Kubernetes YAML](https://kubesail.com/template/loopDelicious/satellites)

# Get started 🌟

Create and activate your virtual environment

    python -m venv venv 
    source venv/bin/activate

Install your dependencies for Python 3

    pip install -r requirements.txt

Add your secrets in a new file called `.env` formatted like `.env.example`

Run the script locally

    python tracker.py

# Run in Docker

Build and run in Docker

    docker build --tag python-starlink .
    docker run --name starlink_test --env-file=.env --rm python-starlink 

Push your Docker image to Docker Hub

    docker tag python-starlink <Your Docker ID>/python-starlink:latest
    docker push <Your Docker ID>/python-starlink:latest

# Run in Kubernetes

Fork the KubeSail [`satellites`](https://kubesail.com/template/loopDelicious/satellites) YAML template

> [**satellites**](https://kubesail.com/template/loopDelicious/satellites) - CronJob to get SMS updates for Starlink satellites 🛰️

---

### Starlink Satellite positions

Using the [Skyfield](https://rhodesmill.org/skyfield/positions.html) Python library to determine [CelesTrak](http://celestrak.com/) Starlink Satellite proximity to a location.

### Dataset

https://celestrak.com/NORAD/elements/starlink.txt