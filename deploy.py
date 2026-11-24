from pathlib import Path


DEPLOYMENT_DIRECTORY = Path("deployment")


def deploy():
    DEPLOYMENT_DIRECTORY.mkdir(exist_ok=True)
    deployed_app = DEPLOYMENT_DIRECTORY / "app.py"
    deployed_app.write_text(
        Path("app.py").read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    print(f"Deployed application to {DEPLOYMENT_DIRECTORY.resolve()}")


if __name__ == "__main__":
    deploy()
