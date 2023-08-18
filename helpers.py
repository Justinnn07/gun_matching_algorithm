def determine_varna(dob):
    # Determine Varna based on birth year (example logic)
    # You would need to implement the actual determination logic here
    if dob.year % 4 == 0:
        return 'Brahmin'
    else:
        return 'Non-Brahmin'

def varna_score(dob_user, dob_partner):
    # Determine the Varna based on birth year (example)
    varna_user = determine_varna(dob_user)
    varna_partner = determine_varna(dob_partner)
    
    # Check if Varna is different
    if varna_user != varna_partner:
        return 1  # Different Varna scores 1 point
    else:
        return 0  # Same Varna scores 0 points
    

def vashya_score(dob_user, dob_partner):
    # Determine the Vashya based on birth year remainder (example)
    vashya_user = determine_vashya(dob_user)
    vashya_partner = determine_vashya(dob_partner)
    
    # Check if Vashya is compatible
    if vashya_user == vashya_partner:
        return 2  # Compatible Vashya scores 2 points
    else:
        return 0  # Incompatible Vashya scores 0 points

def determine_vashya(dob):
    # Determine Vashya based on birth year remainder (example logic)
    # You would need to implement the actual determination logic here
    remainder = (dob.year % 9) % 2
    if remainder == 0:
        return 'Chatushpad'
    else:
        return 'Jalchar'

def determine_nakshatra(dob):
    # Determine the birth star (nakshatra) based on day of birth (example logic)
    # You would need to implement the actual determination logic here
    nakshatra_names = [
        "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra", "Punarvasu",
        "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni", "Hasta",
        "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha", "Mula", "Purva Ashadha",
        "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha", "Purva Bhadrapada",
        "Uttara Bhadrapada", "Revati"
    ]
    
    nakshatra_index = dob.day - 1  # Using birth day as index (example)
    return  nakshatra_index


def tara_score(dob_user, dob_partner):
    # Determine the birth star (nakshatra) of the user and partner
    nakshatra_user = determine_nakshatra(dob_user)
    nakshatra_partner = determine_nakshatra(dob_partner)

    # Calculate compatibility based on nakshatra index (example logic)
    if nakshatra_user == nakshatra_partner:
        return 3  # Excellent score
    elif abs(nakshatra_user - nakshatra_partner) <= 3:
        return 2  # Good score
    else:
        return 0  # No compatibility

def yoni_score(dob_user, dob_partner):
    # Determine the animal sign of the user and partner (example logic)
    animal_user = determine_animal(dob_user)
    animal_partner = determine_animal(dob_partner)
    
    # Define compatibility based on animal signs (example logic)
    if animal_user == animal_partner:
        return 4  # Compatible animal signs score 4 points
    else:
        return 0  # Incompatible animal signs score 0 points

def determine_animal(dob):
    # Determine the animal sign based on birth year (example logic)
    # You would need to implement the actual determination logic here
    animals = [
        "Mouse", "Cow", "Tiger", "Rabbit", "Dragon", "Snake",
        "Horse", "Sheep", "Monkey", "Rooster", "Dog", "Pig"
    ]
    animal_index = (dob.year - 1900) % 12
    return animals[animal_index]

def determine_friendship(dob):
    # Determine planetary friendship based on birth year (example logic)
    # You would need to implement the actual determination logic here
    friendship_planets = [
        "Sun", "Moon", "Mars", "Mercury", "Jupiter", "Venus",
        "Saturn", "Rahu", "Ketu"
    ]
    planet_index = (dob.year - 1900) % 9
    return friendship_planets[planet_index]

def graha_maitri_score(dob_user, dob_partner):
    # Determine the planetary friendship based on birth year (example logic)
    friendship_user = determine_friendship(dob_user)
    friendship_partner = determine_friendship(dob_partner)
    
    # Define compatibility based on planetary friendship (example logic)
    if friendship_user == friendship_partner:
        return 5  # Planetary friends score 5 points
    else:
        return 0  # Planetary non-friends score 0 points

# Define the conditions for Gana aspect
def gana_score(dob_user, dob_partner):
    # Determine the Gana of the user and partner (example logic)
    gana_user = determine_gana(dob_user)
    gana_partner = determine_gana(dob_partner)
    
    # Define compatibility based on Gana (example logic)
    if gana_user == gana_partner:
        return 6  # Same Gana scores 6 points
    else:
        return 0  # Different Gana scores 0 points
    
def determine_gana(dob):
    # Determine Gana based on birth year (example logic)
    # You would need to implement the actual determination logic here
    gana_types = [
        "Deva", "Manushya", "Rakshasa"
    ]
    gana_index = (dob.year - 1900) % 3
    return gana_types[gana_index]

def bhakoot_score(dob_user, dob_partner):
    # Determine the Rashis (zodiac signs) of the user and partner (example logic)
    rashi_user = determine_rashi(dob_user)
    rashi_partner = determine_rashi(dob_partner)
    
    # Define compatibility based on Rashis (example logic)
    if rashi_user != rashi_partner:
        return 7  # Different Rashis score 7 points
    else:
        return 0  # Same Rashis score 0 points
    
def determine_rashi(dob):
    # Determine Rashi (zodiac sign) based on birth year (example logic)
    # You would need to implement the actual determination logic here
    rashis = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    rashi_index = (dob.year - 1900) % 12
    return rashis[rashi_index]

def nadi_score(dob_user, dob_partner):
    # Determine the Nadi of the user and partner (example logic)
    nadi_user = determine_nadi(dob_user)
    nadi_partner = determine_nadi(dob_partner)
    
    # Define compatibility based on Nadi (example logic)
    if nadi_user != nadi_partner:
        return 8  # Different Nadi scores 8 points
    else:
        return 0  # Same Nadi scores 0 points
    
def determine_nadi(dob):
    # Determine Nadi based on birth year (example logic)
    # You would need to implement the actual determination logic here
    nadi_types = [
        "Adi", "Madhya", "Antya"
    ]
    nadi_index = (dob.year - 1900) % 3
    return nadi_types[nadi_index]
    
    
def calculate_ashtakoota(dob_user, dob_partner):

    # Calculate compatibility scores for each aspect (out of 8)
    scores = {
        'Varna': varna_score(dob_user, dob_partner),
        'Vashya': vashya_score(dob_user, dob_partner),
        'Tara': tara_score(dob_user, dob_partner),
        'Yoni': yoni_score(dob_user, dob_partner),
        'Graha Maitri': graha_maitri_score(dob_user, dob_partner),
        'Gana': gana_score(dob_user, dob_partner),
        'Bhakoot': bhakoot_score(dob_user, dob_partner),
        'Nadi': nadi_score(dob_user, dob_partner)
    }
    
    # Calculate total compatibility score
    total_score = sum(scores.values())
    
    return total_score
