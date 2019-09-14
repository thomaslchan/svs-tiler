FROM python:3.6-slim

# Always run `apt-get update` and `apt-get install` together.
# https://docs.docker.com/develop/develop-images/dockerfile_best-practices/

RUN apt-get update && apt-get install -y \
  libvips
RUN pip install \
  pyvips==2.1.8

COPY svs_tiler.py .

CMD python svs_tiler.py \
    --svs_file /input.svs \
    --output_directory /output_dir \
    --prefix $PREFIX
