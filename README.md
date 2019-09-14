# SVS-TIFF Tiler

Builds [svs-tiff-tiler](https://hub.docker.com/r/gehlenborglab/ome-tiff-tiler) Docker image:
This image uses [libvips](https://jcupitt.github.io/libvips/) to convert
[OME-TIFF](http://paulbourke.net/dataformats/svs/) files to
[DeepZoom](https://en.wikipedia.org/wiki/Deep_Zoom) tiles for each image plane.

## Build

```bash
docker build --tag=svs-tiler context
```

## Run

```bash
docker run \
    -rm \
    -e "PREFIX=your_prefix" \
    --mount "type=bind,src=YOUR_FILE.tif,dst=/input.ome.tif" \
    --mount "type=bind,src=YOUR_OUTPUT,dst=/output_dir" \
    ome-tiff-tiler
```
(Or `gehlenborglab/ome-tiff-tiler:latest` to pull from DockerHub.)

Two environment variables should be set:
- `PREFIX`: Prefix to prepend to tile filenames.

And two mounts should be provided:
- Replace `YOUR_FILE.svs` with absolute path of the SVS to tile.
- Replace `YOUR_OUTPUT` with absolute path of directory where the tiles should go.

## Test and push to DockerHub

```bash
./test.sh
```

If tests pass, we're just pushing to DockerHub by hand:
```bash
# We should only push from master:
git checkout master
git pull

# First, set the new VERSION:
VERSION=v0.0.????
docker tag ome-tiff-tiler thomaslchan/svs-tiler:$VERSION
docker push thomaslchan/svs-tiler:$VERSION

# And also make a git tag:
git tag $VERSION
git push origin $VERSION
```
