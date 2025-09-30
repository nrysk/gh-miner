import os

from PIL import Image, ImageDraw, ImageFilter, ImageFont

from fetch import ContributionData

BLOCK_SIZE = 16


class AssetManager:
    def __init__(self, asset_dir: str):
        self.asset_dir = asset_dir

        # images (blocks)
        self.grass_block_image = self._load_image("grass_block.png")
        self.dirt_image = self._load_image("dirt.png")
        self.cobblestone_image = self._load_image("cobblestone.png")
        self.stone_image = self._load_image("stone.png")
        self.coal_ore_image = self._load_image("coal_ore.png")
        self.iron_ore_image = self._load_image("iron_ore.png")
        self.gold_ore_image = self._load_image("gold_ore.png")
        self.diamond_ore_image = self._load_image("diamond_ore.png")

        # images (items)
        self.wooden_pickaxe_image = self._load_image("wooden_pickaxe.png")
        self.stone_pickaxe_image = self._load_image("stone_pickaxe.png")
        self.iron_pickaxe_image = self._load_image("iron_pickaxe.png")
        self.golden_pickaxe_image = self._load_image("golden_pickaxe.png")
        self.diamond_pickaxe_image = self._load_image("diamond_pickaxe.png")
        self.netherite_pickaxe_image = self._load_image("netherite_pickaxe.png")

        # fonts
        self.minecrafter_font_16 = self._load_font("Minecrafter.Reg.ttf", 16)
        self.minecraftia_font_8 = self._load_font("Minecraftia-Regular.ttf", 8)
        self.minecraftia_font_16 = self._load_font("Minecraftia-Regular.ttf", 16)

    def _load_image(self, filename: str) -> Image.Image:
        return Image.open(
            os.path.join(self.asset_dir, "images", filename),
        ).resize((BLOCK_SIZE, BLOCK_SIZE))

    def _load_font(self, filename: str, size: int) -> ImageFont.FreeTypeFont:
        return ImageFont.truetype(os.path.join(self.asset_dir, "fonts", filename), size)

    def get_image_by_level(self, level: str) -> Image.Image:
        return {
            None: self.cobblestone_image,
            "NONE": self.stone_image,
            "FIRST_QUARTILE": self.coal_ore_image,
            "SECOND_QUARTILE": self.iron_ore_image,
            "THIRD_QUARTILE": self.gold_ore_image,
            "FOURTH_QUARTILE": self.diamond_ore_image,
        }[level]


class Drawer:
    def __init__(self, asset_manager: AssetManager):
        self.asset_manager = asset_manager

    def draw(self, data: ContributionData) -> Image.Image:
        background = self.draw_background()
        contribution_grid = self.draw_contribution_grid(data)
        combined = Image.new("RGBA", background.size, (255, 255, 255, 0))
        combined.paste(background, (0, 0))
        combined.paste(contribution_grid, (BLOCK_SIZE, BLOCK_SIZE), contribution_grid)
        text = self.draw_text(f"{data.total_contributions} contributions")
        combined.paste(text, (BLOCK_SIZE * 1, int(BLOCK_SIZE * 0.2)), text)
        text = self.draw_textured_text("GH MINER", self.asset_manager.grass_block_image)
        combined.paste(
            text,
            (BLOCK_SIZE * 54 - text.width, int(BLOCK_SIZE * 8.2)),
            text,
        )

        return combined

    def draw_contribution_grid(self, data: ContributionData) -> Image.Image:
        image = Image.new(
            "RGBA", (BLOCK_SIZE * data.total_weeks, BLOCK_SIZE * 7), (255, 255, 255, 0)
        )

        for i_col in range(53):
            for i_row in range(7):
                try:
                    level = data.level_matrix[i_col][i_row]
                except IndexError:
                    level = None
                image.paste(
                    self.asset_manager.get_image_by_level(level),
                    (i_col * BLOCK_SIZE, i_row * BLOCK_SIZE),
                )

        return image

    def draw_background(self) -> Image.Image:
        image = Image.new("RGBA", (BLOCK_SIZE * 55, BLOCK_SIZE * 9), (255, 255, 255, 0))

        for i in range(55):
            image.paste(self.asset_manager.grass_block_image, (i * BLOCK_SIZE, 0))
            for j in range(1, 9):
                image.paste(
                    self.asset_manager.dirt_image, (i * BLOCK_SIZE, j * BLOCK_SIZE)
                )

        mask = Image.new("L", image.size, 128)
        draw = ImageDraw.Draw(mask)
        for y in range(BLOCK_SIZE - 2):
            alpha = int(128 * (y / BLOCK_SIZE))
            draw.line([(0, y), (image.width, y)], fill=alpha)

        shadow_layer = Image.new("RGBA", image.size, (0, 0, 0, 255))
        image.paste(shadow_layer, (0, 0), mask)

        return image

    def draw_text(self, text: str) -> Image.Image:
        font = self.asset_manager.minecraftia_font_8
        text_size = font.getbbox(text)[2:]
        image = Image.new("RGBA", text_size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), text, font=font, fill=(255, 255, 255, 255))
        return image

    def draw_textured_text(self, text: str, texture: Image.Image) -> Image.Image:
        font = self.asset_manager.minecrafter_font_16
        text_size = font.getbbox(text)[2:]
        text_mask = Image.new("L", text_size, 0)
        draw = ImageDraw.Draw(text_mask)
        draw.text((0, 0), text, font=font, fill=255)

        tiled_texture = Image.new("RGBA", text_size)
        for x in range(0, text_size[0], texture.width):
            for y in range(0, text_size[1], texture.height):
                tiled_texture.paste(texture, (x, y))

        image = Image.new("RGBA", text_size, (0, 0, 0, 0))
        image.paste(tiled_texture, (0, 0), text_mask)

        return image
