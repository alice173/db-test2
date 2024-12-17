from sqlalchemy import(
  create_engine, Column, Integer, Float, String, ForeignKey
)

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# executing instructions from localhost 'chinook' db

db = create_engine("postgresql:///chinook")

base = declarative_base()

# create a class based model for the "programmer" table
class Programmer(base):
  __tablename__ = "Programmer"

  id = Column(Integer, primary_key=True)
  first_name = Column(String)
  last_name = Column(String)
  gender = Column(String)
  nationality = Column(String)
  famous_for = Column(String)

  

# instead of connecting to the database directly, we will ask for a session
# create a new instance of sessionmaker, then point to our engine (the db)
Session = sessionmaker(db)
# opens an actual session by calling the Session() subclass defined above
session = Session()

#creating the db using declarative_base subclass

base.metadata.create_all(db)

#create records on our Programmer table

ada_lovelace = Programmer(
  first_name = "Ada",
  last_name = "Lovelace",
  gender = "Female",
  nationality = "British",
  famous_for = "First Programmer")

#add each instance of our programmers to our session

session.add(ada_lovelace)

# commit our session to the database
session.commit()