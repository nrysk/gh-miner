import argparse
import os

from draw import AssetManager, Drawer
from fetch import fetch_github_contributions

GITHUB_OUTPUT_KEY = "GITHUB_OUTPUT"


def main():
    # Fetch contribution data
    token = os.getenv("INPUT_GITHUB_TOKEN")
    login = os.getenv("INPUT_GITHUB_LOGIN")
    if token is None:
        raise ValueError("INPUT_GITHUB_TOKEN environment variable is not set")
    if login is None:
        raise ValueError("INPUT_GITHUB_LOGIN environment variable is not set")
    data = fetch_github_contributions(token, login)

    # Draw image
    assets = AssetManager(args.assets)
    drawer = Drawer(assets)
    image = drawer.draw(data)
    os.makedirs("output", exist_ok=True)
    image.save("output/contributions.png")

    # Set output for GitHub Actions
    if GITHUB_OUTPUT_KEY in os.environ:
        with open(os.environ[GITHUB_OUTPUT_KEY], "a") as f:
            f.write("output_dir=output\n")


if __name__ == "__main__":
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Fetch GitHub contributions and draw an image."
    )
    parser.add_argument(
        "-a",
        "--assets",
        type=str,
        default="assets",
        help="Path to the assets directory",
    )
    args = parser.parse_args()

    main()
