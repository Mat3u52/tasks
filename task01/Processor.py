from typing import Optional


class Processor:
    def process(self, dta: Optional[dict]) -> tuple:
        return tuple(dta.items() or {})


if __name__ == "__main__":

    some_dict = {
        "key_option0": "value0",
        "key_option1": "value1",
        "key_option2": "value2"
    }

    obj_Processor = Processor()

    outcome = obj_Processor.process(some_dict)

    print(outcome)

