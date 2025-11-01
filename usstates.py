
# ----- Graph of US States -----
usa_map = {
    "Alabama": ["Florida", "Georgia", "Tennessee", "Mississippi"],
    "Alaska": [],
    "Arizona": ["California", "Nevada", "Utah", "Colorado", "New Mexico"],
    "Arkansas": ["Louisiana", "Mississippi", "Tennessee", "Missouri", "Oklahoma", "Texas"],
    "California": ["Oregon", "Nevada", "Arizona"],
    "Colorado": ["Wyoming", "Nebraska", "Kansas", "Oklahoma", "New Mexico", "Arizona", "Utah"],
    "Connecticut": ["New York", "Massachusetts", "Rhode Island"],
    "Delaware": ["Maryland", "Pennsylvania", "New Jersey"],
    "Florida": ["Alabama", "Georgia"],
    "Georgia": ["Florida", "Alabama", "Tennessee", "North Carolina", "South Carolina"],
    "Hawaii": [],
    "Idaho": ["Washington", "Oregon", "Nevada", "Utah", "Wyoming", "Montana"],
    "Illinois": ["Wisconsin", "Iowa", "Missouri", "Kentucky", "Indiana"],
    "Indiana": ["Illinois", "Kentucky", "Ohio", "Michigan"],
    "Iowa": ["Minnesota", "Wisconsin", "Illinois", "Missouri", "Nebraska", "South Dakota"],
    "Kansas": ["Nebraska", "Missouri", "Oklahoma", "Colorado"],
    "Kentucky": ["Illinois", "Indiana", "Ohio", "West Virginia", "Virginia", "Tennessee", "Missouri"],
    "Louisiana": ["Arkansas", "Mississippi", "Texas"],
    "Maine": ["New Hampshire"],
    "Maryland": ["Delaware", "Pennsylvania", "Virginia", "West Virginia"],
    "Massachusetts": ["Connecticut", "New York", "New Hampshire", "Rhode Island", "Vermont"],
    "Michigan": ["Indiana", "Ohio", "Wisconsin", "Minnesota"],
    "Minnesota": ["North Dakota", "South Dakota", "Iowa", "Wisconsin", "Michigan"],
    "Mississippi": ["Alabama", "Arkansas", "Tennessee", "Louisiana"],
    "Missouri": ["Iowa", "Illinois", "Kentucky", "Tennessee", "Arkansas", "Oklahoma", "Kansas", "Nebraska"],
    "Montana": ["Idaho", "Wyoming", "South Dakota", "North Dakota"],
    "Nebraska": ["Colorado", "Iowa", "Kansas", "Missouri", "South Dakota", "Wyoming"],
    "Nevada": ["Idaho", "Utah", "Arizona", "California", "Oregon"],
    "New Hampshire": ["Maine", "Massachusetts", "Vermont"],
    "New Jersey": ["Delaware", "Pennsylvania", "New York"],
    "New Mexico": ["Arizona", "Utah", "Colorado", "Oklahoma", "Texas"],
    "New York": ["Connecticut", "Massachusetts", "Vermont", "New Jersey", "Pennsylvania", "Rhode Island"],
    "North Carolina": ["Virginia", "Tennessee", "Georgia", "South Carolina"],
    "North Dakota": ["Minnesota", "South Dakota", "Montana"],
    "Ohio": ["Pennsylvania", "West Virginia", "Kentucky", "Indiana", "Michigan"],
    "Oklahoma": ["Kansas", "Missouri", "Arkansas", "Texas", "New Mexico", "Colorado"],
    "Oregon": ["California", "Nevada", "Idaho", "Washington"],
    "Pennsylvania": ["New York", "New Jersey", "Delaware", "Maryland", "West Virginia", "Ohio"],
    "Rhode Island": ["Connecticut", "Massachusetts"],
    "South Carolina": ["Georgia", "North Carolina"],
    "South Dakota": ["North Dakota", "Minnesota", "Iowa", "Nebraska", "Wyoming", "Montana"],
    "Tennessee": ["Kentucky", "Virginia", "North Carolina", "Georgia", "Alabama", "Mississippi", "Arkansas", "Missouri"],
    "Texas": ["New Mexico", "Oklahoma", "Arkansas", "Louisiana"],
    "Utah": ["Idaho", "Wyoming", "Colorado", "New Mexico", "Arizona", "Nevada"],
    "Vermont": ["New York", "New Hampshire", "Massachusetts"],
    "Virginia": ["Kentucky", "West Virginia", "Maryland", "North Carolina", "Tennessee"],
    "Washington": ["Idaho", "Oregon"],
    "West Virginia": ["Ohio", "Pennsylvania", "Maryland", "Virginia", "Kentucky"],
    "Wisconsin": ["Minnesota", "Iowa", "Illinois", "Michigan"],
    "Wyoming": ["Montana", "South Dakota", "Nebraska", "Colorado", "Utah", "Idaho"]
}

state_info = {
    "California": {
        "things_to_do": ["Drive the Pacific Coast Highway", "Visit Disneyland", "Explore Yosemite National Park"],
        "fun_fact": "California produces over 80% of U.S. wine.",
        "drive_time": 6
    },
    "Florida": {
        "things_to_do": ["Visit Disney World", "Relax on Miami Beach", "Explore the Everglades"],
        "fun_fact": "Florida has the longest coastline in the contiguous U.S.",
        "drive_time": 5
    },
    "New York": {
        "things_to_do": ["See the Statue of Liberty", "Walk Central Park", "Visit Niagara Falls"],
        "fun_fact": "New York City was the first capital of the U.S.",
        "drive_time": 4
    },
    "Texas": {
        "things_to_do": ["Visit The Alamo", "Explore Austin’s music scene", "Tour NASA in Houston"],
        "fun_fact": "Texas is larger than any European country.",
        "drive_time": 7
    },
    "Washington": {
        "things_to_do": ["Visit Mount Rainier", "Explore Pike Place Market", "See the Space Needle"],
        "fun_fact": "Washington is the only state named after a president.",
        "drive_time": 4
    },
    "Nevada": {
        "things_to_do": ["Visit Las Vegas", "Explore Lake Tahoe", "Drive scenic Highway 50"],
        "fun_fact": "Over 85% of Nevada is owned by the federal government.",
        "drive_time": 3
    },
    "Arizona": {
        "things_to_do": ["See the Grand Canyon", "Explore Sedona", "Drive Route 66 segments"],
        "fun_fact": "Arizona is home to the largest ponderosa pine forest in the world.",
        "drive_time": 4
    },
    "Illinois": {
        "things_to_do": ["Visit Millennium Park", "See Willis Tower", "Explore Chicago’s museums"],
        "fun_fact": "The first skyscraper in the world was built in Chicago.",
        "drive_time": 3
    },
    "Massachusetts": {
        "things_to_do": ["Walk the Freedom Trail", "Visit Boston Common", "Tour Harvard University"],
        "fun_fact": "Massachusetts was the first U.S. state to legalize same-sex marriage.",
        "drive_time": 2
    },
    "Georgia": {
        "things_to_do": ["Explore Atlanta museums", "Visit Savannah historic district", "Drive the Blue Ridge Scenic Route"],
        "fun_fact": "Georgia was the last of the original 13 colonies to be established.",
        "drive_time": 3
    },
    "Colorado": {
        "things_to_do": ["Ski in the Rockies", "Hike 14ers", "Visit Denver attractions"],
        "fun_fact": "Colorado is the only state where every part is above 1,000 meters in elevation.",
        "drive_time": 4
    },
    "Hawaii": {
        "things_to_do": ["Relax on Waikiki Beach", "Hike Diamond Head", "Visit Volcanoes National Park"],
        "fun_fact": "Hawaii is the only U.S. state made entirely of islands.",
        "drive_time": 2
    },
    "Alaska": {
        "things_to_do": ["See the Northern Lights", "Cruise Kenai Fjords", "Hike Denali National Park"],
        "fun_fact": "Alaska has the longest coastline of any U.S. state.",
        "drive_time": 5
    },
    "Pennsylvania": {
        "things_to_do": ["Visit Liberty Bell", "Explore Hersheypark", "Walk historic Philadelphia"],
        "fun_fact": "The first U.S. library was established in Philadelphia.",
        "drive_time": 3
    },
    "Michigan": {
        "things_to_do": ["Drive the Upper Peninsula", "Visit Mackinac Island", "Tour Detroit museums"],
        "fun_fact": "Michigan has the longest freshwater coastline of any state.",
        "drive_time": 4
    }
}
