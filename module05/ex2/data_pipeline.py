from typing import Any, Dict, List, Union, Protocol
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


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


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
                    print("Data Stream error - Can't process element "
                          f"in stream: {element}")
                if proc.validate(element) is True:
                    proc.ingest(element)
                    break

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            batch: list[tuple[int, str]] = []
            for _ in range(nb):
                try:
                    batch.append(proc.output())
                except IndexError:
                    break
            plugin.process_output(batch)

    def print_processors_stats(self) -> None:
        print("\n== DataStream statistics ==\n")

        if not self._processors:
            print("No processor found, no data")
            return
        for proc in self._processors:
            name = type(proc).__name__.replace("Processor", " Processor")
            remaining = len(proc._data)
            total = proc._count + remaining
            print(f"{name}: total {total} items processed, "
                  f"remaining {remaining} on processor")

# CSV and JSON

# so i dont forget -> CSV = Comma Separated Values
# from reddit -> It's a text file with rows that have commas separating
# values on each row.
# This is one way of representing a table of information (like a sheet in
# an Excel workbook).
# You might use it if you want a simple and portable way to save a table.


class CSVExport:
    def _field(self, value: str) -> str:
        if any(c in value for c in ',"\n\r'):
            return '"' + value.replace('"', '""') + '"'
        return value

    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        print(",".join(self._field(value) for _, value in data))


# JSON = JavaScript Object Notation
# It's a text file that contains a data structure that's valid JavaScript,
# but it can be used with anything.
# It represents data as a list or dictionary where the elements can be
# strings, numbers, or other lists and dictionaries (which can be comprised
# of simple types, or lists and dictionaries, etc.).
# This is a common format for exchanging data with web APIs, and it's also
# a simple way of representing complex data structures.
# JSON supports arrays [x,y,z] and nested json/dict data {key: {id: 1}},
# while CSV doesn't.


class JSONExport:
    def _string(self, value: str) -> str:
        out = ""
        for c in value:
            if c == '"':
                out += '\\"'
            elif c == "\\":
                out += "\\\\"
            elif c == "\n":
                out += "\\n"
            elif c == "\r":
                out += "\\r"
            elif c == "\t":
                out += "\\t"
            elif ord(c) < 0x20:  # ord returns the ordinal val of a char
                out += f"\\u{ord(c):04x}"
            else:
                out += c
        return '"' + out + '"'

    def process_output(self, data: list[tuple[int, str]]) -> None:
        items = [f'"item_{rank}": {self._string(value)}'
                 for rank, value in data]
        print("JSON Output:")
        print("{" + ", ".join(items) + "}")


# just to help me
def consume(processor: DataProcessor, count: int) -> None:
    for _ in range(count):
        processor.output()


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("\nInitialize Data Stream...")
    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Processors\n")
    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    stream.register_processor(num)
    stream.register_processor(text)
    stream.register_processor(log)

    batch: List[Any] = [
        "Hello world",
        [3.14, -1, 2.71],
        [{"log_level": "WARNING",
          "log_message": "Telnet access! Use ssh instead"},
         {"log_level": "INFO", "log_message": "User bil is connected"}],
        42,
        ["Hi", "five"]]

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin:")
    stream.output_pipeline(3, CSVExport())
    stream.print_processors_stats()

    batch2: List[Any] = [
        21,
        ["I hate AI", "LLMs are bad for your brain", "Stay healthy"],
        [{"log_level": "ERROR", "log_message": "500 server crash"},
         {"log_level": "NOTICE",
          "log_message": "Certificate expires in 10 days"}],
        [32, 42, 64, 84, 128, 168],
        "Hsin is a goated Sentinel"]
    print(f"\nSend another batch of data: {batch2}")
    stream.process_stream(batch2)
    stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin:")
    stream.output_pipeline(5, JSONExport())
    stream.print_processors_stats()
