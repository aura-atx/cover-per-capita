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
