# группируем временные метки по 2 в подсписки - [время входа, время выхода]
def get_ranges(timestamps: list[int]):
    timestamps = [timestamps[i:i + 2] for i in range(0, len(timestamps), 2)]
    return sorted(timestamps)

# объединение множеств: объединяем временные пересечения
def merge_ranges(timestamps: list[[int, int]]):
    # результирующий массив
    merged_timestamps = []
    if timestamps:
        previous_timestamp_start, previous_timestamp_end = timestamps[0]
        for current_timestamp_start, current_timestamp_end in timestamps[1:]:
            # если диапазон возможно объединить с предыдущим
            if current_timestamp_start <= previous_timestamp_end:
                previous_timestamp_end = max(current_timestamp_end, previous_timestamp_end)
            # если нельзя
            else:
                merged_timestamps.append((previous_timestamp_start, previous_timestamp_end))
                previous_timestamp_start, previous_timestamp_end = current_timestamp_start, current_timestamp_end
        merged_timestamps.append((previous_timestamp_start, previous_timestamp_end))
    return merged_timestamps

# ищем пересечения во времени
def find_joints(interval1: list[[int, int]], interval2: list[[int, int]]):
    intersections = []
    for i in interval1:
        for j in interval2:
            max_timestamp_start = max(i[0], j[0])
            min_timestamp_end = min(i[1], j[1])
            if max_timestamp_start < min_timestamp_end:
                intersections.append([max_timestamp_start, min_timestamp_end])
    return intersections


def appearance(intervals: dict[str, list[int]]) -> int:
    # объединенные временные интервалы для урока и пользователей
    lesson_ranges = merge_ranges(get_ranges(intervals['lesson']))
    tutor_ranges = merge_ranges(get_ranges(intervals['tutor']))
    pupil_ranges = merge_ranges(get_ranges(intervals['pupil']))

    # пересечение во времени ученика и учителя
    pupil_tutor_intersections = find_joints(pupil_ranges, tutor_ranges)
    # пересечение во времени урока и пользователей (ученика и учителя)
    lesson_users_intersection = find_joints(lesson_ranges, pupil_tutor_intersections)

    # подсчет общего времени на уроке
    result = sum(timestamp_end - timestamp_start for timestamp_start, timestamp_end in lesson_users_intersection)
    return result