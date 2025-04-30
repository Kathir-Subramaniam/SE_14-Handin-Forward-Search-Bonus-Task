<h1 align=center><strong>SE_14 Handin Forward Search Bonus Task</strong></h1>

# Problem Description: 
The goal of the problem was to check if a given query is proven/ disproven/ unknown based on a given knowledge base. The knowledge base contains propositional logic statements using AND, OR, NOT, IMPLICATION and BICONDITIONAL. We use them iteratively to infer new knowledge and the implemented forward search does this until the query is resolved or when no new inferences can be made.

# Area of AI: 
Reasoning

# Applied Algorithms: 
Forward Search is the algorithm applied to the solution. The algorithm iteratively uses the logical operators to infer new knowledge till we can either prove or disprove the query or not reach a conclusion. It does this with the help of helper functions. `is_in` checks if the query is in the knowledge base, `check_proven` returns True / False / None depending on the result of the `is_in` function and `get_inferrable_knowledge` takes a knowledge base as an input parameter and returns all the new inferrable knowledge in an array. 

# Results: 
The forward search algorithm successfully determines whether a query is provable, disprovable or can’t be inferred from the knowledge base. The algorithm can infer new facts from logical operators such as conjunction, disjunction, implication, biconditional and negation. The algorithm ensures that no duplicate inferences are added to the knowledge base and stops when no new knowledge can be inferred. This method of using the forward search is very efficient when it comes to solving reasoning problems involving knowledge bases with logical statements. 

# Location: 
The forward search algorithm is implemented in the file called `forward_search.py`, located at `/solvers/forward_search.py`