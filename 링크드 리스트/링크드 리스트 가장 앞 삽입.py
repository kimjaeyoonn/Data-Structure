class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data  # 실제 노드가 저장하는 데이터
        self.next = None  # 다음 노드에 대한 레퍼런스

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드
      
    def prepend(self, data):    # 주요 메소드 !!
        new_node = Node(data)
        if self.head is None:
            self.head = new_node   
            self.tail = new_node   
        else:
            new_node.next = self.head     # 1.new node의 next에는 무엇이 들어가야할까요?
            self.head = new_node          # 2.self.head에는 어떤 값이 들어있나요?
            
    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)
        
        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def __str__(self):
        """링크드  리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:    # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += " {} |".format(iterator.data)
            iterator = iterator.next# 다음 노드로 넘어간다
        return res_str
    
    
my_list = LinkedList()    # 새로운 링크드 리스트 생성

my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)
print(my_list)
my_list.prepend(2) 

print(my_list.head.data)
print(my_list.tail.data)
