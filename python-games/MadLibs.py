words = []
def get_words():
    person = words.append(input("Give me a noun: "))
    place = words.append(input("Give me a place: "))
    body_part = words.append(input("Give me the name of a body part: "))
    action = words.append(input("Give me a verb: "))
    adjective = words.append(input("Give me an adjective: "))
    animal = words.append(input("Give me an animal: "))
    adjective_1 = words.append(input("Give me a adjective: "))
def fill_words():
    madlib = f'\nDear, {words[0]}\nI am having a great time in {words[1]}. Yesterday I injured my {words[2]}. \nI hope that you can make it out to see me {words[3]}.\n All my friends tell me that i am {words[4]}. My {words[5]} ran away yesterday.\nI am just feeling so {words[6]} about that.\n'
    print(madlib)
def main():
    get_words()
    fill_words()
main()
