class WS:
    def __init__(self, id, cap):
        self.id = id
        self.cap = cap
        self.q = []
        self.idle = 0

    def process(self):
        if self.q:
            self.q[0]["pt"] -= 1
            if self.q[0]["pt"] == 0:
                self.q.pop(0)
                return True
        else:
            self.idle += 1
        return False

    def add(self, batch):
        if len(self.q) < self.cap:
            self.q.append(batch)
            return True
        return False


class PL:
    def __init__(self, ws_list):
        self.ws_list = [WS(**ws) for ws in ws_list]
        self.tp = 0

    def simulate(self, batches, steps):
        for step in range(steps):
            for i in range(len(self.ws_list) - 1, -1, -1):
                if self.ws_list[i].process():
                    if i < len(self.ws_list) - 1:
                        self.ws_list[i + 1].add({"pt": 1})
                    else:
                        self.tp += 1
            for batch in batches:
                if batch["at"] == step:
                    self.ws_list[0].add(batch)
        idle_times = {f"ws_{ws.id}": ws.idle for ws in self.ws_list}
        return {"tp": self.tp, "idle_time": idle_times}


ws_list = [{"id": 1, "cap": 1}, {"id": 2, "cap": 2}, {"id": 3, "cap": 1}]
batches = [{"at": 0, "pt": 3}, {"at": 2, "pt": 2}, {"at": 4, "pt": 1}]
steps = 10

pl = PL(ws_list)
result = pl.simulate(batches, steps)
print(result)
