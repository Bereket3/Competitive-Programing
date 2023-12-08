class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mapper= defaultdict(list)
        for path in paths:

            files = path.split(' ')
            directory = files[0]
            
            for _file in files[1:]:
                name, content = _file.split('(')
                mapper[content[:-1]].append(directory + '/' + name)
        out_put = [mapper[content] for content in mapper if len(mapper[content]) > 1]
                
        return out_put