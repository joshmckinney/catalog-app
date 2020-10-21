from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from create_database import Base, Category, Item, User

engine = create_engine('sqlite:///catalogapp.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy users
User0 = User(name="Officer Bricks", email="brickmenot@null.com",
             picture='https://randomuser.me/api/portraits/lego/0.jpg')
session.add(User0)
session.commit()
User1 = User(name="John Lego", email="johnlego@null.com",
             picture='https://randomuser.me/api/portraits/lego/1.jpg')
session.add(User1)
session.commit()
User2 = User(name="Mad Stacker", email="madstacker@null.com",
             picture='https://randomuser.me/api/portraits/lego/2.jpg')
session.add(User2)
session.commit()
User3 = User(name="Dr. Who", email="drwho@null.com",
             picture='https://randomuser.me/api/portraits/lego/3.jpg')
session.add(User3)
session.commit()
User4 = User(name="Knight o' Camelot", email="knightocamelot@null.com",
             picture='https://randomuser.me/api/portraits/lego/4.jpg')
session.add(User4)
session.commit()
User5 = User(name="James Duplo", email="jamesduplo@null.com",
             picture='https://randomuser.me/api/portraits/lego/5.jpg')
session.add(User5)
session.commit()
User6 = User(name="Juan Sr.", email="juansr@null.com",
             picture='https://randomuser.me/api/portraits/lego/6.jpg')
session.add(User6)
session.commit()
User7 = User(name="Builder Bob", email="bobthebuilder@null.com",
             picture='https://randomuser.me/api/portraits/lego/7.jpg')
session.add(User7)
session.commit()
User8 = User(name="Mr. Cooks So Good", email="yummyintummy@null.com",
             picture='https://randomuser.me/api/portraits/lego/8.jpg')
session.add(User8)
session.commit()
User9 = User(name="Jean Crusoe", email="crusoemenot@null.com",
             picture='https://randomuser.me/api/portraits/lego/9.jpg')
session.add(User9)
session.commit()

# Create dummy categories
category0 = Category(user_id=1, name="Crime Stats")
session.add(category0)
session.commit()
category1 = Category(user_id=2, name="Blogging")
session.add(category1)
session.commit()
category2 = Category(user_id=3, name="Anger Therapy")
session.add(category2)
session.commit()
category3 = Category(user_id=4, name="Who's Adventures")
session.add(category3)
session.commit()
category4 = Category(user_id=5, name="Round Table Etiquette")
session.add(category4)
session.commit()
category5 = Category(user_id=6, name="Martini Recipes")
session.add(category5)
session.commit()
category6 = Category(user_id=7, name="Holy Guacamole")
session.add(category6)
session.commit()
category7 = Category(user_id=8, name="Construction Times")
session.add(category7)
session.commit()
category8 = Category(user_id=9, name="Urban Chef")
session.add(category8)
session.commit()
category9 = Category(user_id=10, name="Feminism Today")
session.add(category9)
session.commit()

# Create dummy items
newitem0 = Item(user_id=0, name="Another Blunder",
                description="Crime at all time high, Joker still on the loose",
                category=category0)
session.add(newitem0)
session.commit()
newitem1 = Item(user_id=0, name="Super Heroes Wanted",
                description="Apply at the Police HQ.",
                category=category0)
session.add(newitem1)
session.commit()
newitem2 = Item(user_id=0, name="Question marks (?) tagged throughout city.",
                description="Some report sighting the joker...",
                category=category0)
session.add(newitem2)
session.commit()
newitem3 = Item(user_id=1, name="Going to Tahoe",
                description="Sun, snow and dirt! YEAH BRAH!",
                category=category1)
session.add(newitem3)
session.commit()
newitem4 = Item(user_id=1, name="Taking the best selfies",
                description="Gotta be making those ducklips fo sho.",
                category=category1)
session.add(newitem4)
session.commit()
newitem5 = Item(user_id=1, name="Internet Dating",
                description="Whens a good lego dude gonna catch the lady?",
                category=category1)
session.add(newitem5)
session.commit()
newitem6 = Item(user_id=2, name="Pieces Crashing",
                description="Building legos is like jenga.. don't get angry!",
                category=category2)
session.add(newitem6)
session.commit()
newitem7 = Item(user_id=2, name="Step on me one more time!",
                description="The most painful of foot injuries. This just in.",
                category=category2)
session.add(newitem7)
session.commit()
newitem8 = Item(user_id=2, name="Dealing with the high prices",
                description="Lego building prices sky rocket",
                category=category2)
session.add(newitem8)
session.commit()
newitem9 = Item(user_id=3, name="Time Traveling",
                description="Don't ask too many questions..",
                category=category3)
session.add(newitem9)
session.commit()
newitem10 = Item(user_id=3, name="Builds from another World",
                 description="Careful, your kit is filled with cyber-men.",
                 category=category3)
session.add(newitem10)
session.commit()
newitem11 = Item(user_id=3, name="Looking for Asst.",
                 description="Very adventurous partner no questions asked.",
                 category=category3)
session.add(newitem11)
session.commit()
newitem12 = Item(user_id=4, name="Tis a jolly time",
                 description="All those spirits yee be having, keep it in..",
                 category=category4)
session.add(newitem12)
session.commit()
newitem13 = Item(user_id=4, name="Horses",
                 description="Pile o' Dung does NOT make the world go round.",
                 category=category4)
session.add(newitem13)
session.commit()
newitem14 = Item(user_id=4, name="Monty Python",
                 description="What's the laiden speed of a swallow?",
                 category=category4)
session.add(newitem14)
session.commit()
newitem15 = Item(user_id=5, name="The Classics",
                 description="Tried, can't help staying shaken not stirred.",
                 category=category5)
session.add(newitem15)
session.commit()
newitem16 = Item(user_id=5, name="Drinking on the job",
                 description="Last we checked it's okay if the lady does it.",
                 category=category5)
session.add(newitem16)
session.commit()
newitem17 = Item(user_id=5, name="Not Spiked?",
                 description="Play a game? This ain't no Princess Bride!",
                 category=category5)
session.add(newitem17)
session.commit()
newitem18 = Item(user_id=6, name="The Key to Guacamole",
                 description="More jalepenos!! Fresh Ingredients..",
                 category=category6)
session.add(newitem18)
session.commit()
newitem19 = Item(user_id=6, name="Your travel destinations",
                 description="It's almost time to book your cruise!",
                 category=category6)
session.add(newitem19)
session.commit()
newitem20 = Item(user_id=6, name="Papi Jokes",
                 description="How'd they cut the pizza? With little Ceasars!",
                 category=category6)
session.add(newitem20)
session.commit()
newitem21 = Item(user_id=7, name="Strike for wages",
                 description="Getting paid in plastic gold won't cut it!",
                 category=category7)
session.add(newitem21)
session.commit()
newitem22 = Item(user_id=7, name="1 Found Dead at Job Site",
                 description="A body was found beneath the rubble",
                 category=category7)
session.add(newitem22)
session.commit()
newitem23 = Item(user_id=7, name="Yes We Can",
                 description="The pains of being too optimistic, what to do.",
                 category=category7)
session.add(newitem23)
session.commit()
newitem24 = Item(user_id=8, name="More Good Recipes",
                 description="Come on fattys! You know you'll want these..",
                 category=category8)
session.add(newitem24)
session.commit()
newitem25 = Item(user_id=8, name="Snake",
                 description="The other, other white meat!",
                 category=category8)
session.add(newitem25)
session.commit()
newitem26 = Item(user_id=8, name="Cooking outdoors",
                 description="Lego barbeques aren't doing so hot.",
                 category=category8)
session.add(newitem26)
session.commit()
newitem27 = Item(user_id=9, name="Ladies Meetup",
                 description="Inviting everyone to watch Wonder Woman",
                 category=category9)
session.add(newitem27)
session.commit()
newitem28 = Item(user_id=9, name="Demand Lego make more ladies clothing!",
                 description="Enough of those boy shirts already, gosh.",
                 category=category9)
session.add(newitem28)
session.commit()
newitem29 = Item(user_id=9, name="Girl Legos really shine",
                 description="We might not have spaceships but we have..",
                 category=category9)
session.add(newitem29)
session.commit()

print("Added Dummy Content!")
