import json
from pathlib import Path
from BLL.dorm import DormRoom

class DormData:
    def __init__(self, filename='DAL/data/dorm.json'):
        self.file = Path(filename)
        self.file.parent.mkdir(parents=True, exist_ok=True)

    def load_all(self):
        if not self.file.exists():
            return []

        with self.file.open('r', encoding='utf-8') as f:
            raw = json.load(f)

        rooms = []
        for d in raw:
            room = DormRoom(
                dorm_number=d['dorm_number'],
                room_number=d['room_number'],
                max_capacity=d['max_capacity']
            )
            for sid in d.get('students', []):
                room.add_student(sid)

            rooms.append(room)

        return rooms

    def save_all(self, rooms):
        raw = []
        for r in rooms:
            raw.append({
                'dorm_number': r.dorm_number,
                'room_number': r.room_number,
                'max_capacity': r.max_capacity,
                'students': r.students
            })

        with self.file.open('w', encoding='utf-8') as f:
            json.dump(raw, f, ensure_ascii=False, indent=4)