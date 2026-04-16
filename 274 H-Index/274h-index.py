class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
        
        # Desc:
        acc_citations = 0
        for curr_citation in citations:
            acc_citations += 1
            if curr_citation < acc_citations:
                return acc_citations - 1
            elif curr_citation == acc_citations:
                return acc_citations

        return acc_citations