import pypandoc
from gen import gen

"""
q_type and q_type_explanation example:

args["q_type"] = "Calculation"
args["q_type_explanation"] = "Given a question, the student will calculate or find step-by-step procedure to find the answer."

args["q_type"] = "True and False"
args["q_type_explanation"] = "Given a statement, the student will answer true or false."

"""
args = {}

# 원하는 argument로 변경
args["subject"] = "Programming Language and Compiler"
args["q_type"] = "True and False"
args["q_type_explanation"] = "Given a statement, the student will answer true or false."
args["coverage"] = "Scanner, Context Free Grammar, Top Down Parser, Bottom Up Parser, Context Sensitive Analysis"
args["reference"] = r"""
4. Answer the following questions about attribute grammar (AG)and ad-hoc syntax-directed
translation (SDT). [total 20 points]

Production Attribution Rules
D → T L ; { L.in := T.type }
T → int { T.type := integer }
| float { T.type := real }
L0 → L1 , id { L1.in := L0.in; addtype (word(id), L0.in); }
| id { addtype (word(id), L0.in) }
( non-terminals = { D, T, L }, terminals = { int, float, id, ;, , } )
- word ( id ) returns the input string (variable names) which matches with the token, id.
- addtype ( string, type ) inserts an entry in the symbol table, where its variable name
corresponds to string and its type corresponds to type.

(A) The above AG describes a method to build a simple symbol table. For each non-terminal, list
its attributes and categorize them with their characteristics. [5 points]

(B) Assuming an input is given as follows, draw the parse tree for the input and specify
dependence among attributes [5 point]

(C) Write an ad-hoc SDT to build the symbol table in a similar way to the above AG [10 points].
Use the following functions in the code. If needed, define necessary functions with descriptions
of their internal works.

addType(type, list): insert items in list with type
list_create(): create an empty list and return it.
list_add(L, id): add an item id into the list L. and return the list with added item.
"""
args["User_Prompt"] = ""

# 문항 생성
response = gen(args)

# 문항 markdown 형식으로 저장
yaml_header = r"""---
header-includes:
  - \usepackage{fontspec}
  - \setmainfont{NanumGothic}
---
"""
response = yaml_header + response
with open("response.md", "w") as file:
    file.write(response)

# 문항 pdf로 변환
pypandoc.convert_file("response.md", "pdf", outputfile="response.pdf", extra_args=["--pdf-engine=xelatex"])