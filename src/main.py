import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

from fetch import fetch_github_contributions

BLOCK_SIZE = 16

LEVEL_TO_IMAGE = {
    "NONE": Image.open("assets/stone.png").resize((BLOCK_SIZE, BLOCK_SIZE)),
    "FIRST_QUARTILE": Image.open("assets/coal_ore.png").resize(
        (BLOCK_SIZE, BLOCK_SIZE)
    ),
    "SECOND_QUARTILE": Image.open("assets/iron_ore.png").resize(
        (BLOCK_SIZE, BLOCK_SIZE)
    ),
    "THIRD_QUARTILE": Image.open("assets/gold_ore.png").resize(
        (BLOCK_SIZE, BLOCK_SIZE)
    ),
    "FOURTH_QUARTILE": Image.open("assets/diamond_ore.png").resize(
        (BLOCK_SIZE, BLOCK_SIZE)
    ),
}

GRASS_BLOCK_IMAGE = Image.open("assets/grass_block.png").resize(
    (BLOCK_SIZE, BLOCK_SIZE)
)
DIRT_IMAGE = Image.open("assets/dirt.png").resize((BLOCK_SIZE, BLOCK_SIZE))
STONE_IMAGE = Image.open("assets/stone.png").resize((BLOCK_SIZE, BLOCK_SIZE))

FONT_FILE = "assets/Minecrafter.Reg.ttf"
FONT = ImageFont.truetype(FONT_FILE, 16)


def main():
    token = os.getenv("GITHUB_TOKEN")
    data = fetch_github_contributions(token)

    text_mask = Image.new("RGBA", (BLOCK_SIZE * 55, BLOCK_SIZE * 9), (255, 255, 255, 0))
    draw = ImageDraw.Draw(text_mask)
    draw.text(
        (0, 0),
        "GitHub Contributions",
        font=FONT,
        fill=(255, 255, 255, 255),
    )
    tiled_stone_image = Image.new("RGBA", text_mask.size)
    stone_w, stone_h = STONE_IMAGE.size
    for i in range(0, text_mask.size[0], stone_w):
        for j in range(0, text_mask.size[1], stone_h):
            tiled_stone_image.paste(STONE_IMAGE, (i, j))

    main_image = create_main_image(data)
    base_image = create_base_image()
    base_image.paste(main_image, (BLOCK_SIZE * 1, BLOCK_SIZE * 1), main_image)
    base_image.paste(tiled_stone_image, (0, 0), text_mask)
    os.makedirs("output", exist_ok=True)
    base_image.save("output/contributions.png")


def create_main_image(data) -> Image.Image:
    main_image = Image.new(
        "RGBA", (BLOCK_SIZE * data.total_weeks, BLOCK_SIZE * 7), (255, 255, 255, 0)
    )

    for i_col, week in enumerate(data.level_matrix):
        for i_row, level in enumerate(week):
            image = LEVEL_TO_IMAGE[level]
            main_image.paste(image, (i_col * BLOCK_SIZE, i_row * BLOCK_SIZE))

    return main_image


def create_base_image() -> Image.Image:
    base_image = Image.new(
        "RGBA", (BLOCK_SIZE * 55, BLOCK_SIZE * 9), (255, 255, 255, 0)
    )
    for i in range(55):
        base_image.paste(GRASS_BLOCK_IMAGE, (i * BLOCK_SIZE, 0))
        for j in range(1, 10):
            base_image.paste(DIRT_IMAGE, (i * BLOCK_SIZE, j * BLOCK_SIZE))

    shadow_layer = Image.new("RGBA", base_image.size, (0, 0, 0, 100))
    base_image.paste(shadow_layer, (0, 0), shadow_layer)

    return base_image


if __name__ == "__main__":
    main()
