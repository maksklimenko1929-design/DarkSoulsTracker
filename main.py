import json
import os
from pydoc import text
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps, ImageDraw

BASE_PROGRESS_FILE = os.path.dirname(os.path.abspath(__file__))
RINGS_IMAGES_DIR =os.path.join(
    BASE_PROGRESS_FILE,
    "images",
    "rings",
)
UI_IMAGES_DIR = os.path.join(
    "images",
    "ui",
)
  
PROGRESS_FILE = os.path.join(BASE_PROGRESS_FILE, "progress_base.json")

window = tk.Tk()
window.title("Dark Souls III Tracker")
window.geometry("1920x1080")
window.minsize(900, 650)

window_bg_path = os.path.join(
    BASE_PROGRESS_FILE,
    "images",
    "ui",
    "window_bg.png",
)
window_bg_source = Image.open(window_bg_path).convert("RGBA")
window_bg_source = ImageOps.fit(window_bg_source, (1920, 1080), method=Image.Resampling.LANCZOS)
window_bg_photo = ImageTk.PhotoImage(window_bg_source)


sidebar_panel_path = os.path.join(
    BASE_PROGRESS_FILE,
    "images",
    "ui",
    "sidebar_panel.png",
)
sidebar_panel_source = Image.open(sidebar_panel_path).convert("RGBA")
sidebar_panel_source = ImageOps.fit(sidebar_panel_source, (220, 900), method=Image.Resampling.LANCZOS)
sidebar_panel_photo = ImageTk.PhotoImage(sidebar_panel_source)

window_canvas = tk.Canvas(
    window,
    highlightthickness=0
)
window_canvas.place(
    x=0,
    y=0,
    relheight=1,
    relwidth=1,
)
window_canvas.create_image(
    0,
    0,
    image=window_bg_photo,
    anchor="nw"
)

sidebar_canvas = tk.Canvas(
    window,
    highlightthickness=0,
    width=220
)
sidebar_canvas.create_image(
    0,
    0,
    image=sidebar_panel_photo,
    anchor="nw"
)
sidebar_canvas.pack_propagate(False)
sidebar_canvas.create_text(
    110,
    50,
    text="DARK SOULS III\nTRAKER",
    font=("arial", 16, "bold"),
    fill="white",
    anchor="center"
)
sidebar_canvas.place(
    x=0,
    y=0,
    relheight=1,
    width=220
)
BG = "#08090b"
PANEL_BG = "#0a0d10"
ROW_BG = "#202020"
TEXT = "#A89467"
MUTED_TEXT = "#A0A0A0"
ACCENT = "#B89B5E"
CARD_BG = "#111719"
CARD_BORDER = "#303A3E"
CARD_COLLECTED_BG = "#19160F"
CARD_COLLECTED_BORDER = "#D5A653"
HOVER_BG = "#2A2A2A"
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Dark.Vertical.TScrollbar",
    background=ROW_BG,
    troughcolor=BG,
    bordercolor=BG,
    arrowcolor=TEXT
)
BASE_RINGS_BY_LOCATION = {
    "1. Cemetery of Ash / Firelink Shrine": [
        "Life Ring",
        "Ashen Estus Ring",
        "Estus Ring",
        "Covetous Silver Serpent Ring",
    ],
    "2. High Wall of Lothric": [
        "Ring of Sacrifice",
    ],
    "3. Undead Settlement": [
        "Flynn's Ring",
        "Chloranthy Ring",
        "Bloodbite Ring",
        "Flame Stoneplate Ring",
        "Fire Clutch Ring",
        "Saint's Ring",
    ],
    "4. Road of Sacrifices / Farron Keep": [
        "Great Swamp Ring",
        "Lingering Dragoncrest Ring",
        "Sage Ring",
        "Hawk Ring",
        "Farron Ring",
        "Wolf Ring",
        "Poisonbite Ring",
    ],
    "5. Cathedral of the Deep": [
        "Deep Ring",
        "Lloyd's Shield Ring",
        "Lloyd's Sword Ring",
        "Dark Clutch Ring",
        "Ring of the Evil Eye",
        "Aldrich's Sapphire",
        "Aldrich's Ruby",
    ],
    "6. Catacombs of Carthus / Smouldering Lake": [
        "Carthus Milkring",
        "Carthus Bloodring",
        "Witch's Ring",
        "Knight Slayer's Ring",
        "Thunder Stoneplate Ring",
        "Speckled Stoneplate Ring",
    ],
    "7. Irithyll of the Boreal Valley / Anor Londo": [
        "Ring of Favor",
        "Pontiff's Right Eye",
        "Pontiff's Left Eye",
        "Magic Clutch Ring",
        "Wood Grain Ring",
        "Leo Ring",
        "Sun Princess Ring",
        "Darkmoon Ring",
        "Slumbering Dragoncrest Ring",
        "Ring of Steel Protection",
        "Ring of the Sun's First Born",
    ],
    "8. Irithyll Dungeon / Profaned Capital": [
        "Bellowing Dragoncrest Ring",
        "Covetous Gold Serpent Ring",
        "Dark Stoneplate Ring",
        "Dusk Crown Ring",
        "Cursebite Ring",
        "Magic Stoneplate Ring",
    ],
    "9. Lothric Castle / Grand Archives / Consumed King": [
        "Knight's Ring",
        "Red Tearstone Ring",
        "Scholar Ring",
        "Hunter's Ring",
        "Lightning Clutch Ring",
        "Fleshbite Ring",
        "Priestess Ring",
    ],
    "10. Archdragon Peak": [
        "Calamity Ring",
        "Dragonscale Ring",
    ],
    "11. Covenants / Quests / Boss Souls / Vendors": [
        "Havel's Ring",
        "Prisoner's Chain",
        "Reversal Ring",
        "Untrue Dark Ring",
        "Untrue White Ring",
        "Horsehoof Ring",
        "Obscuring Ring",
        "Silvercat Ring",
        "Skull Ring",
        "Blue Tearstone Ring",
        "Young Dragon Ring",
        "Morne's Ring",
        "Hornet Ring",
    ],
        "12. NG+ Cemetery of Ash / Firelink Shrine": [
        "Speckled Stoneplate Ring +1",
    ],

    "13. NG+ High Wall of Lothric": [
        "Fleshbite Ring +1",
    ],

    "14. NG+ Undead Settlement": [
        "Poisonbite Ring +1",
        "Life Ring +1",
    ],

    "15. NG+ Road of Sacrifices / Farron Keep": [
        "Lingering Dragoncrest Ring +1",
        "Magic Stoneplate Ring +1",
        "Wolf Ring +1",
    ],

    "16. NG+ Cathedral of the Deep": [
        "Ring of the Evil Eye +1",
    ],

    "17. NG+ Catacombs of Carthus / Smouldering Lake": [
        "Thunder Stoneplate Ring +1",
        "Bloodbite Ring +1",
    ],

    "18. NG+ Irithyll of the Boreal Valley / Anor Londo": [
        "Covetous Gold Serpent Ring +1",
        "Chloranthy Ring +1",
        "Ring of Favor +1",
    ],

    "19. NG+ Irithyll Dungeon / Profaned Capital": [
        "Covetous Silver Serpent Ring +1",
        "Flame Stoneplate Ring +1",
    ],

    "20. NG+ Lothric Castle / Grand Archives / Consumed King's Garden / Untended Graves": [
        "Life Ring +2",
        "Dark Stoneplate Ring +1",
        "Sage Ring +1",
        "Wood Grain Ring +1",
        "Ring of Steel Protection +1",
    ],

    "21. NG+ Archdragon Peak": [
        "Havel's Ring +1",
    ],

    "22. NG++ Cemetery of Ash / Firelink Shrine": [
        "Wolf Ring +2",
    ],

    "23. NG++ High Wall of Lothric": [
        "Ring of the Evil Eye +2",
    ],

    "24. NG++ Undead Settlement": [
        "Covetous Silver Serpent Ring +2",
    ],

    "25. NG++ Road of Sacrifices / Farron Keep": [
        "Chloranthy Ring +2",
        "Dark Stoneplate Ring +2",
    ],

    "26. NG++ Cathedral of the Deep": [
        "Ring of Favor +2",
    ],

    "27. NG++ Catacombs of Carthus / Smouldering Lake": [
        "Ring of Steel Protection +2",
        "Flame Stoneplate Ring +2",
    ],

    "28. NG++ Irithyll of the Boreal Valley / Anor Londo": [
        "Wood Grain Ring +2",
        "Havel's Ring +2",
    ],

    "29. NG++ Irithyll Dungeon / Profaned Capital": [
        "Magic Stoneplate Ring +2",
    ],

    "30. NG++ Lothric Castle / Grand Archives / Consumed King's Garden / Untended Graves": [
        "Thunder Stoneplate Ring +2",
        "Sage Ring +2",
        "Lingering Dragoncrest Ring +2",
        "Life Ring +3",
    ],

    "31. NG++ Archdragon Peak": [
        "Covetous Gold Serpent Ring +2",
    ],
}
RING_GUIDES = {
    'Life Ring': {
        "location": 'Firelink Shrine',
        "missable": 'No',
        "how_to_get": (
            'Choose it as a Burial Gift, or give  the Dreamchaser\'s Ashes to the Shrine Handmaid and buy it for 1,500 '
            'souls.'
        ),
    },

    'Ashen Estus Ring': {
        "location": 'Untended Graves',
        "missable": 'No',
        "how_to_get": (
            'From the Untended Graves bonfire, take the left path and loot the corpse '
            'behind the Corvians.'
        ),
    },

    'Estus Ring': {
        "location": 'Firelink Shrine',
        "missable": 'No',
        "how_to_get": (
            'Buy the Tower Key from the Shrine Handmaid, open the tower behind Firelink '
            'Shrine, and carefully drop down the coffins and ledges to the bottom.'
        ),
    },

    'Covetous Silver Serpent Ring': {
        "location": 'Firelink Shrine',
        "missable": 'No',
        "how_to_get": (
            'Reach the rafters above Firelink Shrine, strike the illusory wall at the end '
            'of a beam, then drop down to the chest.'
        ),
    },

    'Ring of Sacrifice': {
        "location": 'High Wall of Lothric',
        "missable": 'No',
        "how_to_get": (
            'One early copy is on an awning above the courtyard with the Winged Knight. '
            'Other copies can also be obtained later.'
        ),
    },

    "Flynn's Ring": {
        "location": 'Undead Settlement',
        "missable": 'No',
        "how_to_get": (
            'After helping Siegward fight the Fire Demon, climb onto the rooftops and '
            'loot the corpse on the broken wooden platform.'
        ),
    },

    'Chloranthy Ring': {
        "location": 'Undead Settlement',
        "missable": 'No',
        "how_to_get": (
            'In the tower used to leave the Siegward/Fire Demon area, break the crates '
            'and drop to the bottom to find the ring.'
        ),
    },

    'Bloodbite Ring': {
        "location": 'Undead Settlement',
        "missable": 'No',
        "how_to_get": 'Kill the large rat in the sewer near the Dilapidated Bridge area.',
    },

    'Flame Stoneplate Ring': {
        "location": 'Undead Settlement',
        "missable": 'No',
        "how_to_get": (
            'Loot the corpse hanging near the cage carrier that leads to the Pit of '
            'Hollows.'
        ),
    },

    'Fire Clutch Ring': {
        "location": 'Undead Settlement',
        "missable": 'No',
        "how_to_get": (
            'Near the Cliff Underside bonfire, follow the broken path by the guillotine '
            'to the corpse holding the ring.'
        ),
    },

    "Saint's Ring": {
        "location": 'Firelink Shrine',
        "missable": 'No',
        "how_to_get": 'Buy it from Irina of Carim.',
    },

    'Great Swamp Ring': {
        "location": 'Road of Sacrifices',
        "missable": 'No',
        "how_to_get": 'Kill one of the giant crabs in the Crucifixion Woods.',
    },

    'Lingering Dragoncrest Ring': {
        "location": 'Farron Keep',
        "missable": 'No',
        "how_to_get": 'Kill the giant crab near the Keep Ruins area.',
    },

    'Sage Ring': {
        "location": 'Road of Sacrifices',
        "missable": 'No',
        "how_to_get": (
            'From Crucifixion Woods, follow the wall through the water to a small room '
            'where the ring is on a corpse.'
        ),
    },

    'Hawk Ring': {
        "location": 'Undead Settlement',
        "missable": 'No',
        "how_to_get": (
            'Obtained from the giant archer at the top of the tower, either after he dies '
            'or by killing him.'
        ),
    },

    'Farron Ring': {
        "location": 'Firelink Shrine',
        "missable": 'Yes (Hawkwood quest)',
        "how_to_get": 'Speak to Hawkwood after defeating the Abyss Watchers.',
    },

    'Wolf Ring': {
        "location": 'Farron Keep',
        "missable": 'No',
        "how_to_get": (
            "Reach rank 2 in the Watchdogs of Farron covenant by offering 30 Wolf's Blood "
            'Swordgrass.'
        ),
    },

    'Poisonbite Ring': {
        "location": 'Cathedral of the Deep',
        "missable": 'No',
        "how_to_get": (
            'From Cleansing Chapel, take the outside path toward the large crystal lizard '
            'area; the ring is on a corpse in the nearby stone passage.'
        ),
    },

    'Deep Ring': {
        "location": 'Cathedral of the Deep',
        "missable": 'No',
        "how_to_get": (
            'Use the lift near Cleansing Chapel, climb the outside ladder, and kill the '
            'Deacon in the tower.'
        ),
    },

    "Lloyd's Shield Ring": {
        "location": 'Firelink Shrine',
        "missable": 'No',
        "how_to_get": "Give the Paladin's Ashes to the Shrine Handmaid, then buy the ring from her.",
    },

    "Lloyd's Sword Ring": {
        "location": 'Cathedral of the Deep',
        "missable": 'No',
        "how_to_get": 'Inside the cathedral, loot the corpse on the upper walkway beside the giant.',
    },

    'Dark Clutch Ring': {
        "location": 'Irithyll Dungeon',
        "missable": 'No',
        "how_to_get": 'In the lower sewer passage, kill the Mimic at the end to obtain the ring.',
    },

    'Ring of the Evil Eye': {
        "location": 'Irithyll Dungeon',
        "missable": 'Yes (Anri quest)',
        "how_to_get": (
            "Follow Anri's quest. Anri can give the ring in the Catacombs after learning "
            "Horace's location, or later at the Church of Yorshka."
        ),
    },

    "Aldrich's Sapphire": {
        "location": 'Cathedral of the Deep',
        "missable": 'No',
        "how_to_get": 'Kill the Deep Accursed in the side room on the lower floor of the cathedral.',
    },

    "Aldrich's Ruby": {
        "location": 'Anor Londo',
        "missable": 'No',
        "how_to_get": (
            'Kill the Deep Accursed hanging from the ceiling near the main doors inside '
            'Anor Londo.'
        ),
    },

    'Carthus Milkring': {
        "location": 'Catacombs of Carthus',
        "missable": 'No',
        "how_to_get": 'Loot it in the room filled with breakable urns and pots.',
    },

    'Carthus Bloodring': {
        "location": 'Catacombs of Carthus',
        "missable": 'No',
        "how_to_get": (
            'From the Catacombs bonfire, follow the lower passage with wheel skeletons to '
            'the corpse at the end.'
        ),
    },

    "Witch's Ring": {
        "location": 'Catacombs of Carthus',
        "missable": 'No',
        "how_to_get": 'Found on a corpse just before the Abandoned Tomb bonfire.',
    },

    "Knight Slayer's Ring": {
        "location": 'Smouldering Lake',
        "missable": 'No',
        "how_to_get": 'Defeat Knight Slayer Tsorig in the Demon Ruins area.',
    },

    'Thunder Stoneplate Ring': {
        "location": 'Archdragon Peak',
        "missable": 'No',
        "how_to_get": (
            'From Dragon-Kin Mausoleum, progress to the outdoor scaffolding area and '
            'climb the ladder to the ring.'
        ),
    },

    'Speckled Stoneplate Ring': {
        "location": 'Smouldering Lake',
        "missable": 'No',
        "how_to_get": (
            'Use the giant ballista to break the stone wall in Smouldering Lake, then '
            'loot the ring behind it.'
        ),
    },

    'Ring of Favor': {
        "location": 'Irithyll of the Boreal Valley',
        "missable": 'No',
        "how_to_get": (
            "Defeat both Sulyvahn's Beasts in the Water Reserve near the Aldrich Faithful "
            'covenant.'
        ),
    },

    "Pontiff's Right Eye": {
        "location": 'Irithyll of the Boreal Valley',
        "missable": 'No',
        "how_to_get": "Kill the Sulyvahn's Beast that attacks on the bridge entering Irithyll.",
    },

    "Pontiff's Left Eye": {
        "location": 'Firelink Shrine',
        "missable": 'No',
        "how_to_get": 'Transpose the Soul of Boreal Valley Vordt with Ludleth of Courland.',
    },

    'Magic Clutch Ring': {
        "location": 'Irithyll of the Boreal Valley',
        "missable": 'No',
        "how_to_get": (
            'Near the Church of Yorshka, strike the illusory wall in the side passage to '
            'reveal the ring.'
        ),
    },

    'Wood Grain Ring': {
        "location": 'Firelink Shrine',
        "missable": 'No',
        "how_to_get": (
            "Find the Easterner's Ashes in Irithyll and give them to the Shrine Handmaid, "
            'then buy the ring.'
        ),
    },

    'Leo Ring': {
        "location": 'Irithyll of the Boreal Valley',
        "missable": 'No',
        "how_to_get": (
            'After the kitchen area, open the chest on the upper floor of the room with '
            'Silver Knights.'
        ),
    },

    'Sun Princess Ring': {
        "location": 'Anor Londo',
        "missable": 'No',
        "how_to_get": (
            "After defeating Aldrich, take the lift up to Gwynevere's chamber and loot "
            'the ring.'
        ),
    },

    'Darkmoon Ring': {
        "location": 'Anor Londo',
        "missable": 'No',
        "how_to_get": (
            'Reach rank 1 in Blade of the Darkmoon by offering 10 Proofs of a Concord '
            'Kept to Company Captain Yorshka.'
        ),
    },

    'Slumbering Dragoncrest Ring': {
        "location": 'Firelink Shrine',
        "missable": 'Yes (Orbeck quest)',
        "how_to_get": (
            'Buy Aural Decoy, Farron Flashsword, Pestilent Mist and Spook from Orbeck, '
            'then speak to him.'
        ),
    },

    'Ring of Steel Protection': {
        "location": 'Archdragon Peak',
        "missable": 'No',
        "how_to_get": (
            'In the Ancient Wyvern area, take the right-hand route and follow the outer '
            'ledge around to the ring.'
        ),
    },

    "Ring of the Sun's First Born": {
        "location": 'Irithyll of the Boreal Valley',
        "missable": 'No',
        "how_to_get": (
            "Backtrack from Pontiff Sulyvahn's bonfire and drop to the lower platform "
            'with the ring.'
        ),
    },

    'Bellowing Dragoncrest Ring': {
        "location": 'Irithyll Dungeon',
        "missable": 'No',
        "how_to_get": (
            "Use the Jailbreaker's Key to open the shortcut near the first bonfire, then "
            'drop to the ledge with the ring.'
        ),
    },

    'Covetous Gold Serpent Ring': {
        "location": 'Irithyll Dungeon',
        "missable": 'No',
        "how_to_get": (
            "Open Siegward's locked cell in Irithyll Dungeon/Profaned Capital and loot "
            'the ring inside.'
        ),
    },

    'Dark Stoneplate Ring': {
        "location": 'Irithyll of the Boreal Valley',
        "missable": 'No',
        "how_to_get": (
            'After Pontiff Sulyvahn, enter the giant courtyard and search the dark lower '
            'area under the left side.'
        ),
    },

    'Dusk Crown Ring': {
        "location": 'Irithyll Dungeon',
        "missable": 'No',
        "how_to_get": 'Found on a corpse inside a cell on the lowest prison level.',
    },

    'Cursebite Ring': {
        "location": 'Profaned Capital',
        "missable": 'No',
        "how_to_get": (
            'In the toxic swamp area, enter the cave below the building and loot the '
            'corpse.'
        ),
    },

    'Magic Stoneplate Ring': {
        "location": "Consumed King's Garden",
        "missable": 'No',
        "how_to_get": "Defeat the cathedral knight guarding the approach to Oceiros' boss room.",
    },

    "Knight's Ring": {
        "location": 'Lothric Castle',
        "missable": 'No',
        "how_to_get": 'Found in the room near the Warrior of Sunlight altar.',
    },

    'Red Tearstone Ring': {
        "location": 'Lothric Castle',
        "missable": 'No',
        "how_to_get": (
            'Before Dragonslayer Armour, enter the side building and go out onto the '
            'balcony/ledge to find the ring.'
        ),
    },

    'Scholar Ring': {
        "location": 'Grand Archives',
        "missable": 'No',
        "how_to_get": (
            'Pull the lever near the central bridge to move a bookshelf and reveal the '
            'corpse holding the ring.'
        ),
    },

    "Hunter's Ring": {
        "location": 'Grand Archives',
        "missable": 'No',
        "how_to_get": (
            'On the roof with the three golden Winged Knights, climb the tower stairs and '
            'ladder to the top.'
        ),
    },

    'Lightning Clutch Ring': {
        "location": 'Archdragon Peak',
        "missable": 'No',
        "how_to_get": (
            'Before the Ancient Wyvern arena, take the side path to the left to find the '
            'ring.'
        ),
    },

    'Fleshbite Ring': {
        "location": 'Grand Archives',
        "missable": 'No',
        "how_to_get": (
            'In the large cursed-hand room after the Crystal Sage bridge, loot the corpse '
            'on the upper level.'
        ),
    },

    'Priestess Ring': {
        "location": 'Untended Graves',
        "missable": 'No',
        "how_to_get": 'Buy it from the Shrine Handmaid in Dark Firelink Shrine.',
    },

    'Calamity Ring': {
        "location": 'Archdragon Peak',
        "missable": 'No',
        "how_to_get": (
            'At the dragon altar near Dragon-Kin Mausoleum, perform the Path of the '
            'Dragon gesture.'
        ),
    },

    'Dragonscale Ring': {
        "location": "Consumed King's Garden",
        "missable": 'No',
        "how_to_get": (
            'Ride the shortcut elevator toward the toxic swamp and jump off midway to '
            'reach the ledge with the ring.'
        ),
    },

    "Havel's Ring": {
        "location": 'Firelink Shrine',
        "missable": 'No',
        "how_to_get": 'Transpose the Soul of a Stray Demon with Ludleth of Courland.',
    },

    "Prisoner's Chain": {
        "location": 'Firelink Shrine',
        "missable": 'No',
        "how_to_get": 'Transpose the Soul of Champion Gundyr with Ludleth of Courland.',
    },

    'Reversal Ring': {
        "location": 'Anor Londo / Darkmoon Tomb',
        "missable": 'No',
        "how_to_get": (
            'In the circular room before the Anor Londo spiral lift, reveal the illusory '
            'wall and enter Darkmoon Tomb; the ring is on the right.'
        ),
    },

    'Untrue Dark Ring': {
        "location": 'Firelink Shrine',
        "missable": 'Yes (Yuria quest)',
        "how_to_get": 'Buy it from Yuria of Londor after she appears in Firelink Shrine.',
    },

    'Untrue White Ring': {
        "location": 'Firelink Shrine',
        "missable": 'Yes (Yuria quest)',
        "how_to_get": 'Buy it from Yuria of Londor after she appears in Firelink Shrine.',
    },

    'Horsehoof Ring': {
        "location": 'Firelink Shrine',
        "missable": 'No',
        "how_to_get": 'Buy it from Unbreakable Patches while Greirat is in Firelink Shrine, or obtain it as a drop when Patches dies.',
    },

    'Obscuring Ring': {
        "location": 'Cathedral of the Deep',
        "missable": 'No',
        "how_to_get": "Reach rank 1 in Rosaria's Fingers by offering 10 Pale Tongues.",
    },

    'Silvercat Ring': {
        "location": 'Firelink Shrine',
        "missable": 'Yes (Sirris quest)',
        "how_to_get": (
            'Help Sirris defeat Creighton using her summon sign on the Irithyll bridge, '
            'then speak to her in Firelink Shrine.'
        ),
    },

    'Skull Ring': {
        "location": 'Firelink Shrine',
        "missable": 'No',
        "how_to_get": (
            'After placing the Lords of Cinder on their thrones and progressing to the '
            "endgame, inspect Ludleth's remains in Firelink Shrine."
        ),
    },

    'Blue Tearstone Ring': {
        "location": 'High Wall of Lothric',
        "missable": 'No',
        "how_to_get": 'Free Greirat from his cell and speak to him; he gives you the ring.',
    },

    'Young Dragon Ring': {
        "location": 'Firelink Shrine',
        "missable": 'Yes (Orbeck quest)',
        "how_to_get": (
            'Sorcerers start with it. Otherwise, give Orbeck a scroll and buy enough '
            'sorceries from him to receive the ring.'
        ),
    },

    "Morne's Ring": {
        "location": 'Road of Sacrifices',
        "missable": 'No',
        "how_to_get": (
            'Before Halfway Fortress, drop from the bridge to the lower path and loot the '
            'corpse.'
        ),
    },

    'Hornet Ring': {
        "location": 'Untended Graves',
        "missable": 'No',
        "how_to_get": (
            'Outside Dark Firelink Shrine, take the lower path on the right and loot the '
            'ring.'
        ),
    },

    'Speckled Stoneplate Ring +1': {
        "location": 'Cemetery of Ash',
        "missable": 'No',
        "how_to_get": (
            'In the starting area, go to the arena with the Ravenous Crystal Lizard; the '
            'ring is on the right side.'
        ),
    },

    'Fleshbite Ring +1': {
        "location": 'High Wall of Lothric',
        "missable": 'No',
        "how_to_get": (
            'From Tower on the Wall, reach the rooftop with the transforming enemy. '
            'Before descending the next ladder, jump to the nearby roof with the corpse.'
        ),
    },

    'Poisonbite Ring +1': {
        "location": 'Undead Settlement',
        "missable": 'No',
        "how_to_get": (
            'In the giant archer graveyard, look behind the well near the White Birch '
            'Tree.'
        ),
    },

    'Life Ring +1': {
        "location": 'Undead Settlement',
        "missable": 'No',
        "how_to_get": (
            'Jump off the tower elevator halfway to reach the balcony where Siegward sits. The ring is on that balcony, near the pillars just before Siegward.'
        ),
    },

    'Lingering Dragoncrest Ring +1': {
        "location": 'Road of Sacrifices',
        "missable": 'No',
        "how_to_get": (
            'Near the Crucifixion Woods bonfire, search the water close to the nearest '
            'giant crab and tree.'
        ),
    },

    'Magic Stoneplate Ring +1': {
        "location": 'Farron Keep',
        "missable": 'No',
        "how_to_get": (
            'From the Farron Keep bonfire, head right toward the Basilisk area; the ring '
            'is on a corpse beside a tree.'
        ),
    },

    'Wolf Ring +1': {
        "location": 'Farron Keep',
        "missable": 'No',
        "how_to_get": (
            'Found on a corpse just outside the building containing the Keep Ruins '
            'bonfire.'
        ),
    },

    'Ring of the Evil Eye +1': {
        "location": 'Cathedral of the Deep',
        "missable": 'No',
        "how_to_get": 'Behind the altar immediately before the Deacons of the Deep boss room.',
    },

    'Thunder Stoneplate Ring +1': {
        "location": 'Catacombs of Carthus',
        "missable": 'No',
        "how_to_get": 'Found in the room filled with breakable pots near the Carthus Milkring.',
    },

    'Bloodbite Ring +1': {
        "location": 'Smouldering Lake',
        "missable": 'No',
        "how_to_get": 'At the top of Smouldering Lake, loot the corpse beside the giant ballista.',
    },

    'Covetous Gold Serpent Ring +1': {
        "location": 'Irithyll of the Boreal Valley',
        "missable": 'No',
        "how_to_get": (
            'From Church of Yorshka, pass through the dark room toward the river. After '
            'exiting, drop through the broken railing to the rocky ledge.'
        ),
    },

    'Chloranthy Ring +1': {
        "location": 'Irithyll of the Boreal Valley',
        "missable": 'No',
        "how_to_get": (
            "Backtrack from Pontiff Sulyvahn's bonfire toward the boss entrance and check "
            'behind the structure below the ledge.'
        ),
    },

    'Ring of Favor +1': {
        "location": 'Irithyll of the Boreal Valley',
        "missable": 'No',
        "how_to_get": "Found on the upper walkway/balcony above Pontiff Sulyvahn's boss arena.",
    },

    'Covetous Silver Serpent Ring +1': {
        "location": 'Irithyll Dungeon',
        "missable": 'No',
        "how_to_get": (
            'Use the shortcut lift near the Irithyll Dungeon bonfire and jump off midway '
            'to the platform with the ring.'
        ),
    },

    'Flame Stoneplate Ring +1': {
        "location": 'Profaned Capital',
        "missable": 'No',
        "how_to_get": (
            'In the toxic swamp area, climb to the roof of the building and drop to the '
            'ledge above the doorway.'
        ),
    },

    'Life Ring +2': {
        "location": 'Lothric Castle',
        "missable": 'No',
        "how_to_get": (
            'From Dragon Barracks, cross the bridge, enter the room on the right, climb '
            'the ladder, exit outside and drop to the ledge below.'
        ),
    },

    'Dark Stoneplate Ring +1': {
        "location": 'Lothric Castle',
        "missable": 'No',
        "how_to_get": (
            'Near Dragonslayer Armour, drop through the broken railing by the white '
            'wyvern area and follow the room to the outside ledge.'
        ),
    },

    'Sage Ring +1': {
        "location": 'Grand Archives',
        "missable": 'No',
        "how_to_get": (
            'From the roof with the three golden Winged Knights, drop into the archives '
            'and work down the rafters to the white beam with the ring.'
        ),
    },

    'Wood Grain Ring +1': {
        "location": "Consumed King's Garden",
        "missable": 'No',
        "how_to_get": (
            'Take the first elevator all the way down and check behind it in the toxic '
            'pool.'
        ),
    },

    'Ring of Steel Protection +1': {
        "location": 'Untended Graves',
        "missable": 'No',
        "how_to_get": (
            'At Dark Firelink Shrine, go to the right-side tower; the ring is on a corpse '
            'beside the locked gate.'
        ),
    },

    "Havel's Ring +1": {
        "location": 'Archdragon Peak',
        "missable": 'No',
        "how_to_get": (
            'From Great Belfry, follow the path toward the altar. Just after the second '
            'stone arch, check the left side.'
        ),
    },

    'Wolf Ring +2': {
        "location": 'Cemetery of Ash',
        "missable": 'No',
        "how_to_get": (
            'After defeating Iudex Gundyr, open the door toward Firelink Shrine and '
            'immediately look to the left.'
        ),
    },

    'Ring of the Evil Eye +2': {
        "location": 'High Wall of Lothric',
        "missable": 'No',
        "how_to_get": (
            'In the room with the first Estus Shard, search the corner by the shelves, '
            'barrels and crates.'
        ),
    },

    'Covetous Silver Serpent Ring +2': {
        "location": 'Undead Settlement',
        "missable": 'No',
        "how_to_get": (
            "In the Siegward/Fire Demon area, climb to Flynn's Ring and look down for the "
            'nearby hut roof holding this ring.'
        ),
    },

    'Chloranthy Ring +2': {
        "location": 'Road of Sacrifices',
        "missable": 'No',
        "how_to_get": (
            'From the first bonfire, pass the wagon and Corvian caster, then drop to the '
            'ledge beside the tree.'
        ),
    },

    'Dark Stoneplate Ring +2': {
        "location": 'Farron Keep',
        "missable": 'No',
        "how_to_get": (
            'From Keep Ruins, cross the bridge with the three Ghru and search behind the '
            'building near the extinguished flame.'
        ),
    },

    'Ring of Favor +2': {
        "location": 'Cathedral of the Deep',
        "missable": 'No',
        "how_to_get": (
            'Reach the upper cathedral roof path toward Rosaria. Before the rafters, '
            'check the left alcove guarded by the axe-wielding enemy.'
        ),
    },

    'Ring of Steel Protection +2': {
        "location": 'Catacombs of Carthus',
        "missable": 'No',
        "how_to_get": (
            'At the first long bridge, look left for the item on a stone pillar and drop '
            'down to it.'
        ),
    },

    'Flame Stoneplate Ring +2': {
        "location": 'Smouldering Lake',
        "missable": 'No',
        "how_to_get": (
            "Near Old King's Antechamber/Demon Ruins, break the illusory wall leading to "
            'the Black Knight with an axe; the ring is beside him.'
        ),
    },

    'Wood Grain Ring +2': {
        "location": 'Irithyll of the Boreal Valley',
        "missable": 'No',
        "how_to_get": (
            'After the kitchen and Silver Knight room, go outside and immediately turn '
            'right into the small alcove.'
        ),
    },

    "Havel's Ring +2": {
        "location": 'Anor Londo / Prison Tower',
        "missable": 'No',
        "how_to_get": (
            'From the Blade of the Darkmoon covenant area, carefully drop down the wooden '
            'beams/platforms below the Prison Tower bonfire.'
        ),
    },

    'Magic Stoneplate Ring +2': {
        "location": 'Profaned Capital',
        "missable": 'No',
        "how_to_get": (
            'From the Profaned Capital bonfire, climb down inside the tower, exit through '
            'the broken wall and turn right down the stairs.'
        ),
    },

    'Thunder Stoneplate Ring +2': {
        "location": 'Lothric Castle',
        "missable": 'No',
        "how_to_get": (
            'Before Dragonslayer Armour, use the side balcony near the Red Tearstone '
            'Ring, drop to the lower roof and follow the ledge.'
        ),
    },

    'Sage Ring +2': {
        "location": "Consumed King's Garden",
        "missable": 'No',
        "how_to_get": (
            'Take the first elevator down and jump off midway. Follow the broken '
            'platforms and stairs to the ring.'
        ),
    },

    'Lingering Dragoncrest Ring +2': {
        "location": 'Grand Archives',
        "missable": 'No',
        "how_to_get": (
            'On the roof with the three golden Winged Knights, climb the spiral stairs '
            'but do not use the ladder; circle the ledge to the hidden alcove.'
        ),
    },

    'Life Ring +3': {
        "location": 'Untended Graves',
        "missable": 'No',
        "how_to_get": 'In Dark Firelink Shrine, look behind the large throne.',
    },

    'Covetous Gold Serpent Ring +2': {
        "location": 'Archdragon Peak',
        "missable": 'No',
        "how_to_get": (
            'After defeating the Nameless King, search the next area near the middle '
            'staircase.'
        ),
    },

}
# Плоский список для розрахунку
if os.path.exists(PROGRESS_FILE):
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        progress = json.load(f)

    # Якщо файл має старий формат — створюємо новий
    if "rings" not in progress:
        progress = {
            "rings": {},
            "emotes": {}
        }

else:
    progress = {
        "rings": {},
        "emotes": {}
    }
ALL_BASE_RINGS = []

for rings in BASE_RINGS_BY_LOCATION.values():
    ALL_BASE_RINGS.extend(rings)

TOTAL_RINGS = len(ALL_BASE_RINGS)

rings_variables = {}

for ring in ALL_BASE_RINGS:
    rings_variables[ring] = tk.BooleanVar(
        value=progress["rings"].get(ring, False)
    )

main_frame = tk.Frame(window)
rings_frame = tk.Frame(window, bg=BG)
ring_bg_canvas = tk.Canvas(
    rings_frame,
    highlightthickness=0
)
ring_bg_canvas.place(
    x=0,
    y=0,
    relheight=1,
    relwidth=1,
)
ring_bg_canvas.create_image(
    0,
    0,
    image=window_bg_photo,
    anchor="nw"
)
sidebar_canvas.create_rectangle(
            10,
            200,
            250,
            5,
            tags="sidebar_button_ring",
        )
    
sidebar_canvas.create_text(
        15,
        118, 
        tags="sidebar_button_ring",     
        text="Rings",
        fill=TEXT,
        font=("Georgia", 16, "bold"),
        anchor="nw",
    )
    

sidebar_canvas.tag_bind(
        "sidebar_button_ring",
        "<Button-1>",
        lambda event: show_rings()
    )

def show_rings():
    main_frame.pack_forget()
    emotes_frame.place_forget()
    
    rings_frame.place(
    x=220,
    y=0,
    relwidth=1,
    relheight=1,
    width=-220
)

   

def show_main():
    rings_frame.place_forget()
    emotes_frame.place_forget()


def save_progress():
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, ensure_ascii=False, indent=4)


def update_rings_progress():
    collected = sum(var.get() for var in rings_variables.values())
    percentage = (collected / TOTAL_RINGS) * 100 if TOTAL_RINGS > 0 else 0

    ring_bg_canvas.itemconfig(
        "progress_text",
        text=f"Collected: {collected}/{TOTAL_RINGS}"
    )

    ring_bg_canvas.itemconfig(
        "rings_percentage",
        text=f"{percentage:.1f}%"
    )

    draw_rings_progress_bar(percentage)
def update_ring_card_style(ring):
    card_canvas = ring_card_canvases.get(ring)
    name_label = ring_name_labels.get(ring)
    bg_item = ring_bg_items.get(ring)

    if not card_canvas:
        return

    if rings_variables[ring].get():
        card_canvas.itemconfig(
            "card_shape",
            fill="",
            outline=ACCENT,
            width=2
        )
        card_canvas.itemconfig(
            bg_item,
            image=card_bg_collected_photo
        )
        card_canvas.itemconfig(
            "ring_name",
            fill=ACCENT
        )

    else:
        card_canvas.itemconfig(
            "card_shape",
            fill="",
            outline=CARD_BORDER,
            width=2
        )
        card_canvas.itemconfig(
            bg_item,
            image=card_bg_photo
        )

   
def ring_changed(ring):
    progress["rings"][ring] = rings_variables[ring].get()
    save_progress()
    update_rings_progress()
    update_ring_card_style(ring)
    if filter_mode.get() in ("Collected", "Uncollected"):
        search_changed()


window.bind("<Escape>", lambda event: show_main())

# Налаштування вікна


ring_bg_canvas.create_text(
    10,
    5,
    text="Rings",
    fill=TEXT,
    font=("Georgia", 20, "bold"),
    anchor="nw"
)
ring_bg_canvas.create_text(
    10,
    50,
    tags="progress_text",
    text=f"Collected: 0/{TOTAL_RINGS}",
    fill=ACCENT,
    font=("Georgia", 12, "bold"),
    anchor="nw"
)

def draw_rings_progress_bar(percentage):
    width = 240
    height = 12
    scale = 4

    image = Image.new(
        "RGBA",
        (width * scale, height * scale),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(image)

    draw.rounded_rectangle(
        (0, 0, width * scale - 1, height * scale - 1),
        radius=6 * scale,
        fill="#2A2A2A"
    )

    fill_width = int(width * (percentage / 100))

    if fill_width > 0:
        draw.rounded_rectangle(
            (0, 0, fill_width * scale, height * scale - 1),
            radius=6 * scale,
            fill=ACCENT
        )

    image = image.resize(
        (width, height),
        Image.Resampling.LANCZOS
    )

    progress_photo = ImageTk.PhotoImage(image)

    ring_bg_canvas.progress_photo = progress_photo

    ring_bg_canvas.delete("rings_progress_bar")

    ring_bg_canvas.create_image(
        180,
        55,
        tags="rings_progress_bar",
        image=progress_photo,
        anchor="nw"
    )

ring_bg_canvas.create_text(
    430,
    50,
    tags="rings_percentage",
    text="0%",
    fill=ACCENT,
    font=("Georgia", 11, "bold"),
    anchor="nw"
)
filter_mode = tk.StringVar(value="All")


def toggle_filter_menu():
    if filter_menu.winfo_ismapped(): 
       filter_menu.place_forget()
       filter_button_visual.config(bg=CARD_BORDER)
    else:
        x=filter_button_visual.winfo_rootx() - window.winfo_rootx()
        y=filter_button_visual.winfo_rooty() - window.winfo_rooty() + filter_button_visual.winfo_height()
        filter_menu.place(
            width=130,
            height=90,
            x=x,
            y=y,
        )
        filter_menu.lift()
        filter_button_visual.config(bg=ACCENT)
def reposition_filter_menu(event):
    if filter_menu.winfo_ismapped():
        x=filter_button_visual.winfo_rootx() - window.winfo_rootx()
        y=filter_button_visual.winfo_rooty() - window.winfo_rooty() + filter_button_visual.winfo_height()
        filter_menu.place(
            x=x,
            y=y
        )
    if event.widget != window:
            return

window.bind("<Configure>", reposition_filter_menu)
    

def select_filter(name):
    filter_button.config(text=f"{name}")
    filter_menu.place_forget()
    filter_mode.set(name)
    search_changed()
    for option_name, button in filter_buttons.items():
        if option_name == name:
         button.pack_forget()
        else:
         button.pack(anchor="w", fill="x")
    
filter_button_visual = tk.Frame(
    rings_frame,
    bg=CARD_BORDER,
    padx=1,
    pady=1
)    
    
filter_button = tk.Button(
    filter_button_visual,
    text="All",
    font=("Georgia", 13,),
    anchor="w",
    width=10,
    padx=12,
    bd=0,
    cursor="hand2",
    bg=ROW_BG,
    fg=MUTED_TEXT,
    relief="flat",
    command=toggle_filter_menu
)
filter_button.pack(
    fill="both",
    ipady=3,
    )
filter_button_visual.place(
    relx=1,
    y=50,
    anchor="ne",
    x=-10,
    width=165,
    height=44
)
filter_menu = tk.Frame(
    window,
    bg=ACCENT,
    highlightthickness=1,
    highlightbackground=ACCENT,
)
filter_menu.pack_propagate(False)
def on_enter(event):
    event.widget.config(bg=HOVER_BG)
def on_leave(event):
    event.widget.config(bg=ROW_BG) 
def close_filter_on_click(event):
    if event.widget == filter_button:
        return
    if event.widget in filter_buttons.values():
        return
    filter_menu.place_forget()
    filter_button_visual.config(bg=CARD_BORDER)\

window.bind_all(
    "<Button-1>",
    close_filter_on_click,
    add="+"
)
filter_all_button = tk.Button(
    filter_menu,
    text="All",
    font=("Georgia", 13,),
    anchor="w",
    padx=12,
    bg=ROW_BG,
    fg=MUTED_TEXT,
    relief="flat",
    bd=0,
    justify="center",
    cursor="hand2",
    command=lambda: select_filter("All")
)
filter_all_button.pack(anchor="w", fill="x")
filter_all_button.bind("<Enter>", on_enter)
filter_all_button.bind("<Leave>", on_leave)
filter_collected_button = tk.Button(
    filter_menu,
    text="Collected",
    font=("Georgia", 13,),
    anchor="w",
    padx=12,
    bg=ROW_BG,
    fg=MUTED_TEXT,
    relief="flat",
    bd=0,
    justify="center",
    cursor="hand2",
    command=lambda: select_filter("Collected")
)
filter_collected_button.pack(anchor="w", fill="x")
filter_collected_button.bind("<Enter>", on_enter)
filter_collected_button.bind("<Leave>", on_leave)
filter_missable_button = tk.Button(
    filter_menu,
    text="Missable",
    font=("Georgia", 13,),
    anchor="w",
    padx=12,
    bg=ROW_BG,
    fg=MUTED_TEXT,
    relief="flat",
    bd=0,
    justify="center",
    cursor="hand2",
    command=lambda: select_filter("Missable")
)
filter_missable_button.pack(anchor="w", fill="x")
filter_missable_button.bind("<Enter>", on_enter)
filter_missable_button.bind("<Leave>", on_leave)
filter_uncollected_button = tk.Button(
    filter_menu,
    text="Uncollected",
    font=("Georgia", 13,),
    anchor="w",
    padx=12,
    bg=ROW_BG,
    fg=MUTED_TEXT,
    relief="flat",
    bd=0,
    cursor="hand2",
    command=lambda: select_filter("Uncollected")
)
filter_uncollected_button.pack(anchor="w", fill="x")
filter_uncollected_button.bind("<Enter>", on_enter)
filter_uncollected_button.bind("<Leave>", on_leave)

filter_buttons = {
    "All": filter_all_button,
    "Collected": filter_collected_button,
    "Missable": filter_missable_button,
    "Uncollected": filter_uncollected_button
}
filter_buttons["All"].pack_forget()





search_var = tk.StringVar()

search_entry = tk.Entry(
    rings_frame,
    textvariable=search_var,
    font=("Georgia", 11),
    width=30,
    bg=ROW_BG,
    fg=TEXT,
    insertbackground=TEXT,
    relief="flat",
    highlightthickness=1,
    highlightbackground="#343434",
    highlightcolor=ACCENT,
)

search_entry.place(
    relx=1,
    y=50,
    anchor="ne",
    x=-193,
    width=250,
    height=44
)
search_entry.insert(0, "🔍  Search rings...")
search_entry.config(fg="#666666")
def search_focus_in(event):
    if search_entry.get().strip().startswith("🔍"):
        search_entry.delete(0, tk.END)
        search_entry.config(fg=TEXT)


def search_focus_out(event):
    if search_entry.get() == "":
        search_entry.insert(0, "🔍  Search rings...")
        search_entry.config(fg="#666666")

search_entry.bind("<FocusIn>", search_focus_in)

search_entry.bind(
    "<Button-1>",
    search_focus_in,
    add="+"
)
search_entry.bind("<FocusOut>", search_focus_out)
def restore_search_placeholder(event):
    if event.widget != search_entry:
        rings_frame.focus_set()

        if search_entry.get() == "":
            search_entry.insert(0, "🔍  Search rings...")
            search_entry.config(fg="#666666")


window.bind_all(
    "<Button-1>",
    restore_search_placeholder,
    add="+",
)
def search_changed(*args):
    text = search_var.get().lower()
    mode = filter_mode.get()

    if text == "🔍  search rings...":
        text = ""

    visible_rings = []

    for ring, row in ring_rows.items():
       matches_search = text in ring.lower()
       is_missable = RING_GUIDES[ring]["missable"].startswith("Yes")
       is_collected =  rings_variables[ring].get()
       is_uncollected = not is_collected
       if mode == "All":
           matches_filter = True
       elif mode == "Missable":
           matches_filter = is_missable
       elif mode == "Collected":
           matches_filter = is_collected
       elif mode == "Uncollected":
           matches_filter = is_uncollected
       if matches_search and matches_filter:
           visible_rings.append(ring)
       else:
           row.grid_forget()
    grid_row = 0
    grid_column = 0
         
    for ring in visible_rings:
        row = ring_rows[ring]
        row.grid(
            row=grid_row,
            column=grid_column,
            padx=1,
            pady=8
            )
        grid_column += 1
        if grid_column == 4:
            grid_column = 0
            grid_row += 1

    update_rings_scrollregion()
    rings_canvas.yview_moveto(0)

search_var.trace_add("write", search_changed)
rings_content = tk.Canvas(rings_frame, highlightthickness=0,bd=0)
rings_content.create_image(
    0,
    -90,
    image=window_bg_photo,
    anchor="nw"
)
rings_content.pack(fill="both", pady=(90, 0), expand=True)
rings_canvas = tk.Canvas(rings_content, bg=BG, highlightthickness=0)
rings_scrollbar = tk.Scrollbar(
    rings_content,
    orient="vertical",
    command=rings_canvas.yview
)
rings_scrollable_frame = tk.Frame(rings_canvas, bg=BG)
ring_list_canvas = tk.Canvas(
    rings_scrollable_frame,
    highlightthickness=0
)
ring_list_canvas.place(
    x=0,
    y=0,
    relheight=1,
    relwidth=1,
)
ring_list_canvas.create_image(
    0,
    0,
    tags="list_bg",
    image=window_bg_photo,
    anchor="nw"
)

def update_rings_scrollregion(event=None):
    rings_canvas.itemconfigure(
    rings_window,
    width=rings_canvas.winfo_width()
)
    rings_scrollable_frame.update_idletasks()

    content_height = rings_scrollable_frame.winfo_reqheight()
    canvas_height = rings_canvas.winfo_height()
    bg_height = window_bg_photo.height
    rings_canvas.configure(
        scrollregion=(
            0,
            0,
            rings_scrollable_frame.winfo_reqwidth(),
            max(content_height, canvas_height)
        )
    )

rings_canvas.bind(
    "<Configure>",
    update_rings_scrollregion
)
rings_scrollable_frame.bind(
    "<Configure>", lambda e: rings_canvas.configure(scrollregion=rings_canvas.bbox("all"))
)

rings_window = rings_canvas.create_window(
    (0, 0),
    window=rings_scrollable_frame,
    anchor="nw"
)
rings_canvas.configure(yscrollcommand=rings_scrollbar.set)



guide_panel_path = os.path.join(
    BASE_PROGRESS_FILE,
    "images",
    "ui",
    "guide_panel.png"
)
guide_panel_source = Image.open(guide_panel_path).convert("RGBA")
guide_panel_source = ImageOps.fit(guide_panel_source, (390, 632), method=Image.Resampling.LANCZOS)
guide_panel_photo = ImageTk.PhotoImage(guide_panel_source)





guide_panel = tk.Frame(
    rings_content,
    bg=PANEL_BG,
    width=390,
    height=632
)
rings_content.grid_columnconfigure(0, weight=1)
rings_content.grid_columnconfigure(1, minsize=420)
rings_content.grid_rowconfigure(0, weight=1)
guide_panel.pack_propagate(False)
rings_canvas.grid(
    row=0,
    column=0,
    sticky="nsew"
)

guide_panel_canvas = tk.Canvas(
    guide_panel,
    highlightthickness=0
)
guide_panel_canvas.place(
    x=0,
    y=0,
    relheight=1,
    relwidth=1,
)
guide_panel_canvas.create_image(
    0,
    0,
    image=guide_panel_photo,
    anchor="nw"
)

guide_panel.grid(
    row=0,
    column=1,
    padx=(14, 0),
    pady=6,
    sticky="nw",
)
guide_panel_canvas.create_text(
    195,
    50,
    tags="guide_title",
    text="Select a ring",
    fill=ACCENT,
    font=("Georgia", 22, "bold"),
    justify="center",
    width=340
)

guide_panel_canvas.create_image(
    195,
    190,
    tags="guide_ring_image",

)

ring_bg_canvas.create_text(
    10,
    5,
    text="Rings",
    fill=TEXT,
    font=("Georgia", 20, "bold"),
    anchor="nw"
)

guide_panel_canvas.create_text(
    20,
    332,
    text="Location:",
    fill=MUTED_TEXT,
    font=("Georgia", 13),
    anchor="nw"
)
guide_panel_canvas.create_text(
    100,
    332,
    tags="location_value",
    text="",
    fill=TEXT,
    font=("Georgia", 13),
    anchor="nw"
)


guide_panel_canvas.create_text(
    20,
    380,
    text="Missable:",
    fill=MUTED_TEXT,
    font=("Georgia", 13),
    anchor="nw"
)
guide_panel_canvas.create_text(
    100,
    380,
    tags="missable_value",
    text="",
    fill=TEXT,
    font=("Georgia", 13),
    anchor="nw"
)

guide_panel_canvas.create_text(
    20,
    432,
    text="How to get:",
    fill=MUTED_TEXT,
    font=("Georgia", 13),
    anchor="nw"
)
guide_panel_canvas.create_text(
    20,
    460,
    tags="how_to_get_value",
    text="",
    fill=TEXT,
    font=("Georgia", 13),
    anchor="nw",
    width=340
)

def show_ring_guide(ring):
    guide = RING_GUIDES.get(ring)

    if not guide:
        return

    guide_panel_canvas.itemconfig(
        "guide_title",
        text=ring,
    )
    base_ring_name = ring

    if " +" in ring:
        base_ring_name = ring.split(" +")[0]

    image_filename = base_ring_name.replace(" ", "_") + ".png"

    image_path = os.path.join(
        RINGS_IMAGES_DIR,
        image_filename
        )

    if os.path.exists(image_path):
        guide_source = Image.open(image_path)

    guide_source = ImageOps.contain(
        guide_source,
        (210, 210),
        method=Image.Resampling.LANCZOS
    )

    guide_photo = ImageTk.PhotoImage(guide_source)

    guide_panel_canvas.itemconfig(
        "guide_ring_image",
        image=guide_photo
    )

    guide_panel_canvas.image =guide_photo

    guide_panel_canvas.itemconfig(
        "location_value",
        text=f"{guide['location']}"
    )

    guide_panel_canvas.itemconfig(
        "missable_value",
        text=f"{guide['missable']}"
    )
    if guide["missable"].startswith("Yes"):
            guide_panel_canvas.itemconfig(
            "missable_value",
            fill="#FF0000"
        )
    else:
       guide_panel_canvas.itemconfig(
           "missable_value",
           fill=TEXT
       )

    guide_panel_canvas.itemconfig(
        "how_to_get_value",
        text=f"{guide['how_to_get']}"
    )

# Відображення чекбоксів
def create_rounded_card(canvas, width, height, radius, fill, outline):
    points = [
        radius, 0,
        width - radius, 0,
        width, 0,
        width,radius,
        width, height - radius,
        width, height,
        width - radius, height,
        radius, height,
        0, height,
        0, height - radius,
        0, radius,
        0, 0,
    ]
    return canvas.create_polygon(
        points,
        smooth=True,
        splinesteps=36,
        fill=fill,
        outline=outline,
        width=1,
        tags="card_shape"
)
ring_rows = {}
ring_card_canvases = {}
ring_name_labels = {}
ring_image_labels = {}
ring_checkbuttons = {}
location_labels = {}
ring_card_bg_images = {}
ring_card_bg_collected_images = {}
ring_bg_items = {}
grid_row = 0
ring_column = 0
for column in range(4):
    rings_scrollable_frame.grid_columnconfigure(
        column,
        weight=1,
        uniform="rings"
    )

ring_images = {}
def draw_ring_check(ring, card_canvas):
    card_canvas.delete("ring_check")

    size = 28
    scale = 4

    image = Image.new(
        "RGBA",
        (size * scale, size * scale),
        (0, 0, 0, 0)
    )

    draw = ImageDraw.Draw(image)

    if rings_variables[ring].get():
        fill_color = ACCENT
        outline_color = ACCENT
    else:
        fill_color = CARD_BG
        outline_color = CARD_BORDER

    draw.ellipse(
        (
            3 * scale,
            3 * scale,
            25 * scale,
            25 * scale
        ),
        fill=fill_color,
        outline=outline_color,
        width=scale
    )

    image = image.resize(
        (size, size),
        Image.Resampling.LANCZOS
    )

    check_photo = ImageTk.PhotoImage(image)

    card_canvas.check_photo = check_photo
    
    card_canvas.create_image(
        165,
        12,
        tags="ring_check",
        image=check_photo,
        anchor="nw"
    )
    if rings_variables[ring].get():
        card_canvas.create_text(
            178,
            26,
            tags="ring_check",
            text="✓",
            fill=CARD_BG,
            font=("Segoe UI Symbol", 11)
        )
    card_canvas.tag_bind(
        "ring_check",
        "<Button-1>",
        lambda event, r=ring, c=card_canvas:toggle_ring_check(r, c)
        )
def toggle_ring_check(ring, canvas):
    rings_variables[ring].set(
        not rings_variables[ring].get()
    )

    ring_changed(ring)
    draw_ring_check(ring, canvas)
card_bg_path = os.path.join(
    BASE_PROGRESS_FILE,
    "images",
    "ui",
    "cards_bg.png"
)
    
card_bg_collected_path = os.path.join(
    BASE_PROGRESS_FILE,
    "images",
    "ui",
    "card_bg_collected.png"
)
card_bg_source = Image.open(card_bg_path).convert("RGBA")
card_bg_source = ImageOps.fit(card_bg_source, (195, 210), method=Image.Resampling.LANCZOS)
card_bg_photo = ImageTk.PhotoImage(card_bg_source)

card_bg_collected_source = Image.open(card_bg_collected_path).convert("RGBA")
card_bg_collected_source = ImageOps.fit(card_bg_collected_source, (195, 225), method=Image.Resampling.LANCZOS)
card_bg_collected_photo = ImageTk.PhotoImage(card_bg_collected_source)

for loc_name, rings in BASE_RINGS_BY_LOCATION.items():
    for ring in rings:
        row = tk.Frame(
            rings_scrollable_frame,
            bg=BG,
            width=195,
            height=210,
            bd=0
        )
        card_canvas = tk.Canvas(
            row,
            width=195,
            height=210,
            bg=BG,
            highlightthickness=0
        )
        ring_card_canvases[ring] = card_canvas
        card_canvas.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )
        bg_item = card_canvas.create_image(
            0,
            0,
            image=card_bg_photo,
            anchor = "nw"
        )
        ring_bg_items[ring] = bg_item
        
        create_rounded_card(
            card_canvas,
            194,
            209,
            8,
            "",
            CARD_BORDER
        )
        
        row.pack_propagate(False)

        ring_rows[ring] = row

        row.grid(
            row=grid_row,
            column=ring_column,
            padx=1,
            pady=8
        )

        base_ring_name = ring

        if " +" in ring:
            base_ring_name = ring.split(" +")[0]

        image_filename = base_ring_name.replace(" ", "_") + ".png"

        image_path = os.path.join(
            RINGS_IMAGES_DIR,
            image_filename
        )

        if os.path.exists(image_path):
            ring_source = Image.open(image_path).convert("RGBA")

            ring_source = ImageOps.contain(
            ring_source,
            (160, 160),
            method=Image.Resampling.LANCZOS
    )

            ring_image = ImageTk.PhotoImage(ring_source)

            ring_images[ring] = ring_image

            ring_image_label = tk.Label(
                row,
                image=ring_image,
                bg=CARD_BG,
                cursor="hand2"
            )
            ring_image_labels[ring] = ring_image_label

           # ring_image_label.pack(
           #     side="top",
           #    pady=(8, 0)
           # )
            
            
            card_canvas.create_image(
                97,
                95,
                tags="ring_image",
                image=ring_image,
                anchor="center"
        )
        draw_ring_check(
            ring,
            card_canvas
            )

        card_canvas.tag_bind(
            "ring_image",
            "<Button-1>",
            lambda event, r=ring: show_ring_guide(r)
            )
        rings_lable = tk.Label(
            row,
            text=ring,
            font=("Georgia", 12),
            bg=CARD_BG,
            fg=TEXT,
            cursor="hand2",
            wraplength=150,
            height=2,
            justify="center",
            anchor="center"
        )
        ring_name_labels[ring] = rings_lable    
        
        card_canvas.create_text(
            97,
            190,
            tags="ring_name",
            text=ring,
            fill=TEXT,
            font=("Georgia", 12),
            width=170,
            justify="center"
)
        
        rings_lable.bind(
            "<Button-1>",
            lambda event, r=ring: show_ring_guide(r)
        )

        if RING_GUIDES[ring]["missable"].startswith("Yes"):
            card_canvas.create_text(
                20,
                24,
                text="❗",
                fill= "#FC0303",
                font=("Georgia", 13),
                anchor="nw"
            )

           # missable_label.place(
           #     x=8,
           #     y=8
           # )

        ring_column += 1

        if ring_column == 4:
            ring_column = 0
            grid_row += 1
for ring in ALL_BASE_RINGS:
    update_ring_card_style(ring)
    rings_scrollable_frame.update_idletasks()
    content_height = rings_scrollable_frame.winfo_reqheight()
    bg_height = window_bg_photo.height()
    for y in range(bg_height, content_height, bg_height):
        ring_list_canvas.create_image(
            0,
            y,
            image=window_bg_photo,
            anchor="nw",
            tags="list_bg"
        )

    
update_rings_progress()
BASE_EMOTES_BY_LOCATION = {
    "1. Starter Gestures": [
        "Point Forward",
        "Point Up",
        "Point Down",
        "Wave",
        "Jump for Joy",
        "Joy",
        "Bow",
    ],
    "2. Cemetery of Ash / Firelink Shrine": [
        "Rest",
        "Collapse",
        "Hurrah!",
        "Beckon",
        "Call Over",
        "Welcome",
        "Curl Up",
        "Applause",
        "Darkmoon Loyalty",
        "Dignified Bow",
    ],
    "3. Undead Settlement": [
        "Prayer",
        "Toast",
        "Sleep",
        "Rejoice",
    ],
    "4. Farron Keep": [
        "Proper Bow",
        "Legion Etiquette",
        "Duel Bow",
        "By My Sword",
    ],
    "5. Cathedral / Irithyll": [
        "Prostration",
        "Quiet Resolve",
    ],
    "6. Catacombs / Smouldering Lake": [
        "My Thanks!",
    ],
    "7. Profaned Capital": [
        "Stretch Out",
    ],
    "8. Lothric Castle": [
        "Praise the Sun",
    ],
    "9. Orbeck of Vinheim": [
        "Silent Ally",
    ],
    "10. Consumed King's Garden": [
        "Path of the Dragon",
    ],
    "11. Special NPC": [
        "Patches Squat",
    ],
}
ALL_BASE_EMOTES = []

for emotes in BASE_EMOTES_BY_LOCATION.values():
    ALL_BASE_EMOTES.extend(emotes)

TOTAL_EMOTES = len(ALL_BASE_EMOTES)

emote_variables = {}

for emote in ALL_BASE_EMOTES:
    emote_variables[emote] = tk.BooleanVar(
        value=progress["emotes"].get(emote, False)
    )
emotes_frame = tk.Frame(window, bg=BG)
sidebar_canvas.create_rectangle(
            10,
            300,
            250,
            5,
            tags="sidebar_button_emotes",
        )
    
sidebar_canvas.create_text(
        15,
        175, 
        tags="sidebar_button_emotes",     
        text="Emotes",
        fill=TEXT,
        font=("Georgia", 16, "bold"),
        anchor="nw",
    )
    

sidebar_canvas.tag_bind(
        "sidebar_button_emotes",
        "<Button-1>",
        lambda event: show_emotes()
    )
def show_emotes():
    main_frame.pack_forget()
    rings_frame.place_forget()
    

    emotes_frame.place(
    x=220,
    y=0,
    relwidth=1,
    relheight=1,
    width=-220
)

    sidebar_canvas.lift()

def update_emotes_progress():
    collected = sum(var.get() for var in emote_variables.values())
    percentage = (collected / TOTAL_EMOTES) * 100 if TOTAL_EMOTES > 0 else 0
    emote_progress_label.config(
        text=f"Emotes Collected: {collected}/{TOTAL_EMOTES} ({percentage:.1f}%)")
    


def emote_changed(emote):
    progress["emotes"][emote] = emote_variables[emote].get()
    save_progress()
    update_emotes_progress()

btn_back = tk.Button(
    emotes_frame, text="Back", font=("Arial", 10), command=show_main, bg=ROW_BG, fg=TEXT, activebackground=PANEL_BG, activeforeground=TEXT, bd=0, padx=12, pady=6
)
btn_back.pack(pady=5, anchor="nw", padx=10)

# Налаштування вікна
title = tk.Label(
    emotes_frame, text="Emotes", font=("Arial", 16, "bold"), bg=BG, fg=TEXT
)
title.pack(pady=8)

emote_progress_label = tk.Label(
    emotes_frame,
    text=f"Emotes Collected: 0/{TOTAL_EMOTES}",
    font=("Arial", 11, "bold"),
    bg=BG,
    fg=ACCENT,
)
emote_progress_label.pack(pady=2)

emotes_canvas = tk.Canvas(emotes_frame,bg=BG, highlightthickness=0)
emotes_scrollbar = ttk.Scrollbar(
    emotes_frame,
    orient="vertical",
    command=emotes_canvas.yview,
    style="Dark.Vertical.TScrollbar"
)
emotes_scrollable_frame = tk.Frame(emotes_canvas, bg=BG)

emotes_scrollable_frame.bind(
    "<Configure>", lambda e: emotes_canvas.configure(scrollregion=emotes_canvas.bbox("all"))
)

emotes_canvas.create_window((0, 0), window=emotes_scrollable_frame, anchor="nw")
emotes_canvas.configure(yscrollcommand=emotes_scrollbar.set)

emotes_canvas.pack(side="left", fill="both", expand=True)
emotes_scrollbar.pack(side="right", fill="y")

def on_mousewheel(event):
    if rings_frame.winfo_ismapped():
        rings_canvas.yview_scroll(
            int(-1 * (event.delta / 120)), "units"
        )

    elif emotes_frame.winfo_ismapped():
        emotes_canvas.yview_scroll(
            int(-1 * (event.delta / 120)), "units"
        )


window.bind_all("<MouseWheel>", on_mousewheel)
# Відображення чекбоксів
for loc_name, emotes in BASE_EMOTES_BY_LOCATION.items():
    tk.Label(
        emotes_scrollable_frame,
        text=loc_name,
        font=("Arial", 11, "bold"),
        bg=BG,
        fg=ACCENT
    ).pack(anchor="w", padx=10, pady=(12, 4))

    for emote in emotes:
        row = tk.Frame(emotes_scrollable_frame, bg=BG)
        row.pack(anchor="w", padx=25, pady=1)

        cb = tk.Checkbutton(
            row,
            text=emote,
            font=("Arial", 10),
            variable=emote_variables[emote],
            command=lambda e=emote: emote_changed(e),
            bg=BG,
            fg=TEXT,
            activebackground=BG,
            activeforeground=TEXT,
            selectcolor=ROW_BG
        )
        cb.pack(side="left")
                        
update_emotes_progress()

window.mainloop()