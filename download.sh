
mkdir assets

# Download Minecraft block textures from the Minecraft Wiki
curl -s -L -o assets/stone.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/dc/Stone_%28texture%29_JE5_BE3.png/revision/latest?cb=20201001141805'
curl -s -L -o assets/coal_ore.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/a2/Coal_Ore_%28texture%29_JE5_BE4.png/revision/latest?cb=20210312150038'
curl -s -L -o assets/iron_ore.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/5a/Iron_Ore_%28texture%29_JE6_BE4.png/revision/latest?cb=20210312150124'
curl -s -L -o assets/gold_ore.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/52/Gold_Ore_%28texture%29_JE7_BE4.png/revision/latest?cb=20210415103228'
curl -s -L -o assets/diamond_ore.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/c0/Diamond_Ore_%28texture%29_JE5_BE5.png/revision/latest?cb=20210312150111'
curl -s -L -o assets/grass_block.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/3/3b/Grass_Block_%28side_texture%29_JE2_BE2.png/revision/latest?cb=20200921204925'
curl -s -L -o assets/snowy_grass_block.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/2/29/Snowy_Grass_Block_%28side_texture%29_JE3_BE3.png/revision/latest?cb=20210327144849'
curl -s -L -o assets/dirt.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/3/3d/Dirt_%28texture%29_JE2_BE2.png/revision/latest?cb=20200919012354'
curl -s -L -o assets/wooden_pickaxe.png 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/0/0b/Wooden_Pickaxe_JE2_BE2.png/revision/latest?cb=20200217231203'
# curl -s -L -o assets/
# curl -s -L -o assets/
# curl -s -L -o assets/
# curl -s -L -o assets/
# curl -s -L -o assets/
# Download Minecraft font 
curl -s -L -o assets/minecrafter.zip 'https://dl.dafont.com/dl/?f=minecrafter'
curl -s -L -o assets/minecraftia.zip 'https://dl.dafont.com/dl/?f=minecraftia'
unzip -o assets/minecrafter.zip -d assets/
unzip -o assets/minecraftia.zip -d assets/
rm assets/*.zip