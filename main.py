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
1. Answer with either “true” or “false” for the following statements. [Total 15 points]
(A) Expressive power of regular expression has the same expressive power of non-deterministic
finite automata. ( ) [3 points]
(B) If a language is specified with context-free grammar, this language can be parsed with either
LL(1) parser or LR(1) parser. ( ) [3 points]
(C) If a context-free grammar has a left recursion, it fails to satisfy LL(1) property. ( )
[3 points]
(D) If an attribute grammar has both synthesized attributes and inherited attributes, it will
generate a circular dependence among attributes. ( ) [3 points]
(E) If a CFG parses an input sentence into two different sequence of derivation steps by using the
same derivation approach, either leftmost derivation or rightmost derivation, the corresponding
grammar is ambiguous. ( ) [3 points]
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