##########################################################################################################################
##  Google foobar - 2.1 - zombit_monitoring.py
##
##  Created by Vikas Wadhwa  http://www.wadhwa-media.com
##########################################################################################################################

##########################################################################################################################
## INSTRUCTIONS
#
# Zombit monitoring
# =================
# 
# The first successfully created zombit specimen, Dolly the Zombit, needs constant monitoring, and Professor Boolean has tasked the minions with it. Any minion who monitors the zombit records the start and end times of their shifts. However, those minions, they are a bit disorganized: there may be times when multiple minions are monitoring the zombit, and times when there are none!
# 
# That's fine, Professor Boolean thinks, one can always hire more minions... Besides, Professor Boolean can at least figure out the total amount of time that Dolly the Zombit was monitored. He has entrusted you, another one of his trusty minions, to do just that. Are you up to the task?
# 
# Write a function answer(intervals) that takes a list of pairs [start, end] and returns the total amount of time that Dolly the Zombit was monitored by at least one minion. Each [start, end] pair represents the times when a minion started and finished monitoring the zombit. All values will be positive integers no greater than 2^30 - 1. You will always have end > start for each interval.
# 
# Languages
# =========
# 
# To provide a Python solution, edit solution.py
# To provide a Java solution, edit solution.java
# 
# Test cases
# ==========
# 
# Inputs:
#     (int) intervals = [[1, 3], [3, 6]]
# Output:
#     (int) 5
# 
# Inputs:
#     (int) intervals = [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
# Output:
#     (int) 16
##########################################################################################################################
 
    
    
def answer(intervals):
    
    
    #test case input: [[10, 14], [4, 18], [19, 20], [19, 20], [13, 20]]
    
    ####################################################################################################################
    ## Sort the input so that we start with the lowest start time
    ####################################################################################################################
    intervals = sorted(intervals)
    monitored_segments = [intervals[0]]
    
    ####################################################################################################################
    ## For comparison, take the first monitored segment and extend start/end times based on the next intervals
    ## If an interval is below/above the monitored segment, add the interval as a new monitored segment.
    ####################################################################################################################
    for interval in intervals:
        
        
        ####################################################################################################################
        # Set new_segment to None here. 
        # If it is ever false, meaning an interval is found to overlap another segment, 
        # that interval will not be marked as a new monitored segment.
        ####################################################################################################################
        new_segment = None
        
        for monitored_segment in monitored_segments:

            ####################################################################################################################
            # if an interval end is before current segment start, 
            # or if an interval start is after current segment end,
            # add interval as a new monitored segment
            ####################################################################################################################
            if new_segment is None and (interval[1] < monitored_segment[0]) or (interval[0] > monitored_segment[1]):
                new_segment = True


            else: 
                new_segment = False
                                
                ####################################################################################################################
                # if an interval start is before current segment start, and ends equal to or after current segment start, 
                # lower current segment start to new interval start
                ####################################################################################################################
                if interval[0] < monitored_segment[0] and interval[1] >= monitored_segment[0]:
                    monitored_segment[0] = interval[0]  

                ####################################################################################################################
                # if an interval start is after or equal to current segment start, and interval end is after current segment end, 
                # increase current segment end to new interval end.
                #
                # if an interval start is equal to current segment end, increase current segment end to new interval end.
                ####################################################################################################################   
                if (interval[0] >= monitored_segment[0] and interval[1] >= monitored_segment[1]) or interval[0] == monitored_segment[1]:
                    monitored_segment[1] = interval[1]

                
        ####################################################################################################################
        # Only add a new monitored segment if it didn't overlap anything else.
        ####################################################################################################################
        if new_segment:
            monitored_segments.append(interval)
            
        
    total_duration = 0
    
    ####################################################################################################################
    # Add up all the monitored segment times and return the result
    ####################################################################################################################
    for segment in monitored_segments:
        duration = segment[1] - segment[0]
        total_duration += duration
    
    return total_duration

    
    
    
   
   