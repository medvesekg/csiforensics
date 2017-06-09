#get the DNA string from the file
with open("dna.txt", "r") as dnaFile:
    DNAstring = dnaFile.read()

sequences = {
    "Hair": {
        "Black":"CCAGCAATCGC",
        "Brown":"GCCAGTGCCG",
        "Blonde":"TTAGCTATCGC"
    },
    "Face": {
        "Square":"GCCACGG",
        "Round":"ACCACAA",
        "Oval":"AGGCCTCA"
    },
    "Eyes": {
        "Blue":"TTGTGGTGGC",
        "Green":"GGGAGGTGGC",
        "Brown":"AAGTAGTGAC"
    },
    "Gender": {
        "Female":"TGAAGGACCTTC",
        "Male":"TGCAGGAACTTC"
    },
    "Race": {
        "White": "AAAACCTCA",
        "Black": "CGACTACAG",
        "Asian": "CGCGGGCCG"
    }
}

suspects = {
    "Eva": {
        "Gender":"Female",
        "Race":"White",
        "Hair":"Blonde",
        "Eyes":"Blue",
        "Face":"Oval"
    },
    "Larisa": {
        "Gender":"Female",
        "Race":"White",
        "Hair":"Brown",
        "Eyes":"Brown",
        "Face":"Oval"
    },
    "Matej": {
        "Gender":"Male",
        "Race":"White",
        "Hair":"Black",
        "Eyes":"Blue",
        "Face":"Oval"
    },
    "Miha": {
        "Gender":"Male",
        "Race":"White",
        "Hair":"Brown",
        "Eyes":"Green",
        "Face":"Square"
    }
}

# Find the substrings in the DNA string and build a suspect profile
suspectProfile = {}
print "Suspect profile: "
for feature in sequences:
    for value, substring in sequences[feature].iteritems():
        if substring in DNAstring:
            print feature + " - " + value
            suspectProfile[feature] = value

# Prepare for matching the suspect profile to the suspects by setting a counter
for suspect in suspects:
    suspects[suspect]["matching"] = 0

# Find the matches
for feature in suspectProfile:
    for suspect in suspects:
        if suspectProfile[feature] == suspects[suspect][feature]:
            suspects[suspect]["matching"] += 1

# If somebody matches all the features declare him guilty
for suspect in suspects:
    if suspects[suspect]["matching"] == len(suspectProfile):
        print suspect + " matches the profile. " + suspect + " ate all the ice cream."



