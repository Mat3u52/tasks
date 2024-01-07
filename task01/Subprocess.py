from typing import Optional
from Processor import Processor


class Subprocess(Processor):
    def process(self, dta: Optional[dict]) -> tuple:
        return super().process(dta) + (('extension', True),)


if __name__ == "__main__":

    obj_subprocess = Subprocess()

    some_dict = {
        "key_option0": "value0",
        "key_option1": "value1",
        "key_option2": "value2"
    }

    outcome = obj_subprocess.process(some_dict)

    print(outcome)

