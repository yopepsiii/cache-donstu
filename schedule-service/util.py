from proto.gen.schedule.schedule_pb2 import Lesson
from google.protobuf.json_format import ParseDict

def convert_dict_to_lesson(json_data):
    lesson = Lesson()
    ParseDict(json_data, lesson, ignore_unknown_fields=True)
    return lesson