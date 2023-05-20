from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today ?",]
    ],
    [
        r"(.*)help(.*) ",
        ["I can help you ",]
    ],
     [
        r"(.*) your name ?",
        ["My name is the Chiti, but you can just call me robot and I'm a chatbot .",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well", "i am great! Thank you"]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind that",]
    ],
    [
        r"i am (.*) (good|well|okay|ok)",
        ["Nice to hear that","Alright, great !",]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello", "Hey there",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],
    [
        r"(.*)created(.*)",
        [" Akshay created me using Python's NLTK library ","Akshay",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Nagpur (MH), India',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2","In %2 there is a 50% chance of rain",]
    ],
    [
        r"how (.*) your health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health ",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket",]
    ],
    [
        r"(.*)open google maps(.*)",
        ["Sorry ! i don't have access to open google maps",]
    ],
    [
        r"(.*) sing a song(.*)",
        ["Sorry ! i can't sing a song, but i always refer youtube",]
    ],
    [
        r"(.*) healthcare concept(.*)",
        ["Health care, or healthcare, is the improvement of health via the prevention, diagnosis, treatment, amelioration or cure of disease, illness, injury, and other physical and mental impairments in people. Health care is delivered by health professionals and allied health fields. Medicine, dentistry, pharmacy, midwifery, nursing, optometry, audiology, psychology, occupational therapy, physical therapy, athletic training, and other health professions all constitute health care. It includes work done in providing primary care, secondary care, and tertiary care, as well as in public health",]
    ],
    [
        r"(.*) code 777(.*)",
        ["For action code 775/776/777, first we need to check clinical grid, NPL list, then check for authorization ATV/MC, if found take action accordingly. If not then send to MPO for review.",]
    ],
    [
        r"(.*) codes required one year history (.*)",
        ["I would say history required for all J-codes (injection codes) and Q-codes. These codes required by default.",]
    ],
    [
        r"(.*) code 779(.*)",
        ["This is incidental issue, we need to do MPO prep and send to NCAU-Coding for review. ATV/MC not required for coding review.",]
    ],
    [
        r"(.*) to update ATV/MC (.*)",
        ["We have to raised Intake Tool request with add template for update ATV/MC, if update done then work accordingly. If not then misdirecting the case.",]
    ],
    [
        r"(.*) go Pune to Nagpur(.*)",
        ["You can go Pune to Nagpur through MSRTC Bus, Private Bus, Cab, Train and flight running everyday. We have International Airport in Nagpur. Happy Journey.",]
    ],
    [
        r"(.*) cities under Vidarbha (.*)",
        ["Here is the city names under Vidarbha Region. Situated in central India. The largest city in Vidarbha is Nagpur followed by Amravati. Nagpur, Amravati, Akola, Chandrapur, Yavatmal, Gondia, Wardha, Bhandara, Washim, Buldhana and Gadchiroli. 11 cities under Vidarbha Region.",]
    ],
    [
        r"(.*) Pune famous (.*)",
        ["Pune exemplifies an indigenous Marathi culture and ethos, in which education, arts and crafts, and theatres are given due prominence. It is the birthplace of the poet-saint Tukaram (in Dehu) and Jnaneshvara (in Alandi), the author of the well-known commentary 'Jnaneshwari',on the “Bhagavad Gita”.",]
    ],
    [
        r"(.*) Shivaji Maharaj(.*)",
        ["Chhatrapati Shivajiraje Bhosale ( 1630-1680 AD) was a great king and strategist of India who laid the foundation of the Maratha Empire in western India in 1674 AD. For this he fought with Aurangzeb, the ruler of the Mughal Empire. He was coronated in Raigarh in 1674 and became Chhatrapati. If a Tatvdarshi saint had been found, Shivajiraje would have chosen the path of salvation. Chhatrapati Shivaji Maharaj provided an able and progressive administration with the help of his disciplined army and well organized administrative units. He made many innovations in martial arts and developed a new style of guerrilla warfare ( Shivasutra ). He revived ancient Hindu political practices and court etiquette and made Marathi and Sanskrit the official languages. He started being remembered as a hero in the Indian freedom struggle. Bal Gangadhar Tilak started Shivajiraje Janmotsav for the development of the feeling of nationalism. Malojiraje Bhosale (1552–1597) was an influential general of the Ahmednagar Sultanate, Deshmukh of Pune Chakan and Indapur. Malojiraje's son Shahajiraje was also a very influential politician in the court of Vijapur Sultan. Shivaji was born to Shahaji Raje and his wife Jijabai .",]
    ],
    [
        r"(.*)hill stations in maharashtra(.*)",
        ["Lonavala,Khandala, Matheran, Mahabaleshwar, Igatpuri, Panchgani, Karjat, Lavasa",]
    ],
    [
        r"who (.*) (Cricketer|Batsman)?",
        ["M S Dhoni"]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :) ","It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ['Our customer service will reach out to you'] 
    ],
]


print(reflections)


my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
    }

print("Hi, I'm Chiti and I like to chat\nPlease type lowercase English language to start a conversation. Type quit to leave ")

chat = Chat(pairs, reflections)



chat.converse() 
