from flask_sqlalchemy import SQLAlchemy
import logging as lg
import enum

from .views import app

db = SQLAlchemy(app)


class Gender(enum.Enum):
    female = 0
    male = 1
    other = 2
    undefined = 2


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    gender = db.Column(db.Enum(Gender), nullable=False)

    def __init__(self, description, gender):
        self.description = description
        self.gender = gender


def init_db():
    db.drop_all()
    db.create_all()
    db.session.add(Content("Iron Man _-_ Tony Stark est un phénomène de génie scientifique et un inventeur exceptionnel, principalement grâce à ses tissus neuraux qui parcourent son corps, qui développent son intelligence et donne à son corps de fantastiques capacités régénératrices. Sa bio-armure bactérienne se fixe à son corps comme une seconde peau, développe sa résistance et inhibe ses douleurs neurologiques chroniques. Il est multilingue, a une excellente mémoire et a une capacité quasiment sans limites pour faire plusieurs tâches en même temps. _-_ http://www.marvel-world.com/encyclopedie-266-fiche-iron-man-ultimate-biographie.html", Gender['male']))
    db.session.add(Content("Captain America _-_ Génie tactique et stratégique. Sait manipuler de nombreuses armes, et maîtrises de nombreuses formes de combat au corps à corps. Sait conduire un certain nombre de véhicules militaires, dont un avion de chasse moderne. _-_ http://www.marvel-world.com/encyclopedie-532-fiche-captain-america-ultimate-biographie.html", Gender['male']))
    db.session.add(Content("Hulk _-_  Le stress ou l’adrénaline déclenchent la transformation en Hulk. Sous cet état, il dispose d’une force et d’une endurance surhumaines, peut guérir à grande vitesse, et est capable de sauts de grande distance. A l’heure actuelle, il semblerait que Hulk dispose d’une intelligence au moins normale. _-_ http://www.marvel-world.com/encyclopedie-947-fiche-hulk-ultimate-biographie.html", Gender['male']))
    db.session.add(Content("Black Widow _-_ Black Widow est une experte en arts martiaux, une tireuse d'élite, une actrice naturelle, une redoutable séductrice, des talents qui font d’elle une espionne hors du commun.  _-_ http://www.marvel-world.com/encyclopedie-513-fiche-black-widow-romanova-ultimate-biographie.html", Gender['female']))
    db.session.add(Content("Scarlet Witch _-_ La Sorcière rouge possède de considérables connaissances dans les domaines occultes et mystiques, acquises surtout auprès d’Agatha Harkness et du Dr Strange, même si elle a bénéficié de moins d’entraînement mystique formel qu’il est habituellement nécessaire de suivre pour atteindre de hauts niveaux de puissance magique. Wanda s’est aussi entraînée de manière intensive dans les techniques de combats à mains nues et les tactiques et stratégies de batailles avec ses coéquipiers des Avengers et notamment Captain América, Hawkeye et l’USAgent (John Walker) ; elle a ainsi acquis une solide formation et expérience et s’est révélé être un chef d’équipe compétent quand elle a été à la tête des Avengers ou de Force Works. Elle a aussi des années d’expérience dans le pilotage des quinjets des Avengers, ou d’appareils similaires utilisés par les Avengers. Wanda est également une cavalière expérimentée et une bonne conductrice. Elle parle plusieurs langues, souvent acquises lors de ses errances en Europe durant son adolescence, et parle couramment anglais et français. Elle est aussi une bonne danseuse, formée par sa famille adoptive durant son enfance au style de danses tziganes. _-_ http://www.marvel-world.com/encyclopedie-64-fiche-sorciere-rouge-la-biographie.html", Gender['female']))
    db.session.add(Content("Gamora _-_ Gamora est une excellente combattante et maîtrise d’innombrables techniques de combats, aussi bien à mains nues qu’avec des armes blanches ou des armes à feu ; en fait, elle maîtrise l’ensemble des techniques développées dans la Voie lactée et figure parmi les meilleures pratiquantes des arts martiaux de la galaxie. Ses compétences techniques lui permettent de triompher d’adversaires physiquement plus puissants ou plus nombreux ; ainsi Gamora a prouvé être capable de vaincre un bataillon militaire de plusieurs douzaines de soldats en l’espace de quelques minutes. Elle connaît également les points vitaux sur lesquels appuyer pour paralyser ou tuer un ennemi d’un seul coup. _-_ http://www.marvel-world.com/encyclopedie-578-fiche-gamora-biographie.html", Gender['female']))
    db.session.add(Content("Venom _-_ A la base , Brock est un athlète très endurant et musclé, une fois que le symbiote prend possession de son corps (physiquement) , il est capable de soulever et presser 12 tonnes , il resite a tous types de blessures, et possède une puissante capacité de regénération, il ne craint pas les balles, il peut les absorber comme tous types de metal, et les reprojeter sur ses adversaires .Il est également doté une adherence a tous types de parois, ce qui lui permet de grimper aux murs et aux plafonds.Il peut aussi se rendre presque invisible, en se fondant dans le décor , il détient egalement un 6 ème sens l'avertissant du danger.Il peut projeter des toiles organiques , très résistantes pouvant se propager jusqu'a 30 mètres. Le symbiote et son hote partagent le meme corps en permanence, l'esprit de brock est toujours présent lors des combats, pour limiter les degats , cependant une fois en mauvaise posture Eddie peut laisser le total controle au symbiote , pour ainsi entrer dans un état de furie provisoire augmentant , sa force ainsi que tous le reste de ses capacités. _-_ https://marvel-arena.forumsrpg.com/t544-psychopathe-simbiotique-a-k-a-venom", Gender['other']))
    db.session.add(Content("Phoenix _-_ La Force Phénix est une manifestation immortelle, indestructible et mutable de la force vitale primaire de l’univers, dérivant des psychés de tous les êtres vivants. Sous sa forme naturelle, le cycle de vie en cours est suffisant pour entretenir la Force. Cependant, afin de se manifester elle-même sur le plan physique, la Force doit puiser dans la source d’énergie presque illimitée qui est fournie par la force vitale réservée aux générations futures, empêchant ainsi celles-ci d’exister. La Force Phénix peut manipuler cet énergie pour projeter des rayons d’une immense force de concussion, ainsi que se déplacer à travers le temps et l’espace en repliant ces énergies en elle-même, provoquant leur effondrement, d’une manière semblable à un trou noir, puis en se reformant dès qu’elle a atteint sa destination, comme le Phénix des légendes de la Terre. Quand il possède un hôte humain, la Force Phénix est capable d’accroître n’importe quel pouvoir surhumain jusqu’à des niveaux extrêmement élevés et puissants. _-_ http://www.marvel-world.com/encyclopedie-1131-fiche-force-phenix-la-biographie.html", Gender['other']))
    db.session.add(Content("Mystique _-_ Mystique est une excellente combattante au corps à corps et à l'arme blanche pouvant rivaliser avec Captain America (Steve Rogers) et Black Widow (Natasha Romanova). C'est une grande stratège et elle a l'habitude de préparer des missions commando ou terroristes. C'est une excellente actrice et elle parle couramment au moins 11 langues dont : l'anglais, l'allemand, le portugais, le suédois, l'espagnol, le français, le farsi et le tchèque. Elle est également une grande hypnotiseuse capable de s’auto-hypnotiser pour tromper jusqu’aux plus grands télépathes. _-_ http://www.marvel-world.com/encyclopedie-202-fiche-mystique-biographie.html", Gender['other']))
    db.session.commit()
    lg.warning('Database initialized!')
