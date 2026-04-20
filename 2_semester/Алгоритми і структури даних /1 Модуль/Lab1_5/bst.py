from collections import deque
from student import Student
 
class BSTNode:
    def __init__(self, student: Student):
        self.student = student
        self.key = student.birth_key()
        self.left:  "BSTNode | None" = None
        self.right: "BSTNode | None" = None


class BST:
    def __init__(self):
        self.root: BSTNode | None = None

    def rotate_left(self, node: BSTNode) -> BSTNode:
        if node.right is None:
            raise ValueError("rotate_left: правий нащадок відсутній.")
        right = node.right
        node.right = right.left
        right.left = node
        return right
    
    def rotate_right(self, node: BSTNode) -> BSTNode:
        if node.left is None:
            raise ValueError("rotate_right: лівий нащадок відсутній.")
        left = node.left
        node.left = left.right
        left.right = node
        return left
    
    def _insert_as_root(self, node: BSTNode | None, new_node: BSTNode) -> BSTNode:
        if node is None:
            return new_node
        if new_node.key < node.key:
            node.left = self._insert_as_root(node.left, new_node)
            node = self.rotate_right(node)
        else:
            node.right = self._insert_as_root(node.right, new_node)
            node = self.rotate_left(node)
        return node
    
    def _tree_to_vine(self) -> tuple[BSTNode, int]:
        pseudo = BSTNode.__new__(BSTNode)
        pseudo.left = None
        pseudo.right = self.root
        pseudo.student = None  
        pseudo.key = -1
 
        tail = pseudo
        rest = tail.right
        size = 0
        while rest:
            if rest.left is None:
                tail  = rest
                rest  = rest.right
                size += 1
            else:
                tmp = rest.left
                rest.left = tmp.right
                tmp.right = rest
                tail.right = tmp
                rest = tmp
        return pseudo, size
    
    @staticmethod
    def _compress(root: BSTNode, count: int):
        scanner = root
        for _ in range(count):
            child = scanner.right
            scanner.right = child.right
            scanner = scanner.right
            child.right = scanner.left
            scanner.left = child
 
    @staticmethod
    def _floor_log2(n: int) -> int:
        r = 0
        while n >= 2:
            n >>= 1
            r += 1
        return r

    def _dsw_balance(self):
        pseudo, size = self._tree_to_vine()
        if size <= 2:
            self.root = pseudo.right
            return
        m = (1 << self._floor_log2(size + 1)) - 1
        self._compress(pseudo, size - m)
        while m > 1:
            m >>= 1
            self._compress(pseudo, m)
        self.root = pseudo.right

    def insert(self, student: Student) -> None:
        new_node  = BSTNode(student)
        self.root = self._insert_as_root(self.root, new_node)
        self._dsw_balance()
        print(f"\n  [+] [{new_node.key}] "
              f"{student.last_name} {student.birth_str()} / {student.hobby}")
        self._print_bfs_inline()

    def search(self, key: int) -> BSTNode | None:
        current = self.root
        steps = 0
        while current:
            steps += 1
            if key == current.key:
                print(f"      → знайдено за {steps} крок(ів).")
                return current
            current = current.left if key < current.key else current.right
        print(f"      → не знайдено (перевірено {steps} вузл(ів)).")
        return None
    
    def _print_bfs_inline(self):
        if not self.root:
            print("      (порожнє дерево)")
            return
        queue = deque([(self.root, 0)])
        level, buf = 0, []
        print("      BFS: ", end="")
        while queue:
            node, lvl = queue.popleft()
            if lvl != level:
                print("  │  ".join(buf))
                print("           ", end="")
                buf, level = [], lvl
            buf.append(f"[{node.key}]{node.student.last_name}")
            if node.left:
                queue.append((node.left,  lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))
        if buf:
            print("  │  ".join(buf))

    def print_bfs_full(self, title: str = ""):
        W = 74
        if title:
            print(f"\n{'─'*W}\n  {title}\n{'─'*W}")
        if not self.root:
            print("  (порожнє дерево)")
            return
        print(f"  {'№':<4} {'Рів.':<6} {'Ключ':<12} Студент")
        print(f"  {'─'*(W-2)}")
        queue = deque([(self.root, 0)])
        i = 1
        while queue:
            node, lvl = queue.popleft()
            print(f"  {i:<4} {lvl:<6} {node.key:<12} {node.student}")
            i += 1
            if node.left:
                queue.append((node.left,  lvl + 1))
            if node.right:
                queue.append((node.right, lvl + 1))
        print(f"{'─'*W}")


 