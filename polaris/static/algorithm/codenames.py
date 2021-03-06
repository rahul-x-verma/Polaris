"""
DICTIONARIES FOR CODENAME LOOKUP

The algorithm and accompanying database use short codenames to refer to physical
locations. The full name and description of physical locations will be shown on
the user interface. 
"""
codenames = {"Downtown Berkeley BART Station: Shattuck Avenue @ Addison Street" : "BART",
 "Evans Hall: Hearst Mining Circle Side" : "EVANS",
 "Strawberry Canyon Recreational Area" : "SCRA",
 "UC Botanical Garden": "UCBG",
 "Lawrence Hall of Science": "LHS",
 "Space Sciences Lab/MSRI": "SSL",
 "Oxford Street @ University Avenue": "OXFU",
 "Tolman Hall: Hearst Avenue @ Arch Street": "TOLMAN",
 "North Gate Hall: Hearst Avenue @ Euclid Avenue": "NORTH",
 "Cory Hall: Hearst Avenue @ LeRoy Avenue": "CORY",
 "Gayley @ Stadium Rimway": "STADIUM",
 "Haas School of Business, Piedmont Avenue Side": "HAAS",
 "International House: Piedmont Avenue @ Bancroft Way": "IHOUSE",
 "Piedmont Avenue @ Channing Way": "PIEDCHA",
 "College Avenue @ Haste Street": "COLHA",
 "Kroeber Hall: Bancroft Way @ College Avenue": "KROEBER",
 "Hearst Memorial Gym: Bancroft Way @ Bowditch Street": "HEARST",
 "Sproul Hall: Bancroft Way @ Barrow Lane": "SPROUL",
 "RSF: Bancroft Way @ Ellsworth Street": "RSF",
 "Banway Building: Bancroft Way @ Shattuck Avenue": "BANWAY",
 "Shattuck Avenue @ Kittredge Street": "SHAKIT",
 "Moffit Library, University Drive": "MOFFIT",
 "West Circle: University Drive Side": "WEST",
 "Li Ka Shing Center: West Crescent Side": "LKS",
 "Moffit Library, Memorial Glade Side": "MOFFITM",
 "Life Science Addition, West Circle Side": "LSA",
 "University Avenue @ Shattuck Avenue": "USHA",
 "Foothill Student Housing: Hearst Avenue Side": "FOOTHILL",
 "Highland Place @ Ridge Road": "HIRIDGE",
 "East Gate: Gayley Road @ University Drive": "EAST",
 "Bowles Hall: Gayley Road Side": "BOWLES",
 "ASUC: Bancroft Way @ Telegraph Avenue": "ASUC",
 "Bancroft Way @ Kittredge Street": "BAKIT",
 "Shattuck Avenue @ Allston Way": "SHAAL",
 "Manville Hall: Shattuck Avenue @ Channing Avenue": "MANV",
 "Dwight Way @ Fulton Street": "DWIFU",
 "Ellsworth Structure, Channing Way Side": "ELCHA",
 "Unit 3: Channing Way @ Telegraph Avenue": "UN3",
 "Unit 1: Channing Way @ College Avenue": "UN1",
 "Unit 2: College Avenue @ Haste Street": "UN2",
 "Warring Street @ Piedmont Crescent": "WAPIE",
 "Warring Street @ Bancroft Steps": "WABA",
 "Greek Theater: Gayley Road @ University Drive": "GREEK",
 "Shattuck Avenue @ Bancroft Way": "BASHA",
 "Clark Kerr Campus": "CKC",
 "Warring Street @ Channing Way": "WACHA",
 "West Crescent": "WC",
 }

reverse_codenames = {}

for k,v in codenames.items():
    reverse_codenames[v] = k
