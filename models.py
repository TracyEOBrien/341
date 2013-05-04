from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://' + 'username:password' + '@' +
        'localhost/databasename')

Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

class Recipe(Base):
    __tablename__ = "tblRecipe"
    rid = Column(Integer, primary_key=True)
    url = Column(String(60))
    description = Column(String(260))
    name = Column(String(60))
    
class IngredientGroup(Base):
    __tablename__ = "tblIngredientGroup"
    gid = Column(Integer, primary_key=True)
    groupname = Column(String(60))

class Ingredient(Base):
    __tablename__ = "tblIngredient"
    iid = Column(Integer, primary_key=True)
    name = Column(String(20))

class Contains(Base):
    __tablename__ = "tblContains"
    iid = Column(Integer, ForeignKey("IngredientGroup.iid"))
    rid = Column(Integer, ForeignKey("Recipe.rid"))

class GroupContains(Base):
    __tablename__ = "tblGroupContains"
    gcid = Column(Integer, primary_key=true)
    gid = Column(Integer, ForeignKey("Recipe.gid"))
    iid = Column(Integer, ForeignKey("IngredientGroup.iid"))
    
