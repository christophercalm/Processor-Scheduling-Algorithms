#My attempt at round robin



def findWaitingTime(job_list, wt, quantum):  
    rem_cpu_time = [0] * len(job_list) 
  
    # Copy the cpu cycle time into rt[]  
    for i in range(len(job_list)):  
        rem_cpu_time[i] = job_list[i][2] 
    
    time = 0 # Currentime time  
  
    # Keep traversing processes in round  
    # robin manner until all of them are 
    # not done.  
    while(1): 
        done = True
  
        # Traverse all processes one by 
        # one repeatedly  
        for i in range(len(job_list)): 
              
            # If burst time of a process is greater  
            # than 0 then only need to process further  
            if (rem_cpu_time[i] > 0) : 
                done = False # There is a pending process 
                  
                if (rem_cpu_time[i] > quantum) : 
                  
                    # Increase the value of t i.e. shows  
                    # how much time a process has been processed  
                    time += quantum  
  
                    # Decrease the burst_time of current  
                    # process by quantum  
                    rem_cpu_time[i] -= quantum  
                  
                # If burst time is smaller than or equal   
                # to quantum. Last cycle for this process  
                else: 
                  
                    # Increase the value of t i.e. shows  
                    # how much time a process has been processed  
                    time += rem_cpu_time[i]  
  
                    # Waiting time is current time minus  
                    # time used by this process  
                    wt[i] = time - job_list[i][2]  
  
                    # As the process gets fully executed  
                    # make its remaining burst time = 0  
                    rem_cpu_time[i] = 0
                  
        # If all processes are done  
        if (done == True): 
            break
              
# Calculate turnaround time
def findTurnAroundTime(job_list, wt, tat): 
  
    # calculating turnaround  
    # time by adding bt[i] + wt[i] 
    for i in range(len(job_list)): 
        tat[i] = job_list[i][2] + wt[i] 

def findavgTime(job_list,quantum): 
  
    wt = [0] * len(job_list) 
    tat = [0] * len(job_list)  
    total_wt = 0
    total_tat = 0
  
    # Function to find waiting  
    # time of all processes 
    findWaitingTime(job_list, wt, quantum) 
  
    # Function to find turn around  
    # time for all processes 
    findTurnAroundTime(job_list, wt, tat) 
  
    # Print job information with Wait and turnaround times 
    print( "Job Num \t" +
           "CPU time\t" + 
            " Waiting Time\t" + 
            " Turnaround Time") 
  
    # Calculate total waiting time  
    # and total turn around time 
    for i in range(len(job_list)): 
      
        total_wt = total_wt + wt[i] 
        total_tat = total_tat + tat[i] 
        print("  " + str(job_list[i][0]) + "\t\t  " + 
                    str(job_list[i][2]) + "\t\t   " + 
                    str(wt[i]) + "\t\t\t" + 
                    str(tat[i]))  
  
    print( "Average waiting time = "+
                   str(total_wt / len(job_list))) 
    print("Average turn around time = "+
                     str(total_tat / len(job_list))) 
    

# Driver code 
if __name__ =="__main__": 
      
    job_list=[[1,0,3],[2,0,4],[3,0,3]]
    #job_list=[[1,0,6],[2,3,2],[3,5,1],
#             [4,9,7],[5,10,5],[6,12,3],
#             [7,14,4],[8,16,5],[9,17,7],
#           [10,19,2]]
    quantum = 1

    print("Round Robin Algorithm")
    print("Quanum time is:",quantum)
    findavgTime(job_list,quantum)

    
    
    
