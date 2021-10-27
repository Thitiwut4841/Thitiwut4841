from logic import *

rain = Symbol("Rain")
alice = Symbol("Alice")
chale = Symbol("Chale")


knowledge = And(
    Implication(Not(rain), alice),
    Or(alice, chale),
    Not(And(alice, chale)),
    chale
)

print("Visited Chale? \n", model_check(knowledge, chale))

print("Visited today? \n", model_check(knowledge, rain))

print("Visited Alice? \n", model_check(knowledge, alice))