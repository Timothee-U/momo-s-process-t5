import uuid

class DataHandler:
    def __init__(self):
        self.transactions = {}

    def get_all(self):
        return list(self.transactions.values())

    def get_one(self, tid):
        return self.transactions.get(tid)

    def add(self, data):
        tid = str(uuid.uuid4())
        data["id"] = tid
        self.transactions[tid] = data
        return data

    def update(self, tid, new_data):
        if tid in self.transactions:
            self.transactions[tid].update(new_data)
            return self.transactions[tid]
        return None

    def delete(self, tid):
        return self.transactions.pop(tid, None)