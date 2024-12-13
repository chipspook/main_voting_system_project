
import os
import json

class VoteSystem:
    def __init__(self, data_file='votes.json'):
        self.data_file = data_file
        self.candidates = {1: 'Bianca', 2: 'Edward', 3: 'Felicia'}
        self.votes = {candidate_id: 0 for candidate_id in self.candidates}
        self.load_votes()

    def load_votes(self):
        """Load votes from a file."""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as file:
                self.votes = json.load(file)

    def save_votes(self):
        """Save votes to a file."""
        with open(self.data_file, 'w') as file:
            json.dump(self.votes, file)

    def vote(self, candidate_id):
        """Add a vote to the selected candidate."""
        if candidate_id in self.candidates:
            self.votes[candidate_id] += 1
            self.save_votes()
            return self.candidates[candidate_id]
        else:
            raise ValueError("Invalid candidate ID.")

    def get_results(self):
        """Return the voting results."""
        total_votes = sum(self.votes.values())
        return {self.candidates[cid]: self.votes[cid] for cid in self.candidates}, total_votes

def text_based_ui(predefined_inputs):
    """Run a text-based user interface for the voting system with predefined inputs."""
    vote_system = VoteSystem()
    input_index = 0

    def get_next_input(prompt):
        nonlocal input_index
        if input_index < len(predefined_inputs):
            response = predefined_inputs[input_index]
            print(f"{prompt} {response}")
            input_index += 1
            return response
        else:
            raise ValueError("No more inputs available.")

    while True:
        print('----------------------------------')
        print('VOTE MENU')
        print('----------------------------------')
        print('1: Vote')
        print('2: Show Results')
        print('3: Exit')
        option = get_next_input('Option:').strip()

        if option == '1':
            print('----------------------------------')
            print('CANDIDATE MENU')
            print('----------------------------------')
            for cid, name in vote_system.candidates.items():
                print(f'{cid}: {name}')
            try:
                candidate_choice = int(get_next_input('Candidate:').strip())
                candidate_name = vote_system.vote(candidate_choice)
                print(f'Voted for {candidate_name}')
            except ValueError as e:
                print(f'Error: {e}')
        elif option == '2':
            results, total_votes = vote_system.get_results()
            print('----------------------------------')
            for candidate, votes in results.items():
                print(f'{candidate}: {votes}')
            print(f'Total Votes: {total_votes}')
            print('----------------------------------')
        elif option == '3':
            print('Exiting the voting system. Goodbye!')
            break
        else:
            print('Invalid option. Please choose 1, 2, or 3.')

if __name__ == '__main__':
    predefined_inputs = ["1", "2", "3", "1", "1", "2", "3"]  # Example inputs for testing
    text_based_ui(predefined_inputs)
