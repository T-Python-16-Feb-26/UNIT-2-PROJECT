import opennsfw2 as n2
from better_profanity import profanity

profanity.load_censor_words()

print(profanity.contains_profanity("hey how we doin"))
#score = n2.predict_image('C:\\Users\\Mohammed\\Desktop\\tuwaiq\\Unit-2\\UNIT-2-PROJECT\\GreenerSaudi\\main\\static\\img\\about-mgi.webp')
# print(score)

