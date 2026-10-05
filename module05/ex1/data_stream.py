from typing import Any, Dict, List, Union
from abc import ABC, abstractmethod
import typing


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


class DataStream:
    def __init__(self) -> None:
        self._processors: List[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            for proc in self._processors:
                try:
                    proc.validate(element)
                except ValueError:
                    print(f"Data Stream error - Can't process element in stream: {element}")
                if proc.validate(element) is True:
                    proc.ingest(element)
                    break

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")

        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            remaining = len(proc._data)
            total = proc._count + remaining
            print(f"{name}: total {total} items processed, "
                f"remaining {remaining} on processor")
        


# just to help me
def consume(processor: DataProcessor, count: int) -> None:
    for _ in range(count):
        processor.output()


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    num = NumericProcessor()
    stream.register_processor(num)

    batch: List[Any] = [ "Hello world", [3.14, -1, 2.71], [{"log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead"},
            {"log_level": "INFO", "log_message": "User wil is connected"}], 42, ["Hi", "five"] ]
    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors\n")
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(log)
    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    element_num: Dict[str, tuple[DataProcessor, int]] = {
        "Numeric": (num, 3),
        "Text": (text, 2),
        "Log": (log, 1), }
    summary = ", ".join(f"{name} {count}" for name, (_, count) in element_num.items())
    print(f"\nConsume some elements from the data processors: {summary}")
    for proc, count in element_num.values():
        consume(proc, count)
    stream.print_processors_stats()


    # !! data stream test !! 
    stream = DataStream()
    num, text, log = NumericProcessor(), TextProcessor(), LogProcessor()
    for proc in (num, text, log):
        stream.register_processor(proc)

    batch: List[Any] = [ "Hello world",
        [3.14, -1, 2.3],
        [{"log_level": "WARNING", "log_message": "Telnet access!"}],
        42, None ]
    stream.process_stream(batch)