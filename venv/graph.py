from collections import deque

def person_is_seller(name):
    return name[-1] == 'p'

def search(name):

    search_queue = deque()
    search_queue += graph [name]
    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print (person + ' found!')
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False
if __name__ == '__main__':

    graph = {}
    graph['You'] = {'Ann', 'John', 'ZZ_top'}
    graph['Ann'] = {'Anuj', 'Peggy'}
    graph['John'] = {'Peggy'}
    graph['ZZ_top'] = {'Tom', 'Curt'}
    graph['Anuj'] = {}
    graph['Peggy'] = {}
    graph['Tom'] = {}
    graph['Curt'] = {}


    print(search('You'))

