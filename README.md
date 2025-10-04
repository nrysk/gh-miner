

_If you like this project, please give it a star ⭐️_

# GH Miner
A GitHub contributions visualizer with Minecraft theme.

![example](https://raw.githubusercontent.com/nrysk/gh-miner/refs/heads/main/img/example.png)

## Quick Start


This example GitHub workflow generates the PNG image and pushes them to your repository.
Please create a file at `.github/workflows/gh-miner.yml` in your repository and paste the following code.

Note: Replace `<YOUR_GITHUB_LOGIN>` with your GitHub username.

```yaml
name: GH Miner

on:
  push:
    branches:
      - main

permissions:
  contents: write

jobs:
  generate-and-push:
    runs-on: ubuntu-latest
    steps:
      - name: Generate Picture
        id: generate
        uses: nrysk/gh-miner@v1.0.0
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          github_login: <YOUR_GITHUB_LOGIN>

      - name: Push Picture
        uses: crazy-max/ghaction-github-pages@v4
        with:
          target_branch: gh-miner
          build_dir: ${{ steps.generate.outputs.output_dir }}
          commit_message: "Generate contribution image"
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

You can see the generated image at `https://github.com/<YOUR_GITHUB_LOGIN>/<YOUR_REPOSITORY>/blob/gh-miner/contributions.png?raw=true`.

## Contribution

Feel free to open issues and pull requests.