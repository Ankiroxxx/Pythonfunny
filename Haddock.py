import random
import time
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-300)
volume = engine.getProperty('volume')
engine.setProperty('volume', 1.0)
engine.setProperty('voice', voices[1].id)
a =  ["accapareur","aérolithe","amiral de bateau-lavoir","amphitryon","anacoluthe","analphabète","analphabète diplômé","animal","anthracite","anthropophage","anthropopithèque","apache","apophtegme","apprenti-dictateur à la noix de coco","arlequin","ascenseur","astronaute d'eau douce","athlète complet","autocrate","autodidacte","aztèques"]
bb = ["babouin","bachi-bouzouk","bachi-bouzouk de tonnerre de Brest","bachi-bouzouk des Carpathes","bande de jeunes effrontés","bande de joyeux drilles","bande d'ectoplasmes de tonnerre de Brest",\
    "bande d'emplâtres","bande d'enragés","bande d'escrocs","bande d'hurluberlus","bande de bachi-bouzouks","bande de brutes","bande de canaques","bande de Ku-Klux-Klans","bande de pirates","bande de sauvages","bande de voleurs","bande de zapotèques de tonnerre de Brest","bandit","bayadère de carnaval","bibelot","bibendum","bidule","blague, fumisterie et compagnie","boit-sans-soif","bombe atomique","bonhomme","bougre d'ectoplasme à roulettes","bougre d'ectoplasme de moule à gaufres","bougre d'amiral de bateau-lavoir","bougre de crème d'emplâtre à la graisse de hérisson","bougre d'extrait de cornichon","bougre d'extrait de crétin des Alpes","bougre d'extrait d'hydrocarbure","bougres de faux jetons à la sauce tartare","bougre de méchant Blanc","bougre de mouchard","bougre d'olibrius","bougre d\'ostrogoth","bougre de papou des Carpathes","bougre de petit cornichon","bougre de phénomène de tonnerre de Brest","bougre de phénomène de moule à gaufres de tonnerre de Brest","bougre de sauvage d'aérolithe de tonnerre de Brest","bougre de zouave","bougres de zouaves d'anthropopithèques","brigand","brontosaure","brute","bulldozer à réaction"]
cc = [
    "cachalot",
    "cake-walk",
    "calembredaine",
    "canaille",
    "canaque",
    "cannibale",
    "cannibale emplumé",
    "capitaine de bateau-lavoir",
    "casse-pieds",
    "catachrèse",
    "cataplasme",
    "cercopythèque",
    "cercueil volant",
    "chauffard",
    "chenapan",
    "choléra",
    "chouette mal empaillée",
    "chrysanthème",
    "cigare volant",
    "cloche à fromage",
    "cloporte",
    "clown",
    "clysopompe",
    "coléoptère",
    "coloquinte",
    "coloquinte à la graisse de hérisson",
    "concentré de moules à gaufres",
    "coquin",
    "cornemuse",
    "cornichon",
    "cornichon de zouave de tonnerre de Brest",
    "cornichon diplômé",
    "corsaire",
    "coup de Trafalgar",
    "coupe-jarret",
    "cow-boy de la route",
    "crème d'emplâtre à la graisse de hérisson",
    "crème d'emplâtre à la graisse de hérisson",
    "crème d'emplâtre à la graisse de hérisson",
    "crétin de l'Himalaya",
    "crétin des Alpes",
    "crétin des Balkans",
    "cro-magnon",
    "cuistre",
    "cyanure",
    "cyclone",
    "cyclone ambulant",
    "cyclotron",
    "cyrano à quatre pattes"
]
dd = [
    "diable",
    "diable de zouave",
    "diablesse",
    "dieu soit loué",
    "diplodocus",
    "doryphore",
    "doux agneaux",
    "dynamiteur"
]
e1 = [
    "ecornifleur",
    "écraseur",
    "ectoplasme",
    "ectoplasme à roulettes",
    "égoïste",
    "électron",
    "emplâtre",
    "emplâtré à la graisse de hérisson",
    "emplâtré à la graisse de hérisson",
    "emplâtré à la graisse de hérisson",
    "empoisonneur",
    "encordé",
    "énergumène",
    "enfonceur de porte ouverte",
    "enragé",
    "entêté",
    "épouvantail",
    "équilibriste",
    "esclavagiste",
    "escogriffe",
    "escroc",
    "extrait d'hydrocarbure",
    "extrait de cornichon"
]
e2 = [
    "espèce de loup-garou à la graisse de renoncule de mille sabords",
    "espèce de porc-épic mal embouché",
    "enfer et damnation",
]
f = [
    "face de brute",
    "farceur",
    "fatma de prisunic",
    "faux frère",
    "faux jeton",
    "faux jeton à la sauce tartare",
    "fichue espagnolette",
    "fichue fusée de tonnerre de Brest",
    "fieffé menteur",
    "fiston à son papa ouin ouin !!",
    "flibustier",
    "flibustier de carnaval",
    "flûte",
    "forban",
    "fourbe",
    "frère de la côte",
    "froussard"
]
g = [
    "gaillard",
    "galopin",
    "gamin",
    "gangster",
    "garde-côtes à la mie de pain",
    "gargarisme",
    "garnement",
    "gibier de potence",
    "goujat",
    "graine de vaurien",
    "graisse de hérisson",
    "graisse de trombone à coulisse",
    "grand escogriffe",
    "grand lâche",
    "gredin",
    "grenouille",
    "gros-plein-de-soupe",
    "grotesque polichinelle",
    "gyroscope"
]
h1 = [
    "hérétique",
    "hurluberlu",
    "hydrocarbure"
]
h2 = [
    "hors-la-loi"
]
ii = [
    "iconoclaste",
    "inca de carnaval",
    "individu de général de tonnerre de Brest",
    "invertébré",
    "isotope",
    "ivrogne",
]
j = [
    "jet d'eau ambulant",
    "jeune chenapan",
    "jeune impertinent",
    "jocrisse",
    "judas",
    "jus de réglisse"
]
k = [
    "khroumir",
    "krrtchmvrtz",
    "ku klux klan",
    "kanak"
]
l = [
    "lâche",
    "lascar",
    "lépidoptère",
    "logarithme",
    "loup-garou à la graisse de renoncule de mille tonnerres de Brest",
    "loup-garou à la graisse de renoncule de mille tonnerres de Brest"
]
m1 = [
    "maboul",
    "macaque",
    "macrocéphale",
    "malappris",
    "malheureux",
    "malotru",
    "mamelouk",
    "marchand de guano",
    "marchand de tapis",
    "marin d'eau douce",
    "marmotte male réveillée",
    "mazette",
    "mégacycle",
    "mégalomane",
    "mercanti",
    "mercenaire",
    "mérinos",
    "mérinos mal peignés",
    "migou de malheur",
    "misérable",
    "misérable ectoplasme",
    "misérable ver-de-terre",
    "mitrailleur à bavette",
    "moratorium",
    "moricaud",
    "morues dans un carton à chapeau",
    "mouchard",
    "moujik",
    "moule à gaufres",
    "moussaillon",
    "moussaillon de malheur",
    "moussaillon du diable",
    "mufle",
    "mrkrpxzkfmtfrz",
    "mussolini de carnaval"
]

n = [
    "naufrageur",
    "négrier",
    "noix de coco",
    "nyctalope"
]
m1 = [
    "maboul",
    "macaque",
    "macrocéphale",
    "malappris",
    "malheureux",
    "malotru",
    "mamelouk",
    "marchand de guano",
    "marchand de tapis",
    "marin d'eau douce",
    "marmotte male réveillée",
    "mazette",
    "mégacycle",
    "mégalomane",
    "mercanti",
    "mercenaire",
    "mérinos",
    "mérinos mal peignés",
    "migou de malheur",
    "misérable",
    "misérable ectoplasme",
    "misérable ver-de-terre",
    "mitrailleur à bavette",
    "moratorium",
    "moricaud",
    "morues dans un carton à chapeau",
    "mouchard",
    "moujik",
    "moule à gaufres",
    "moussaillon",
    "moussaillon de malheur",
    "moussaillon du diable",
    "mufle",
    "mrkrpxzkfmtfrz",
    "mussolini de carnaval"
]
m2 = [
    "mille milliards de mille millions de mille sabords",
    "mille milliards de mille sabords",
    "mille milliards de mille sabords de tonnerre de Brest",
    "mille milliards de tonnerre de Brest",
    "mille millions de mille milliards de mille sabords",
    "mille millions de mille milliards de mille sabords de tonnerre de Brest",
    "mille millions de mille sabords",
    "mille millions de mille sabords de tonnerre de Brest",
    "mille millions de sabords",
    "mille millions de tonnerre de Brest",
    "mille sabords",
    "mille tonnerres",
    "mille tonnerres de Brest",
    "I'm Monkey D. Luffy and I will become king of the pirates ",
    "I'm Monkey D. Luffy and I will become king of the pirates ",
    "I'm Monkey D. Luffy and I will become king of the pirates ",
    "I'm Monkey D. Luffy and I will become king of the pirates ",
    "Yee-ha",
    "Yee-ha",
    "Yee-ha"
]
o = [
    "olibrius",
    "ophicléide",
    "ornithorynque",
    "oryctérope",
    "ostrogoth",
    "ours mal léché"
]
p = [
    "pachyderme",
    "pacte à quatre",
    "paltoquet",
    "pantoufle",
    "papou",
    "papou des carpathes",
    "paranoïaques",
    "parasites",
    "patagon",
    "patagon de zoulou",
    "patapouf",
    "patate",
    "pauvre bougre",
    "pauvre type",
    "peau-rouge",
    "pénultième",
    "père volant",
    "péronnelle",
    "perruche bavarde",
    "perroquet déplumé",
    "petit choléra",
    "petit délicat",
    "petit ornithorynque",
    "petite tigresse",
    "petit vaurien",
    "phénomène",
    "phlébotome",
    "phylactère",
    "phylloxéra",
    "pignouf",
    "pirate",
    "pirate d'eau douce",
    "pirate du ciel",
    "plein de dos",
    "pleurnichard",
    "polichinelle",
    "polygraphe",
    "porc-épic mal embouché",
    "potentat",
    "poussière",
    "profiteur",
    "projectile guidé",
    "protozoaire",
    "pyromane",
    "pyrophore"
]
q = [
    "que diable",
    "que le grand cric me croque et me fasse avaler ma barbe"
]
r = [
    "rapace",
    "rat",
    "ravachol",
    "renégat",
    "rhizopode",
    "rocaille de tonnerre de Brest",
    "rocambole"
]
s = [
    "sacré mitrailleur à bavette",
    "sacripant",
    "sajou",
    "sale bête",
    "saleté d'appareil à sous",
    "sale vilaine bête de tonnerre de Brest",
    "saltimbanque",
    "sapajou",
    "sapristi",
    "satanée fusée de tonnerre de Brest",
    "satanée marche",
    "satanée fenêtre",
    "satrape",
    "sauvage",
    "sauvage d'aérolithe",
    "scaphandrier d'eau de vaisselle",
    "scélérat",
    "schizophrène",
    "scolopendre",
    "scorpion",
    "serpent",
    "simili-martien à la graisse de cabestan",
    "sinapisme",
    "sinistre farceur",
    "sombre brute",
    "sombre oryctérope",
    "soulographe",
    "sous-produit d'ectoplasme"
]
t = [
    "tas de cornichons",
    "tas de sauvages",
    "tchouk-tchouk-nougat",
    "technocrate",
    "terroriste",
    "tête de lard",
    "tête de mule",
    "têtu comme une mule",
    "tigresse",
    "tonnerre",
    "tonnerre de brest",
    "tonnerre de tonnerre de brest",
    "topinambour",
    "tortionnaire",
    "trafiquant de chair humaine",
    "traîne-potence",
    "traître",
    "tricheur",
    "troglodyte",
    "trompe-la-mort",
    "troufignol"
]
v = [
    "vampire",
    "vandale",
    "va-nu-pieds",
    "vaurien",
    "végétarien",
    "ver-de-terre",
    "vercingétorix de carnaval",
    "vermicelles",
    "vermine",
    "vieille baderne",
    "vieille branche",
    "vieille coque rouillée",
    "vieille marmotte",
    "vieille perruche bavarde",
    "vieux farceur",
    "vieux frère",
    "vieux rafiot que je suis",
    "vipère",
    "vivisectionniste",
    "volatile de malheur",
    "voleur",
    "voleur d'enfants"
]
w = [
    "wisigoths"
]
z = [
    "zapothèques",
    "zèbre",
    "zigomar",
    "zouave",
    "zouave interplanétaire",
    "zouave à la noix de coco",
    "zoulou"
]

c = input("Combien de jurons veux-tu ? ")
d = int(c)
for i in range(0, d):
    b = random.randint(1, len(a)+len(bb))
    sele = random.randint(1, 27)
    if sele == 2:
        b = random.randint(0, len(bb)-1)
        y = ("espèce de " + bb[b]+ "!")
        print(y)
    if sele == 1:
        b = random.randint(0, (len(a)-1))
        y = ("espèce d'" + a[b]+ "!")
        print(y)
    if sele == 3:
        b = random.randint(0, len(cc)-1)
        y = ("espèce de " + cc[b]+ "!")
        print(y)
    if sele == 4:
        b = random.randint(0, len(dd)-1)
        y = ("espèce de " + dd[b]+ "!")
        print(y)
    if sele == 5:
        b = random.randint(0, (len(e1)-1))
        y = ("espèce d'" + e1[b]+ "!")
        print(y)
    if sele == 6:
        b = random.randint(0, 1)
        y = (e2[b]+ "!")
        print(y)
    if sele == 7:
        b = random.randint(0, (len(f)-1))
        y = ("espèce de " + f[b]+ "!")
        print(y)
    if sele == 8:
        b = random.randint(0, (len(g)-1))
        y = ("espèce de " + g[b]+ "!")
        print(y)
    if sele == 9:
        b = random.randint(0, (len(h1)-1))
        y = ("espèce d'" + h1[b]+ "!")
        print(y)
    if sele == 10:
        b = random.randint(0, (len(h2)-1))
        y = ("espèce de " + h2[b]+ "!")
        print(y)
    if sele == 11:
        b = random.randint(0, (len(ii)-1))
        y = ("espèce d'" + ii[b]+ "!")
        print(y)
    if sele == 12:
        b = random.randint(0, (len(j)-1))
        y = ("espèce de " + j[b]+ "!")
        print(y)
    if sele == 13:
        b = random.randint(0, (len(k)-1))
        y = ("espèce de " + k[b]+ "!")
        print(y)
    if sele == 14:
        b = random.randint(0, (len(l)-1))
        y = ("espèce de " + l[b]+ "!")
        print(y)
    if sele == 15:
        b = random.randint(0, (len(m1)-1))
        y = ("espèce de " + m1[b]+ "!")
        print(y)
    if sele == 16:
        b = random.randint(0, (len(m2)-1))
        y = (m2[b]+ "!")
        print(y)
    if sele == 17:
        b = random.randint(0, (len(n)-1))
        y = ("espèce de " + n[b]+ "!")
        print(y)
    if sele == 18:
        b = random.randint(0, (len(o)-1))
        y = ("espèce d'" + o[b]+ "!")
        print(y)
    if sele == 19:
        b = random.randint(0, (len(p)-1))
        y = ("espèce de " + p[b]+ "!")
        print(y)
    if sele == 20:
        b = random.randint(0, (len(q)-1))
        y = (q[b]+ "!")
        print(y)
    if sele == 21:
        b = random.randint(0, (len(r)-1))
        y = ("espèce de " + r[b]+ "!")
        print(y)
    if sele == 22:
        b = random.randint(0, (len(s)-1))
        y = (s[b]+ "!")
        print(y)
    if sele == 23:
        b = random.randint(0, (len(t)-1))
        y = ("espèce de " + t[b]+ "!")
        print(y)
    if sele == 24:
        b = random.randint(0, (len(v)-1))
        y = ("espèce de " + v[b]+ "!")
        print(y)
    if sele == 25:
        b = random.randint(0, (len(w)-1))
        y = ("espèces de " + w[b]+ "!")
        print(y)
    if sele == 26:
        b = random.randint(0, (len(z)-1))
        y = ("espèce de " + z[b]+ "!")
        print(y)
    if sele == 27:
        b = random.randint(0, (len(m2)-1))
        y = (m2[b]+ "!")
        print(y)
    engine.say(y)
    engine.runAndWait()