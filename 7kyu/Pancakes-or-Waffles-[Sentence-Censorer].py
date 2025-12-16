# The owner of a certain chatbox app has came under fire recently for
# a drama regarding the age old debate of pancakes or waffles. Because
# of this, he came to you in order to hide any words regarding pancakes.
#
# The following words are the words that he is looking to censor by
# replacing it with an equal amount of astricks (*):
#
# pancakes, flapjacks, slapjacks, hotcakes
#
# In conjunction to that, the following words shall be highlighted
# with a double astricks (**):
#
# waffles, crepes, blintzes
#
# Finally, as long as there is no mention of a waffle relating word in
# the sentence, also censor the following word unless, there is a
# waffle relating word then highlight it:
#
# syrup, honey, jam, butter, chocolate, margarine
#
# Examples:
#
# print(censor("I like waffles with chocolate")) --> "I like
# **waffles** with **chocolate**"
#
# print(censor("I like pancakes with syrup" --> "I like ******* with
# *****"
#
# print(censor("The debate between pancakes and waffles is as sweet as
# honey" --> "The debate between ******** and **waffles** is as sweet
# as **honey**"


import re


def censor(sentence):
    censor_words = {'pancakes', 'flapjacks', 'slapjacks', 'hotcakes'}
    waffle_words = {'waffles', 'crepes', 'blintzes'}
    extras = {'syrup', 'honey', 'jam', 'butter', 'chocolate', 'margarine'}
    has_waffle = any(re.search(rf'\b{w}\b', sentence) for w in waffle_words)
    def repl(m):
        word = m.group()
        lw = word.lower()

        if lw in censor_words:
            return '*' * len(word)
        if lw in waffle_words:
            return f'**{word}**'
        if lw in extras:
            return f'**{word}**' if has_waffle else '*' * len(word)
        return word
    return re.sub(r'\b[a-zA-Z]+\b', repl, sentence)


if __name__ == '__main__':
    print(censor('I like waffles'))


# Best solutions:


def censor(sentence):
    group1 = {'pancakes', 'flapjacks', 'slapjacks', 'hotcakes'}
    group2 = {'waffles', 'crepes', 'blintzes'}
    group3 = {'syrup', 'honey', 'jam', 'butter', 'chocolate',
              'margarine'}

    words = sentence.split()
    has_waffle = any(word in group2 for word in words)

    processed = []
    for word in words:
        if word.lower() in group1:
            processed.append('*' * len(word))
        elif word.lower() in group2:
            processed.append(f'**{word}**')
        elif word.lower() in group3:
            if has_waffle:
                processed.append(f'**{word}**')
            else:
                processed.append('*' * len(word))
        else:
            processed.append(word)
    return ' '.join(processed)


def censor(sentence):
    sent = sentence.split(' ')
    banned = {'pancakes', 'flapjacks', 'slapjacks', 'hotcakes'}
    highlight = {'waffles', 'crepes', 'blintzes'}
    spread = {'syrup', 'honey', 'jam', 'butter', 'chocolate', 'margarine'}

    if any(x.lower() in highlight for x in sent):
        sent = [f'**{x}**' if x.lower() in (highlight | spread) else x for x in sent]
    sent = ['*' * len(x) if x.lower() in (banned | spread) else x for x in sent]

    return ' '.join(sent)


import re
censor_word=lambda m:"*"*len(m.group(0))
highlight_word=lambda m:"**"+m.group(0)+"**"
def censor(sentence):
    sentence=re.sub(r'pancakes|flapjacks|slapjacks|hotcakes',censor_word,sentence,flags=re.IGNORECASE)
    sentence_waf=re.sub(r'waffles|crepes|blintzes',highlight_word,sentence,flags=re.IGNORECASE)
    mutate=censor_word if sentence==sentence_waf else highlight_word
    return re.sub(r'syrup|honey|jam|butter|chocolate|margarine',mutate,sentence_waf,flags=re.IGNORECASE)
