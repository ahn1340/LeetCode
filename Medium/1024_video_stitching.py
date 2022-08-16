class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips = sorted(clips)
        start = clips[0][0]
        d = {start: []}
        for clip in clips:
            if clip[0] == start:
                d[start].append(clip)
            else:
                start = clip[0]
                d[start] = [clip]

        t = 0
        best = [0, 0]
        updated = False
        count = 0
        for k, v in d.items():
            if best[1] >= time:
                break
            if k > t:
                if best[1] < k:  # no overlap
                    return -1
                else:
                    if updated:
                        count += 1
                        updated = False
                    t = best[1]
            if best[1] < v[-1][1]:
                updated = True
                best = v[-1]
        if updated:
            count += 1
        
        
        if best[1] < time:
            return -1
        else:
            return count
          
"""
Store each clip in dict, where key: start time, value: sorted list of clips where clip[0] == key.
Then, greedily stitch clips with biggest end time.
Time: O(nlogn), where n = number of clips. Space: O(n) for storing clips in dict.
"""
