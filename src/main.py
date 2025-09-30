import os

from draw import AssetManager, Drawer
from fetch import fetch_github_contributions


def main():
    token = os.getenv("GITHUB_TOKEN")
    login = os.getenv("GITHUB_LOGIN")
    if token is None:
        raise ValueError("GITHUB_TOKEN environment variable is not set")
    data = fetch_github_contributions(token, login)

    assets = AssetManager("assets")
    drawer = Drawer(assets)
    image = drawer.draw(data)
    os.makedirs("output", exist_ok=True)
    image.save("output/contributions.png")


if __name__ == "__main__":
    main()
