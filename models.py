from django.db import models

class Recipe(models.Model):
    __tablename__ = "tblRecipe"
    rid = models.IntegerField()
    url = models.CharField(max_length=260)
    description = models.CharField(max_length=260)
    name = models.CharField(max_length=60)
    
class IngredientGroup(models.Model):
    __tablename__ = "tblIngredientGroup"
    gid = models.CharField(max_length=60,primary_key=True)
    groupname = models.CharField(max_length=60)

class Ingredient(models.Model):
    __tablename__ = "tblIngredient"
    iid = models.CharField(max_length=60,primary_key=True)
    name = models.CharField(max_length=60)

class Contains(models.Model):
    __tablename__ = "tblContains"
    iid = models.ForeignKey(IngredientGroup.iid))
    rid = models.ForeignKey(Recipe.rid))

class GroupContains(models.Model):
    __tablename__ = "tblGroupContains"
    gid = models.ForeignKey(Recipe.gid))
    iid = models.ForeignKey(IngredientGroup))
    
