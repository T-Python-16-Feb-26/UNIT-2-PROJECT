import opennsfw2 as n2
from better_profanity import profanity

profanity.load_censor_words()
print(profanity.contains_profanity("hey how we doin"))
score = n2.predict_image('')
print(score)

