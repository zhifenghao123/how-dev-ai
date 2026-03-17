from langchain_core.prompts import load_prompt


def load_yaml_prompt_template():
    prompt_template = load_prompt("res/simple_prompt_yaml.yml")
    prompt = prompt_template.format(name="hao", what="上学")
    print(prompt)

def load_json_prompt_template():
    prompt_template = load_prompt("res/simple_prompt_json.json")
    prompt = prompt_template.format(name="hao", what="上学")
    print(prompt)


def main():
    load_yaml_prompt_template()
    load_json_prompt_template()

if __name__ == '__main__':
    main()