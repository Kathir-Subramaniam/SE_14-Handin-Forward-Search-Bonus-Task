
from copy import deepcopy
from tabnanny import check
from turtle import right
from logic.conjunction import And
from logic.disjunction import Or
from logic.biconditional import Biconditional
from logic.implication import Implication
from logic.negation import Not


def is_in(knowledge, query):
    for conjunct in knowledge.conjuncts:
        if conjunct.is_same(query):
            return True
    return False

def check_proven(knowledge, query):
    """
        checks whether the query is currently proven or disproven in the knowledge base.

        returns:
        - True: if the query is contained
        - False: if the negation of the query is contained.
        - None: else
    """
    if is_in(knowledge,query):
        return True
    elif is_in(knowledge,Not(query)):
        return False
    else:
        None

def get_inferrable_knowledge(knowledge):
    """
        Takes a knowledge base and finds all sentences that can be inferred.

        returns a list of sentences that can be inferred from the knowlede base.
    """
    inferrable_knowledge = []
    for sentence in knowledge.conjuncts:
        if type(sentence) is And:
            if is_in(knowledge, sentence.conjuncts[0]) and not is_in(knowledge, sentence.conjuncts[1]):
                print(f"And: {sentence.conjuncts}")
                inferrable_knowledge.append(sentence.conjuncts[1])
            if not is_in(knowledge, sentence.conjuncts[0]) and is_in(knowledge, sentence.conjuncts[1]):
                inferrable_knowledge.append(sentence.conjuncts[0])  
        if type(sentence) is Or:
            if (is_in(knowledge, sentence.disjuncts[0]) or is_in(knowledge, Not(sentence.disjuncts[0]))) and not is_in(knowledge, sentence.disjuncts[1]):
                print(f"Or: {sentence.disjuncts}")
                inferrable_knowledge.append(sentence.disjuncts[1])
            if not is_in(knowledge, sentence.disjuncts[0]) and (is_in(knowledge, sentence.disjuncts[1]) or is_in(knowledge, Not(sentence.disjuncts[1]))):
                inferrable_knowledge.append(sentence.disjuncts[0])   
        if type(sentence) is Implication:
            if is_in(knowledge,sentence.antecedent) and not is_in(knowledge,sentence.consequent):
                print(f"Implication: {sentence.antecedent} -> {sentence.consequent}")
                inferrable_knowledge.append(sentence.consequent)
        if type(sentence) is Biconditional:
            left_known = is_in(knowledge,sentence.left)
            right_known = is_in(knowledge, sentence.right)

            if left_known and not right_known:
                inferrable_knowledge.append(sentence.right)
            elif right_known and not left_known:
                inferrable_knowledge.append(sentence.left)
    print(f"New Inferred knowledge: {inferrable_knowledge}")
    return inferrable_knowledge

            


def forward_search(knowledge, query):
    """
        solved the query by doing forward search.
    
        parameters:
        - The knowledge base containing all knowledge. This is an And formula.
        - The query to check. This is expected to be a symbol.

        returns:
        - True: if the query can be proven
        - False: if the query can be disproven
        - None: if the query can't be proven or disproven
    """

    # Best practice: copy the knowledge base so we don't accidentally modify an input parameter.
    knowledge_base = deepcopy(knowledge)
    count = 1
    
    # Looping through the entire knowledgbase while adding newly inferred knowledge to the copied knowledge base and checking for a result to return
    while True:
        print(f"Attempt: {count}")
        count += 1
        answer = check_proven(knowledge_base,query) # calculating an answer to see if the query is proven/unproven/doesn't exist in the knowledgebase
        if answer != None: #returning the answer if the query is proven/unproven
            return answer
        
        inferrable_knowledge = get_inferrable_knowledge(knowledge_base) # calculate all new inferrable knowledge from existing knowledgebase

        if(len(inferrable_knowledge)==0): # if no new inferred knowledge then break and return None, since we can't prove/disprove
            break

        for sentence in inferrable_knowledge: # add the newly inferred knowledge into the existing knowledgbase
            if(is_in(knowledge_base,sentence)==False):
                knowledge_base.conjuncts.append(sentence)

    return None



    
