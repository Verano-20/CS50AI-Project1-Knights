from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnight, AKnave), # A is a knight or a knave
    Not(And(AKnight, AKnave)), # A is not a knight and a knave
    Implication(AKnight, And(AKnight, AKnave)), # If A is a knight, implies A is a knight and a knave
    Implication(AKnave, Not(And(AKnave, AKnight))) # If A is a knave, implies A is not a knight and a knave
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave), # A is a knight or a knave
    Not(And(AKnight, AKnave)), # A is not a knight and a knave
    Or(BKnight, BKnave), # B is a knight or a knave
    Not(And(BKnight, BKnave)), # B is not a knight and a knave
    Implication(AKnight, And(AKnave, BKnave)), # If A is a knight, A and B are both knaves
    Implication(AKnave, Not(And(AKnave, BKnave))) # If A is a knave, A and B are not both knaves
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave), # A is a knight or a knave
    Not(And(AKnight, AKnave)), # A is not a knight and a knave
    Or(BKnight, BKnave), # B is a knight or a knave
    Not(And(BKnight, BKnave)), # B is not a knight and a knave
  
    # If A is a knight, implies A and B are the same. If A is a knave, implies A and B are different
    Implication(AKnight, Or(Biconditional(AKnight, BKnight), Biconditional(AKnave, BKnave))),
    Implication(AKnave, Or(Biconditional(AKnave, BKnight), Biconditional(AKnight, BKnave))),

    # If B is a knight, implies A and B are different. If B is a knave, implies A and B are the same
    Implication(BKnight, Or(Biconditional(AKnight, BKnave), Biconditional(AKnave, BKnight))),
    Implication(BKnave, Or(Biconditional(AKnight, BKnight), Biconditional(AKnave, BKnave)))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(

    Or(AKnight, AKnave), # A is a knight or a knave
    Not(And(AKnight, AKnave)), # A is not a knight and a knave
    Or(BKnight, BKnave), # B is a knight or a knave
    Not(And(BKnight, BKnave)), # B is not a knight and a knave
    Or(CKnight, CKnave), # C is a knight or a knave
    Not(And(CKnight, CKnave)), # C is not a knight and a knave

    # AKnight implies either AKnight or AKnave
    Implication(AKnight, Or(AKnight, AKnave)),
    # AKnave implies either Not(AKnight) or Not(AKnave)
    Implication(AKnave, Or(Not(AKnight), Not(AKnave))),

    # BKnight implies either AKnight implies AKnave or AKnave implies Not(AKnave)
    Implication(BKnight, And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave)))),
    # BKnave implies either AKnight does not imply AKnave or AKnave does not imply not AKnave
    Implication(BKnave, Not(And(Implication(AKnight, AKnave), Implication(AKnave, Not(AKnave))))),

    # BKnight implies CKnave
    Implication(BKnight, CKnave),
    # BKnave imples not(CKnave)
    Implication(BKnave, Not(CKnave)),

    # CKnight implies AKnight
    Implication(CKnight, AKnight),
    # CKnave implies not(AKnight)
    Implication(CKnave, Not(AKnight))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
