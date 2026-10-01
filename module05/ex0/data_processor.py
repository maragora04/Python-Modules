from typing import Any, Dict, List, Union
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: List[str] = []
        self._count: int = 0

    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._data:
            raise IndexError("No data to output")
        value = self._data.pop(0)
        rank = self._count
        self._count += 1
        return (rank, value)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, bool):
            return False
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            for item in data:
                if isinstance(item, bool):
                    return False
                if not isinstance(item, (int, float)):
                    return False
            return True
        return False

    def ingest(
        self, data: Union[int, float, List[Union[int, float]]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._data.append(str(item))


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, str):
                    return False
            return True
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            items = data
        else:
            items = [data]
        for item in items:
            self._data.append(item)


class LogProcessor(DataProcessor):
    def _is_log(self, entry: Any) -> bool:
        if not isinstance(entry, dict):
            return False
        for key, value in entry.items():
            if not isinstance(key, str) or not isinstance(value, str):
                return False
        return True

    def validate(self, data: Any) -> bool:
        if isinstance(data, list):
            for entry in data:
                if not self._is_log(entry):
                    return False
            return True
        return self._is_log(data)

    def ingest(
        self, data: Union[Dict[str, str], List[Dict[str, str]]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            entries = data
        else:
            entries = [data]
        for entry in entries:
            self._data.append(": ".join(entry.values()))


# just to help me
def extract(processor: DataProcessor, count: int, label: str) -> None:
    plural = "" if count == 1 else "s"
    print(f"Extracting {count} value{plural}...")
    for _ in range(count):
        rank, value = processor.output()
        print(f"{label} {rank}: {value}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")

    print("Testing Numeric Processor...")
    num = NumericProcessor()
    for input in (42, "Hello"):
        print(f"Trying to validate input '{input}': {num.validate(input)}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        num.ingest("foo")
    except ValueError as error:
        print(f"Got exception: {error}")
    numbers: List[Union[int, float]] = [1, 2, 3, 4, 5]
    print(f"Processing data: {numbers}")
    num.ingest(numbers)
    extract(num, len(numbers), "Numeric value")

    print("Testing Text Processor...")
    text = TextProcessor()
    for input in (42, "Hello"):
        print(f"Trying to validate input '{input}': {text.validate(input)}")
    words = ["Hello", "Nexus", "World"]
    print(f"Processing data: {words}")
    text.ingest(words)
    extract(text, len(words), "Text value")

    print("Testing Log Processor...")
    log = LogProcessor()
    for input in (42, "Hello"):
        print(f"Trying to validate input '{input}': {log.validate(input)}")
    logs: List[Dict[str, str]] = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"}]

    print(f"Processing data: {logs}")
    log.ingest(logs)
    extract(log, len(logs), "Log entry")
