class InvalidDNAError(Exception):
    pass
class InvalidSiteError(Exception):
    pass
class DNASequence:
    VALID_BASES = set("ATGC")
    def __init__(self, id, sequence):
        sequence = sequence.upper()
        if not sequence:
            raise InvalidDNAError("DNA sequence cannot be empty.")
        invalid_bases = set(sequence) - self.VALID_BASES
        if invalid_bases:
            raise InvalidDNAError(f"Invalid DNA base(s): {', '.join(sorted(invalid_bases))}")
        self.id = id
        self.sequence = sequence
    def complement(self):
        pairing = {"A": "T", "T": "A", "G": "C", "C": "G"}
        new_sequence = "".join(pairing[base] for base in self.sequence)
        return DNASequence(self.id + "_comp", new_sequence)
    def reverse_complement(self):
        reversed_sequence = self.complement().sequence[::-1]
        return DNASequence(self.id + "_revcomp", reversed_sequence)
    def transcribe(self):
        return self.sequence.replace("T", "U")
    def find_site(self, site):
        site = site.upper()
        if not site or set(site) - self.VALID_BASES:
               raise InvalidSiteError("Search site must contain only A, T, G and C.")
        positions = []
        start = 0
        while True:
            index = self.sequence.find(site, start)
            if index == -1:
                 break
            positions.append(index + 1)
            start = index + 1
        return positions
if __name__ == "__main__":
    s2 = DNASequence("seq2", "ATGGAATTCTAG")
    print("Original:", s2.sequence)
    print("Complement:", s2.complement().sequence)
    print("Reverse complement:", s2.reverse_complement().sequence)
    print("mRNA:", s2.transcribe())
    print("GAATTC at:", s2.find_site("GAATTC"))
    print("TTT at:", s2.find_site("TTT"))
try:
    DNASequence("bad_seq", "ATGBXYZ")
except InvalidDNAError as error:
    print("DNA error:", error)
try:
    s2.find_site("ATX")
except InvalidSiteError as error:
    print("Site error:", error)