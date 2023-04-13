# AI Edtech with ChatGPT and BERT

### Advances in AI technology have made it easier than ever for teachers like myself to streamline their techniques for making pedagogical content. In this project I used ChatGPT and a BERT model to generate longform multiple choice questions from a list of topics.

## Here's how we instantiate the class:

```
from longform import *

tokenizer_name = 'bert-base-cased'
model_name = 'bert-base-cased'

QuestionGenerator = Longform(tokenizer_name, model_name)
```

## Here's how we generate customizable output. I chose the topics of Japan, unicorns, and oak trees.

```
topics = ['the history of Japan',
            'unicorns',
            'oak trees']

save = True
ans_path='../data/answers.txt'
question_path='../data/questions.txt'
top_k=2000 ## Size of pool of alternative words to choose from, higher number == more choices
offset=500 ## Higher offset => how different words are from the actual answer
top_words=10 ## Number of words to be removed in text
choices=5 ## Number of alternative words in answer

QuestionGenerator.generate_longform_questions(topics, save, ans_path, question_path, top_k, offset, top_words, choices)
```

# Here's the Output

```
AI GENERATED QUESTIONS

QUESTION #1
```

`From its origins as a tribe of hunter-gatherers some 30,000 years ago to the modern (1)____________ giant it is today, Japan has an extensive and interesting history. The country has (2)____________ dramatic Sino-Japanese wars, powerful (3)____________ rulers, and (4)____________ disasters. Over the centuries, Japan's rich culture and history have produced a wealth of literature, art, and music that continues to influence the world to this day. The earliest recorded Japanese culture is known as Jōmon (縄文) and is believed to have begun around 10,000 B. C. During this period, Japan's inhabitants followed a hunter-gatherer lifestyle, producing clay pottery and making use of dogs for hunting and transportation. By the 3rd century B. C. , Jōmon culture had evolved into three distinct (5)____________ groups; the Yayoi people of Kyushu and Honshu, the Emishi of Northern Honshu and Tohoku, and the Ainu of Hokkaido and Northern Honshu. The eighth century saw many changes in Japan. In an effort to strengthen their growing presence on the mainland, the Yamato people (安宅) formed a (6)____________ government, the Imperial Court of Japan, and adopted a variety of Chinese (7)____________ as their own. This period, known as the Nara Period, saw rapid growth and development of a unique Japanese culture and language. The Ninth century saw the emergence of powerful regional warlords who controlled the country. This period, known as the Heian Period, lasted until 1185, when the Minamoto clan established the first samurai-led military government, known as the Kamakura Shogunate. The shogunate system provided a stable central government and laid the groundwork for the growth of samurai culture, which reached its peak in the Edo Period (1603-1867). This period saw the flourishing of art, literature, and famously the practice of Zen Buddhism. The Meiji Restoration of 1868 initiated a period of modernization and Westernization of Japan. This period saw the introduction of new commodities and technologies, such as railroads and telegraphs, and saw Japan quickly become a powerful nation. In the (8)____________ century, Japan experienced rapid growth, which came to an end with its defeat in World War II, and subsequently the economic (9)____________ of the post-war years. Today, Japan is one of the world’s most advanced countries, being home to world-renowned shopping, entertainment, technology, and tourism industries. Japan’s unique culture and deep-rooted history remain (10)____________ and continue to be a strong source for the country’s identity and the pride of its people.`

```
1.
A. metro
B. free
C. possible
D. technological
E. swamp
F. pack

2.
A. before
B. witnessed
C. easily
D. possesses
E. processed
F. recounted

3.
A. State
B. uneven
C. highway
D. resentment
E. feudal
F. judicial

4.
A. weird
B. devastating
C. Communist
D. southern
E. Philippine
F. leading

5.
A. open
B. tribal
C. tooth
D. named
E. arms
F. educational

6.
A. Nanjing
B. intermediate
C. blank
D. woman
E. centralized
F. treasury

7.
A. Emperor
B. furnishings
C. noble
D. customs
E. font
F. Indonesian

8.
A. ant
B. crime
C. stopped
D. pattern
E. did
F. twentieth

9.
A. heating
B. initiatives
C. boom
D. rulers
E. sink
F. crashing

10.
A. endless
B. inheritance
C. interdisciplinary
D. intact
E. cooperative
F. when

QUESTION #2
```

`Unicorns have been part of history, folklore, and (1)____________ for centuries, and remain a part of the (2)____________ today. The idea of a (3)____________ creature with a horn on its forehead is so delightful that it has caused great controversy and debate over whether the unicorn actually exists. Regardless of whether or not the existence of unicorns can be proved, the idea of them has been regaled and steeped in (4)____________ stories throughout the ages. Most accounts describe unicorns as having a white or dark colored body, a long (5)____________ horn on their head, and cloven hooves. Legends and (6)____________ often depict them as wise creatures that were only ever seen by innocent children or virgins and that quelled wild animals with their mere presence. They were seen as symbols of innocence, healing, and purity, with the ability to grant wishes to righteous seekers. Unicorns have been mentioned in Greek mythology, Indian and Chinese literature, and in the Bible. Most famously, however, is the unicorn’s (7)____________ in European folklore. Here, stories about the famous horned animals and their magical abilities are plentiful and varied. In some, the unicorn symbolized great strength, power, and faithfulness. In others, unicorns were flights of fancy that both enchanted and terrified; it was said that to behold one was like looking into a mirror and finding that all your secrets were revealed. In the modern world, unicorns often represent all that is good and beautiful in the world, providing a wonderful escape from the often harsh realities of life. Whether they are depicted as magical, powerful steeds or sweet, gentle animals, their fantasy (8)____________ and unique features capture the imagination and bring smiles to faces everywhere. It is impossible to definitively prove the existence of unicorns, but the idea that such a creature could possibly exist, even for a brief moment or on a remote, hidden, magical world, is something that draws many people in. Whether unicorn-lovers are starry-eyed romantics, obsessed collectors, or die-hard storytellers, the nostalgia, romanticism, and mythos associated with these animals make them an enduring part of our psyche.`

```
1.
A. imaging
B. friends
C. arms
D. mythology
E. radiation
F. pop

2.
A. flavor
B. laboratory
C. band
D. imagination
E. flower
F. sunlight

3.
A. teenage
B. neck
C. Scottish
D. mythical
E. swirling
F. symmetrical

4.
A. quest
B. fantastic
C. rogue
D. noir
E. inside
F. skull

5.
A. traveling
B. needle
C. spiral
D. from
E. bleeding
F. trick

6.
A. gestures
B. folklore
C. activists
D. immigrants
E. romantic
F. mankind

7.
A. depiction
B. ingredient
C. match
D. flock
E. stone
F. writing

8.
A. turrets
B. nods
C. talents
D. routes
E. wit
F. advent


QUESTION #3
```

`Oak trees hold a special place in human imagination, with their strength and roots deeply connected to the Earth. They are one of the most (1)____________ and celebrated trees in the world, with many cultural and spiritual connections across different societies. Oaks are known for their unusual and impressive strength, with massive (2)____________ and branches stretching (3)____________ of thousands of feet. The iconic shape and (4)____________ of an oak tree are unique, with a strong core surrounded by deep, jagged ridges. The oak tree has a long and varied history, with various symbolic and religious (5)____________ attached to its wood and acorns. In Greek and Roman mythology, oak trees are seen as symbols of strength, truth, and wisdom. The Celtic Druids attached great spiritual significance to the oak, believing it to be the axis around which the universe moves. In Christianity, the oak is seen as a symbol of God’s power and protection. This association has been long-standing, as did trees are recorded as being planted near churches in the Middle Ages. Despite its (6)____________ in (7)____________ and religion, oak trees have also been used for real-world, practical applications. Its strong, durable wood has been used to construct ship hulls and build homes overseas, helping to enable exploration and facilitate trade. Oaks are also well-known for the valuable acorns that they produce. For centuries, acorns have been collected and used to feed hogs and cattle, as well as to produce flour, starch, and medicines. Oak trees are truly remarkable specimens and have been of great benefit to human civilization. They have been vilified in some folklore, but also treasured in (8)____________ other stories. From offering nourishment and spiritual guidance, to being used as building materials, oaks are one of the oldest and most important trees around. As much now as in the past, oaks play a valuable role in enriching and (9)____________ human life.`

```
1.
A. recognizable
B. surrounding
C. palm
D. shaped
E. affecting
F. emphasized

2.
A. posture
B. Plants
C. holdings
D. trunks
E. Windows
F. construct

3.
A. mankind
B. talents
C. avenue
D. upwards
E. ones
F. genres

4.
A. people
B. brass
C. veil
D. texture
E. representations
F. timing

5.
A. meanings
B. fears
C. heirs
D. link
E. approaches
F. was

6.
A. task
B. shows
C. minorities
D. youth
E. prevalence
F. plantation

7.
A. conferences
B. folklore
C. Sociology
D. circles
E. images
F. nationality

8.
A. construction
B. recognition
C. Other
D. countless
E. cross
F. loosely

9.
A. profitable
B. poetic
C. strengthening
D. elegant
E. terrified
F. recognizable
```

## Conclusions

### As a somewhat lazy teacher, this tool allows me to create vocabulary-builing reading activities for my students with ease. Give it a try!
