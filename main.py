import pypandoc
from gen import gen


args = {}

# 원하는 argument로 변경
args["subject"] = "Programming Language and Compiler"
args["q_type"] = "Calculation"
args["q_type_explanation"] = "Given a question, the student will calculate or find step-by-step procedure to find the answer."
args["coverage"] = "Top Down Parser"
args["reference"] = r"""
Left Factoring

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