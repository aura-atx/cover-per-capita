import http.client
from pathlib import Path
from urllib.parse import urljoin
import zipfile

from invoke import task
import nox


@task(default=True)
def setup(c):
    """Setup the developper environment."""
    c.run(f"nox -f {__name__}.py --envdir .")


@nox.session()
def venv(session):
    """Setup the developper environment."""
    # Install dependencies.
    session.install("--upgrade", "pip", "setuptools")
    session.install("-r", "requirements.txt")
    session.install("-r", "requirements-dev.txt")


@task
def prepare(c):
    """Prepare input datasets."""
    HOTOSM_HOST = "export.hotosm.org"
    HOTOSM_PATH = "/downloads/8a430b3a-7b16-4c88-9b36-7da085b4d141/"
    ZIP_FILE = "austin-tx_shp.zip"
    SAMPLE_DIR = "sample/input_datasets"
    OUTPUT_DIR = "osm-austin"
    CHUNK_SIZE = 8192

    # Create the directory.
    p = Path(SAMPLE_DIR)
    p.mkdir(parents=True, exist_ok=True)

    # Download the assets.
    conn = http.client.HTTPSConnection(HOTOSM_HOST)
    conn.request("GET", f"{HOTOSM_PATH}/{ZIP_FILE}")
    try:
        r = conn.getresponse()
        size = 0
        with open(p / ZIP_FILE, "wb") as f:
            while not r.closed:
                chunk = r.read(CHUNK_SIZE)
                f.write(chunk)
                size += len(chunk)

                # Sometime the stream never ends.
                if size >= int(r.headers.get("Content-Length", 0)):
                    break
    finally:
        conn.close()

    # Extract them.
    with zipfile.ZipFile(p / ZIP_FILE) as z:
        z.extractall(p / OUTPUT_DIR)

