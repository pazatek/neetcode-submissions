class UnionFind:
    def __init__(self, n):
            self.parent = [i for i in range(n)]
            self.rank = [1] * n

    def search(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, x1, x2):
        parent1 = self.search(x1)
        parent2 = self.search(x2)
        if parent1 == parent2:
            return False
        if self.rank[parent1] > self.rank[parent2]:
            self.parent[parent2] = parent1
            self.rank[parent1] += self.rank[parent2]
        else:
            self.parent[parent1] = parent2
            self.rank[parent2] += self.rank[parent1]
        return True
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        uf = UnionFind(len(accounts))
        emailsToRowIndex = {}

        for rowIndex, nameAndEmails in enumerate(accounts):
            for email in nameAndEmails[1:]:
                if email in emailsToRowIndex:              # if this email is already associated with an account, 
                    uf.union(emailsToRowIndex[email], rowIndex) # associate this other account and all its emails with it
                else:
                    emailsToRowIndex[email] = rowIndex
                
        rootRowToEmails = defaultdict(list)
        for email, rowIndex in emailsToRowIndex.items():
            rootRowIndex = uf.search(rowIndex)
            rootRowToEmails[rootRowIndex].append(email)

        result = []
        for rootRowIndex, emails in rootRowToEmails.items():
            result.append([accounts[rootRowIndex][0]] + sorted(emails))
        return result

