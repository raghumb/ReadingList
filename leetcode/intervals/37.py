# find the minimum number of meeting rooms required to accommodate all meetings without conflicts.


def minMeetingRooms(intervals):
    starts = sorted(interval[0] for interval in intervals)
    ends = sorted(interval[1] for interval in intervals)

    rooms = 0
    end_ptr = 0

    for start in starts:
        if start < ends[end_ptr]:
            # A meeting is still running, need a new room
            rooms += 1
        else:
            # A room is available, reuse it
            end_ptr += 1

    return rooms


# Hardcoded input
intervals = [[0, 30], [5, 10], [15, 20]]

print("Minimum rooms required:", minMeetingRooms(intervals))

