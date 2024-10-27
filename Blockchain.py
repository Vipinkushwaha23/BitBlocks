import hashlib
import time


# Block class representing each record in the ledger
class Block:
    def __init__(self, manufacturer_urn, quantity_type_chemical, vehicle_number, destination, previous_hash=''):
        self.manufacturer_urn = manufacturer_urn
        self.quantity_type_chemical = quantity_type_chemical
        self.vehicle_number = vehicle_number
        self.destination = destination
        self.timestamp = time.time()  # Store the current timestamp
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    # Method to calculate the block's hash using SHA-256
    def calculate_hash(self):
        block_data = (self.previous_hash + str(self.timestamp) + self.manufacturer_urn +
                      self.quantity_type_chemical + self.vehicle_number + self.destination)
        return hashlib.sha256(block_data.encode()).hexdigest()

    # Method to display block data in tabular format
    def display_block(self):
        print(
            f"{self.manufacturer_urn:<20} {self.quantity_type_chemical:<30} {self.vehicle_number:<20} {self.destination:<20}")


# Blockchain class representing the ledger
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    # Genesis block (first block)
    @staticmethod
    def create_genesis_block():
        return Block("GENESIS", "0", "N/A", "N/A", "0")

    # Method to get the last block in the chain
    def get_last_block(self):
        return self.chain[-1]

    # Method to add a new block to the chain
    def add_block(self, manufacturer_urn, quantity_type_chemical, vehicle_number, destination):
        previous_block = self.get_last_block()
        new_block = Block(manufacturer_urn, quantity_type_chemical, vehicle_number, destination, previous_block.hash)
        self.chain.append(new_block)

    # Method to display the entire ledger
    def display_ledger(self):
        print(
            f"{'Manufacturer URN':<20} {'Quantity & Type of Chemical':<30} {'Vehicle Number':<20} {'Destination':<20}")
        print("-" * 90)
        for block in self.chain:
            block.display_block()

    # Verify blockchain integrity
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            # Check if the current block's hash is still valid
            if current_block.hash != current_block.calculate_hash():
                print("Current block's hash is invalid.")
                return False

            # Check if the previous block's hash matches the previous hash in the current block
            if current_block.previous_hash != previous_block.hash:
                print("Previous block's hash does not match.")
                return False

        return True


# Main function to run the immutable ledger
if __name__ == "__main__":
    # Create a new blockchain (ledger)
    ledger = Blockchain()

    # Adding blocks to the ledger
    ledger.add_block("MAN-001", "500 Liters of Chemical-A", "TX1234", "New York")
    ledger.add_block("MAN-002", "300 Liters of Chemical-B", "CA5678", "Los Angeles")
    ledger.add_block("MAN-003", "700 Liters of Chemical-C", "FL9101", "Miami")
    ledger.add_block("MAN-004", "200 Liters of Chemical-D", "TX1122", "Houston")
    ledger.add_block("MAN-005", "150 Liters of Chemical-E", "CA3344", "San Francisco")
    ledger.add_block("MAN-006", "800 Liters of Chemical-F", "FL5566", "Orlando")
    ledger.add_block("MAN-007", "450 Liters of Chemical-G", "NY7788", "Buffalo")
    ledger.add_block("MAN-008", "600 Liters of Chemical-H", "TX9900", "Dallas")
    ledger.add_block("MAN-009", "550 Liters of Chemical-I", "CA2233", "San Diego")
    ledger.add_block("MAN-010", "750 Liters of Chemical-J", "FL4455", "Tampa")
    ledger.add_block("MAN-011", "400 Liters of Chemical-K", "TX6677", "Austin")
    ledger.add_block("MAN-012", "350 Liters of Chemical-L", "CA8899", "Sacramento")
    ledger.add_block("MAN-013", "500 Liters of Chemical-M", "FL1010", "Jacksonville")
    ledger.add_block("MAN-014", "700 Liters of Chemical-N", "TX2020", "Fort Worth")
    ledger.add_block("MAN-015", "250 Liters of Chemical-O", "CA3030", "Long Beach")
    ledger.add_block("MAN-016", "600 Liters of Chemical-P", "FL4040", "St. Petersburg")
    ledger.add_block("MAN-017", "450 Liters of Chemical-Q", "TX5050", "El Paso")
    ledger.add_block("MAN-018", "500 Liters of Chemical-R", "CA6060", "Fresno")
    ledger.add_block("MAN-019", "550 Liters of Chemical-S", "FL7070", "Tallahassee")
    ledger.add_block("MAN-020", "650 Liters of Chemical-T", "TX8080", "Arlington")
    ledger.add_block("MAN-021", "300 Liters of Chemical-U", "CA9090", "Bakersfield")
    ledger.add_block("MAN-022", "400 Liters of Chemical-V", "FL1212", "Fort Lauderdale")
    ledger.add_block("MAN-023", "500 Liters of Chemical-W", "TX1313", "Corpus Christi")
    ledger.add_block("MAN-024", "600 Liters of Chemical-X", "CA1414", "Anaheim")
    ledger.add_block("MAN-025", "700 Liters of Chemical-Y", "FL1515", "Hialeah")
    ledger.add_block("MAN-026", "450 Liters of Chemical-Z", "TX1616", "Plano")
    ledger.add_block("MAN-027", "500 Liters of Chemical-AA", "CA1717", "Santa Ana")
    ledger.add_block("MAN-028", "550 Liters of Chemical-BB", "FL1818", "Hollywood")
    ledger.add_block("MAN-029", "600 Liters of Chemical-CC", "TX1919", "Lubbock")
    ledger.add_block("MAN-030", "650 Liters of Chemical-DD", "CA2020", "Stockton")
    ledger.add_block("MAN-031", "700 Liters of Chemical-EE", "FL2121", "Pembroke Pines")
    ledger.add_block("MAN-032", "750 Liters of Chemical-FF", "TX2222", "Laredo")
    ledger.add_block("MAN-033", "800 Liters of Chemical-GG", "CA2323", "Chula Vista")
    ledger.add_block("MAN-034", "350 Liters of Chemical-HH", "FL2424", "Cape Coral")
    ledger.add_block("MAN-035", "500 Liters of Chemical-II", "TX2525", "Garland")
    ledger.add_block("MAN-036", "550 Liters of Chemical-JJ", "CA2626", "Riverside")
    ledger.add_block("MAN-037", "600 Liters of Chemical-KK", "FL2727", "Clearwater")
    ledger.add_block("MAN-038", "650 Liters of Chemical-LL", "TX2828", "Irving")
    ledger.add_block("MAN-039", "700 Liters of Chemical-MM", "CA2929", "San Bernardino")
    ledger.add_block("MAN-040", "450 Liters of Chemical-NN", "FL3030", "Palm Bay")
    ledger.add_block("MAN-041", "500 Liters of Chemical-OO", "TX3131", "Amarillo")
    ledger.add_block("MAN-042", "550 Liters of Chemical-PP", "CA3232", "Modesto")
    ledger.add_block("MAN-043", "600 Liters of Chemical-QQ", "FL3333", "Port St. Lucie")
    ledger.add_block("MAN-044", "650 Liters of Chemical-RR", "TX3434", "McKinney")
    ledger.add_block("MAN-045", "700 Liters of Chemical-SS", "CA3535", "Oxnard")
    ledger.add_block("MAN-046", "450 Liters of Chemical-TT", "FL3636", "Lakeland")
    ledger.add_block("MAN-047", "500 Liters of Chemical-UU", "TX3737", "Frisco")
    ledger.add_block("MAN-048", "550 Liters of Chemical-VV", "CA3838", "Huntington Beach")
    ledger.add_block("MAN-049", "600 Liters of Chemical-WW", "FL3939", "Miramar")
    ledger.add_block("MAN-050", "700 Liters of Chemical-XX", "TX4040", "Brownsville")

    # Display the ledger
    ledger.display_ledger()
