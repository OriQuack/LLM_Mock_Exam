from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate

from prompt import GenPrompt

load_dotenv()


def gen(args: dict):
    # Get model
    prompt_message = ChatPromptTemplate.from_messages(
        [
            ("user", "{user_input}"),
        ]
    )
    llm = ChatOpenAI(
        model_name="o1-preview", temperature=1, max_completion_tokens=10000
    )
    model = prompt_message | llm

    # Get prompt
    prompt_template = GenPrompt.prompt

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=[
            "subject",
            "q_type",
            "q_type_explanation",
            "coverage",
            "reference",
        ],
    )

    # Get response
    chain = prompt | model
    response = chain.invoke(
        {
            "subject": args.get("subject", ""),
            "q_type": args.get("q_type", ""),
            "q_type_explanation": args.get("q_type_explanation", ""),
            "coverage": args.get("coverage", ""),
            "reference": args.get("reference", ""),
        }
    )
    return response.content