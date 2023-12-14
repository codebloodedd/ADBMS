class Coordinater:
    def __init__(self):
        self.participants = []
        self.votes = []

    def add_participant(self, participant):
        self.participants.append(participant)

    def send_prepare(self):
        print("-------------- Preparation Phase --------------")
        for p in self.participants:
            p.receive_prepare()

    def start_voting(self):
        print("-------------- Voting Phase --------------")
        for p in self.participants:
            self.votes.append(p.send_vote())
    
    def send_commit(self):
        print("-------------- Commit Phase --------------")
        for p in self.participants:
            p.receive_commit()

    def make_decision(self):
        print("-------------- Decision Phase --------------")
        if 0 in self.votes:
            print("Transaction aborted as all participating sites not ready!")   
        else: 
            print("Transaction Commited") 

class Participant:
    def __init__(self, name):
        self.name = name
        self.prepared = False
    
    def receive_prepare(self):
        print(f"{self.name} is preparation phase")

    def send_vote(self):
        v = int(input("Enter 1 if ready to commit and 0 if not: "))
        if v:
            self.prepared = True
        return v
    
    def receive_commit(self):
        if self.prepared:
            print(f"{self.name} has committed")
        else:
            print(f"{self.name} did not commit because it was not prepared")
    

n = int(input("Enter the number of participants: "))

coordinater = Coordinater()

for i in range(n):
    participant = Participant(f"Participant {i+1}")
    coordinater.add_participant(participant)

coordinater.send_prepare()
coordinater.start_voting()
coordinater.send_commit()
coordinater.make_decision()

print("Tranaction completed")