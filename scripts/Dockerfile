# Simple Fedora based Docker container for running Boxes.py

# Note that it downloads Boxes.py from GitHub and does not use your local copy
# of the repository. Adjust the git command below to get it from somewhere else

# Build with
#  docker build -t boxes.py .
# Run with
#  docker run -ti -p 4000:8000 boxes.py
# to get the web interface at localhost:4000
# First access may take a while as the Python files need to be complied

# Use latest Fedora release as base
FROM fedora:latest

# fix from https://medium.com/nttlabs/ubuntu-21-10-and-fedora-35-do-not-work-on-docker-20-10-9-1cd439d9921
ADD https://github.com/AkihiroSuda/clone3-workaround/releases/download/v1.0.0/clone3-workaround.x86_64 /clone3-workaround
RUN chmod 755 /clone3-workaround
SHELL ["/clone3-workaround", "/bin/sh", "-c"]

# Install requirements
RUN dnf install -y git-core python3-markdown python3-setuptools python3-affine pstoedit && dnf clean all

# Get Boxes.py sources to /boxes
RUN git clone --depth 1 -b master https://github.com/jiskar/boxes.git

# Internal port used
EXPOSE 8000

# Start the boxes web server on container start up
CMD ["/boxes/scripts/boxesserver"]
