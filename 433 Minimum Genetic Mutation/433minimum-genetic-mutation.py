class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank = set(bank)
        current_genes = { startGene }
        mutation_count = 0
        # Search based on adjacency

        while current_genes:
            next_genes = set()
            for gene in current_genes:
                for i in range(8):
                    for char in ['A', 'C', 'G', 'T']:
                        new_gene = gene[:i] + char + gene[i+1:]
                        if new_gene in bank:
                            if new_gene == endGene:
                                return mutation_count + 1
                            bank.remove(new_gene)
                            next_genes.add(new_gene)

            current_genes = next_genes
            mutation_count += 1
        return -1