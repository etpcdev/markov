from markov import Tokenizer, ModelHandler, MarkovMachine

"""This file serves as an example for using the markov package."""

#Preparing an input (ideally read a file for this)
#Book Source: https://www.gutenberg.org/cache/epub/49010/pg49010.txt
txt = \
"""The Project Gutenberg eBook of Æsop's Fables: A Version for Young Readers

This ebook is for the use of anyone anywhere in the United States and
most other parts of the world at no cost and with almost no restrictions
whatsoever. You may copy it, give it away or re-use it under the terms
of the Project Gutenberg License included with this ebook or online
at www.gutenberg.org. If you are not located in the United States,
you will have to check the laws of the country where you are located
before using this eBook.

Title: Æsop's Fables: A Version for Young Readers

Author: J. H. Stickney
        Aesop

Illustrator: Charles Livingston Bull

Release date: May 21, 2015 [eBook #49010]

Language: English

Credits: Produced by Juliet Sutherland, Emmy and the Online
        Distributed Proofreading Team at http://www.pgdp.net


*** START OF THE PROJECT GUTENBERG EBOOK ÆSOP'S FABLES: 
A VERSION FOR YOUNG READERS ***

Produced by Juliet Sutherland, Emmy and the Online
Distributed Proofreading Team at http://www.pgdp.net

[Illustration: THE WOLF, THE FOX, AND THE APE

(See page 153)]

Æsop’s Fables

    A Version for
    Young Readers

    _By_
    J. H. Stickney

    Illustrated by
    Charles Livingston Bull

    Ginn and Company

    Boston—New York—Chicago—London
    Atlanta—Dallas—Columbus—San Francisco

[Illustration]

    COPYRIGHT, 1915, BY GINN AND COMPANY
    ALL RIGHTS RESERVED
    321.11


    THE Athenæum Press
    GINN AND COMPANY·PROPRIETORS·BOSTON·U.S.A.

PREFACE

THE good fortune which has attended the earlier edition of this book
is a proof that there is less occasion now than formerly to plead the
cause of fables for use in elementary schools. And yet their value
is still too little recognized. The homely wisdom, which the fables
represent so aptly, was a more common possession of intelligent people
of a generation or two ago than it is at the present time. It had
then a better chance of being passed on by natural tradition than
is now the case among the less homogeneous parentage of our school
children. And there has never been a greater need than now for the
kind of seed-sowing for character that is afforded by this means. As
in the troubled times in Greece in Æsop’s day, twenty-five centuries
ago, moral teaching to be salutary must be largely shorn of didactic
implications and veiled with wit and satire. This insures its most
vital working wherever its teaching is pertinent. To be whipped,
warned, shamed, or encouraged, and so corrected, over the heads of
animals as they are represented in the expression of their native
traits, is the least offensive way that can fall to a person’s lot.
Among several hundred episodes, knowledge of which is acquired in
childhood as a part of an educational routine, most conservative"""

#Tokenizing the input
tokens: list[str] = Tokenizer.tokenize_text(txt)

#Generating a model using the tokens
model: str = ModelHandler.generate_model(tokens=tokens, depth=3)

#Saving the model to a json file (Optional)
ModelHandler.export_model(model=model, path="./models/example_model.json")

#Initializing the markov text generator
mkv: MarkovMachine = MarkovMachine()

#Load a model from memory
mkv.load_model(model)

#Load a model from a json file
mkv.load_model_from_file("./models/example_model.json")

#Tokenizing a user input to start the machine with
my_text: list[str] = Tokenizer.tokenize_text(" a proof ")

#Printing the machine's output
print(mkv.generate_text(output_length=200, input_tokens=my_text))

