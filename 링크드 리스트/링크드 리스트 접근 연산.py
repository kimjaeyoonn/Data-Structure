class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스


class LinkedList:
    """링크드 리스트 클래스"""
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드, 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
            
        return iterator
    
    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)


        if self.head is None:    # 링크드 리스트가 비어있는 경우
            self.head = new_node
            self.tail = new_node
        else:    # 링크드 리스트가 비어있지 않은 경우
            self.tail.next = new_node
            self.tail = new_node


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
print(my_list)


# 링크드 리스트 노드에 접근(데이터 가져오기)
print(my_list.find_node_at(3).data)


# 링크드 리스트 노드에 접근 (데이터 바꾸기)
my_list.find_node_at(2).data = 13


#전체 링크드 리스트 출력
print(my_list)



실행결과
| 2 | 3 | 5 | 7 | 11 |
7
| 2 | 3 | 13 | 7 | 11 |
