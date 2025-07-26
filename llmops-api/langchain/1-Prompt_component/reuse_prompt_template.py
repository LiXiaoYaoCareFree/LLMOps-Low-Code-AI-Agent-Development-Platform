from langchain_core.prompts import PipelinePromptTemplate, PromptTemplate


full_template = """{instruction}
{example}
{start}"""


full_prompt = PromptTemplate.from_template(full_template)
# 描述提示模板
instruction_template = "你正在模拟{person}。"
instruction_prompt = PromptTemplate.from_template(instruction_template)


# 示例提示模板
example_template = """下面是一个交互例子:
Q: {example_q}
A: {example_a}"""

example_prompt = PromptTemplate.from_template(example_template)


# 开始提示模板
start_template = """现在，你是一个真实的人，请回答用户的问题！
Q: {input}
A:"""

start_prompt = PromptTemplate.from_template(start_template)


input_prompts = [
("instruction", instruction_prompt),
("example", example_prompt),
("start", start_prompt),
]
pipeline_prompt = PipelinePromptTemplate(
    final_prompt=full_prompt,
    pipeline_prompts=input_prompts
)
print(pipeline_prompt.format(
person="雷军", example_q="你最喜欢的汽车是什么?", example_a="小米su7",
input="你最喜欢的手机是什么?"
))