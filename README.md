# creg_ML_cheminf_flask_app
Developement/deployment stack for running cheminformatics ML model in Flask webapp

# Development environment
Build a docker image to enter containerized environment that mimics the production environment with these commands in the root directory of the repo:
```bash
cd Development/
docker build -t docker_image_name .
```
To enter the container and use the Jupyter notebooks or develop/modify modules:
```bash
docker run --rm -it docker_image_name
```
