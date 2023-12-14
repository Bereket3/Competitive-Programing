class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        mapper = {}
        for _ in cpdomains:
            num, _domain = _.split()
            num, domain = int(num), _domain.split('.')
            for i in range(len(domain)):
                sub_domain = '.'.join(domain[i:])
                if sub_domain in mapper:
                    mapper[sub_domain] += num
                else:
                    mapper[sub_domain] = num

        return [f'{v} {k}' for k, v in mapper.items()]