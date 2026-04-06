from collections import deque
from typing import Optional, List
from student import Student

class TreeNode:
    def __init__(self, student: Student):
        self.data: Student = student
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None
 

class BinaryTree:
    def __init__(self):
        self.root: Optional[TreeNode] = None
 
    def insert(self, student: Student) -> None:
        if self.root is None:
            self.root = TreeNode(student)
        else:
            self._insert(self.root, student)
 
    def _insert(self, node: TreeNode, student: Student) -> None:
        if student.student_id < node.data.student_id:
            if node.left is None:
                node.left = TreeNode(student)
            else:
                self._insert(node.left, student)
        elif student.student_id > node.data.student_id:
            if node.right is None:
                node.right = TreeNode(student)
            else:
                self._insert(node.right, student)
        else:
            print(f"  [!] Квиток #{student.student_id} вже існує — пропущено.")
 
    def bfs_traversal(self) -> List[TreeNode]:
        result = []
        if self.root is None:
            return result
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            result.append(node)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result
 
    def print_tree(self, title: str = "Вміст дерева") -> None:
        nodes = self.bfs_traversal()
        line = "─" * 63
        print(f"\n{'═' * 63}")
        print(f"  {title}")
        print(f"{'═' * 63}")
        if not nodes:
            print("  (дерево порожнє)")
        else:
            imya = "Ім'я"
            print(f"  {'Квиток':<10} {'Прізвище':<15} {imya:<12}"
                  f" {'Курс':<7} Армія")
            print(f"  {line}")
            for node in nodes:
                print(node.data)
        print(f"{'═' * 63}\n")
 
    def _find_by_criteria(self, node: Optional[TreeNode], course: int, served: bool, result: List[Student]) -> None:
        if node is None:
            return
        if node.data.course == course and node.data.served_in_army == served:
            result.append(node.data)
        self._find_by_criteria(node.left, course, served, result)
        self._find_by_criteria(node.right, course, served, result)
 

    def delete_by_criteria(self, course: int = 5, served: bool = True) -> int:
        targets: List[Student] = []
        self._find_by_criteria(self.root, course, served, targets)
        count = len(targets)
        for student in targets:
            self.root = self._delete_node(self.root, student.student_id)
        return count
 
    def _delete_node(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if node is None:
            return None
        if key < node.data.student_id:
            node.left = self._delete_node(node.left, key)
        elif key > node.data.student_id:
            node.right = self._delete_node(node.right, key)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                successor = self._find_min(node.right)
                node.data = successor.data
                node.right = self._delete_node(node.right, successor.data.student_id)
        return node
 
    def _find_min(self, node: TreeNode) -> TreeNode:
        while node.left is not None:
            node = node.left
        return node
    
    def print_tree_visual(self, title: str = "Візуальна структура") -> None:
        print(f"\n{'═' * 63}")
        print(f"  {title}")
        print(f"{'═' * 63}")
        if self.root is None:
            print("  (дерево порожнє)")
        else:
            self._print_visual_recursive(self.root, prefix="", is_left=True, is_root=True)
        print(f"{'═' * 63}\n")

    def _print_visual_recursive(self, node: TreeNode, prefix: str, is_left: bool, is_root: bool) -> None:
        if node is None:
            return

        if node.right:
            new_prefix = prefix + ("│  " if is_left and not is_root else "   ")
            self._print_visual_recursive(node.right, new_prefix, False, False)

        connector = ""
        if is_root:
            connector = "────› [Root] " # Корінь має спеціальну стрілочку
        elif is_left:
            connector = prefix + "└───› (L) " # Лівий нащадок 
        else:
            connector = prefix + "┌───› (R) " # Правий нащадок 

        data_str = f"[#{node.data.student_id}] {node.data.last_name}"
        print(f"  {connector}{data_str}")

        if node.left:
            new_prefix = prefix + ("   " if is_left or is_root else "│  ")
            self._print_visual_recursive(node.left, new_prefix, True, False)