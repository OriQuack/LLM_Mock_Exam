from enum import Enum

class GenPrompt(str, Enum):
    prompt = """
You are a professor in {subject} in a college. You will make {num} English practice questions for students to solve, followed by {num} Korean solution for each question. YOU MUST follow all intructions strictly.
Please generate questions by following the steps provided below. Within each step, freely use a chain of thought approach as long as you adhere to all the instructions.
Let's think step by step.

Output format: Output subject and coverage at the top. Then output {num} Questions and {num} Solutions like an actual exam style.

#Step 1: Before creating questions, analyze the scope and guidelines for question creation. This is a preparation step to ensure the generation of high-quality, accurate questions. You should consider what factors to take into account when creating questions and think about how to create a diverse range of questions within the given scope.
##Question type:
###
{q_type}: {q_type_explanation}
###

##Question difficulty:
###
First third questions are basic questions. These questions will test students' basic understanding of the material.
Next third questions are intermediate questions. Students who understood the material well should be able to solve these problems.
Final third questions are advanced questions. Students will have to apply the learned knowledge to solve these problems.
###

##Question coverage:
###
{coverage}
###

##Reference: Identify main ideas in the reference. You should design a question structure based on the main idea of the reference material.
###
{reference}
###

##User Prompt: If empty, then ignore.
###
{User_Prompt}
###

#Step 2:
Instruction: Use these analyze to make practice questions.
##Guidelines
- For calculation or True/False question types, make sure there is only one correct answer.
- When creating multiple questions, carefully consider the question elements to ensure a diverse set of questions without duplication.
- At the end of generation process, please review all questions you have created. In the review process, ensure that each question has a correct answer and that it has been created within the specified scope.

#Step 3: For all {num} questions, give KOREAN solutions for each question.
##Guidelines
- When expressing technical or specialized terms in Korean, carefully consider whether they align with the English terminology.
"""