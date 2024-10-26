import pypandoc

from gen import gen

args = {}
args["subject"] = "Programming Language and Compilers"
args["q_type"] = "Short answer"
args["q_type_explanation"] = "Question that requires students to write words or sentences or fill in table."
args["coverage"] = "Top Down Parser"
args["reference"] = """Left Factoring

What if my grammar does not have the LL(1) property?
- Sometimes, we can transform the grammar.

Transformation Process:
For any A ∈ NT:
1. Find the longest prefix α that occurs in two or more right-hand sides of A.
2. If α ≠ ε, then replace all productions of A as follows:

   A → αβ1 | αβ2 | … | αβn | γ

   with

   - A → αZ | γ
   - Z → β1 | β2 | … | βn

   where Z is a new element of NT.

3. Repeat until no common prefixes remain.
"""

response = gen(args)

with open("response.md", "w") as file:
    file.write(response)
    
pypandoc.convert_file("response.md", "pdf", outputfile="response.pdf")