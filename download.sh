
IMAGE_DIR="./assets/images"
FONT_DIR="./assets/fonts"

mkdir -p $IMAGE_DIR
mkdir -p $FONT_DIR

# Download Minecraft block textures from the Minecraft Wiki (Blocks)
curl -s -L -o $IMAGE_DIR/cobblestone.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/a7/Cobblestone_%28texture%29_JE5_BE3.png/revision/latest?cb=20201001121005'
curl -s -L -o $IMAGE_DIR/stone.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/dc/Stone_%28texture%29_JE5_BE3.png/revision/latest?cb=20201001141805'
curl -s -L -o $IMAGE_DIR/coal_ore.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/a2/Coal_Ore_%28texture%29_JE5_BE4.png/revision/latest?cb=20210312150038'
curl -s -L -o $IMAGE_DIR/iron_ore.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/5a/Iron_Ore_%28texture%29_JE6_BE4.png/revision/latest?cb=20210312150124'
curl -s -L -o $IMAGE_DIR/gold_ore.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/52/Gold_Ore_%28texture%29_JE7_BE4.png/revision/latest?cb=20210415103228'
curl -s -L -o $IMAGE_DIR/diamond_ore.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/c0/Diamond_Ore_%28texture%29_JE5_BE5.png/revision/latest?cb=20210312150111'
curl -s -L -o $IMAGE_DIR/grass_block.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/3/3b/Grass_Block_%28side_texture%29_JE2_BE2.png/revision/latest?cb=20200921204925'
curl -s -L -o $IMAGE_DIR/snowy_grass_block.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/29/Snowy_Grass_Block_%28side_texture%29_JE3_BE3.png/revision/latest?cb=20210327144849'
curl -s -L -o $IMAGE_DIR/dirt.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/3/3d/Dirt_%28texture%29_JE2_BE2.png/revision/latest?cb=20200919012354'
curl -s -L -o $IMAGE_DIR/bedrock.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/0/08/Bedrock_%28texture%29_JE2_BE2.png/revision/latest?cb=20201001115713'

# Download Minecraft pickaxe textures from the Minecraft Wiki (Items)
curl -s -L -o $IMAGE_DIR/wooden_pickaxe.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/0/0b/Wooden_Pickaxe_JE2_BE2.png/revision/latest?cb=20200217231203'
curl -s -L -o $IMAGE_DIR/stone_pickaxe.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/c4/Stone_Pickaxe_JE2_BE2.png/revision/latest?cb=20200217234007'
curl -s -L -o $IMAGE_DIR/iron_pickaxe.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/d1/Iron_Pickaxe_JE3_BE2.png/revision/latest?cb=20200105053011'
curl -s -L -o $IMAGE_DIR/golden_pickaxe.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/a6/Golden_Pickaxe_JE4_BE3.png/revision/latest?cb=20200226194041'
curl -s -L -o $IMAGE_DIR/diamond_pickaxe.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/e/e7/Diamond_Pickaxe_JE3_BE3.png/revision/latest/scale-to-width-down/48?cb=20250628224016'
curl -s -L -o $IMAGE_DIR/netherite_pickaxe.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/d4/Netherite_Pickaxe_JE3.png/revision/latest/scale-to-width-down/48?cb=20210418192807'

# Download Minecraft font 
curl -s -L -o $FONT_DIR/minecrafter.zip 'https://dl.dafont.com/dl/?f=minecrafter'
curl -s -L -o $FONT_DIR/minecraftia.zip 'https://dl.dafont.com/dl/?f=minecraftia'
unzip -o -q $FONT_DIR/minecrafter.zip -d $FONT_DIR/
unzip -o -q $FONT_DIR/minecraftia.zip -d $FONT_DIR/
rm $FONT_DIR/*.zip