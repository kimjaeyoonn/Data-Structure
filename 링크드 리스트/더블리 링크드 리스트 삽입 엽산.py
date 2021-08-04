class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스
        self.prev = None

class LinkedList:
    """링크드 리스트 클래스"""
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)    # 새로운 데이터를 저장하는 노드

        if self.head is None:    # 링크드 리스트가 비어있는 경우
            self.head = new_node
            self.tail = new_node
        else:    # 링크드 리스트가 비어있지 않은 경우
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드, 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next

        return iterator


    def insert_after(self, previous_node, data):    # 주요 메소드 !!
        """링크드 리스트 삽입 연산 메소드"""
        new_node = Node(data)
        
        if previous_node is self.tail:    # 가장 마지막 순서 삽입
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        else:    # 중간에 삽입하는 경우
            new_node.prev = previous_node
            new_node.next = previous_node.next
            previous_node.next = new_node
            previous_node.next.prev = new_node

        return data

            
    def __str__(self):
        """링크드  리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head


        # 링크드  리스트 끝까지 돈다
        while iterator is not None:    # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next    # 다음 노드로 넘어간다
        return res_str


my_list = LinkedList()

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)    # 첫번째 줄

tail_node = my_list.tail
my_list.insert_after(tail_node, 5)
print(my_list)    # 두번째 줄

print(tail_node.next.data)    # 세번째 줄


index_3 = my_list.find_node_at(3)
my_list.insert_after(index_3, 3)
print(my_list)    # 네번째 줄


index_2 = my_list.find_node_at(2)
my_list.insert_after(index_2, 2)
print(my_list)    # 다섯번째 줄



실행결과
| 2 | 3 | 5 | 7 | 11 |
| 2 | 3 | 5 | 7 | 11 | 5 |
5
| 2 | 3 | 5 | 7 | 3 | 11 | 5 |
| 2 | 3 | 5 | 2 | 7 | 3 | 11 | 5 |
