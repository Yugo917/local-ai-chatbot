import re
from typing import List, Tuple

class Prompter:
    def replace_patterns_in_prompt(self, prompt: str, patterns: List[Tuple[str, str]]) -> str:

        for pattern, replacement in patterns:
            prompt = re.sub(pattern, replacement, prompt)

        return prompt
