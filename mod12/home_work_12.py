from pathlib import Path
import pickle

class Record:
    pass

class AddressBook:
    def __init__(self, filename):
        self.records = {}
        self.last_record_id = 0
        self.file = Path(filename)
        self.deserialize()

    def add(self, record: Record):
        self.records[self.last_record_id] = record
        record.id = self.last_record_id
        self.last_record_id += 1

    def search(self, search_str):
        result = []
        for record_id, record in self.records.items():
            if search_str in record:
                result.append(record_id)
        return result

    def serialize(self):
        with open(self.file, "wb") as file:
            pickle.dump((self.last_record_id, self.records), file)

    def deserialize(self):
        if not self.file.exists():
            return None
        with open(self.file, "rb") as file:
            self.last_record_id, self.records = pickle.load(file)

    def show_record(self, rec_id):
        return f'{self.records[rec_id]}\n'

    def show_records(self, size: int):
        counter = 0
        result = ""
        for record in self.records.values():
            result += str(record)
            counter += 1
            if counter == size:
                yield result
                counter = 0
                result = ""
        yield result
