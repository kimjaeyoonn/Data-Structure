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
            self
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node        

    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정"""
        iterator = self.head
        for _ in range(index):
            iterator = iterator.next
        return iterator
    

    def delete(self, node_to_delete):    # 주요 메소드 ! (이해가 너무 어렵다. 다시 볼 것.)
        data = node_to_delete.data

        if node_to_delete.prev is None and node_to_delete.next is None:    # 마지막 남은 노드 삭제
            self.head = None
            self.tail = None
        elif node_to_delete is self.head:   # head 노드 삭제
            self.head = node_to_delete.next
            node_to_delete.next.prev = None
        elif self.tail is node_to_delete:    # tail 노드 삭제
            self.tail = node_to_delete.prev
            node_to_delete.prev.next = None
        else:    # 두 노드 사이의 노드를 삭제
            node_to_delete.prev.next = node_to_delete.next    # node_to_delete의 전 노드의 다음 노드가 node_to_delete의 다음 노드를 가르키게 함.
            node_to_delete.next.prev = node_to_delete.prev    # node_to_delete의 다음 노드의 전 노드가 node_to_delete의 전 노드를 가르키게 함.

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
print(my_list)


node_1 = my_list.find_node_at(2)   
my_list.delete(node_1) 
print(my_list)

node_2 = my_list.find_node_at(0)
print(my_list.delete(node_2))

print(my_list)

node_3 = my_list.find_node_at(1)
my_list.delete(node_3)
print(my_list)

node_4 = my_list.find_node_at(0)
my_list.delete(node_4)
print(my_list)



실행 결과
| 2 | 3 | 5 | 7 |
| 2 | 3 | 7 |
2
| 3 | 7 |
| 3 |
|

