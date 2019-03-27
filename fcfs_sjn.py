#This program simulates the FCFS algorithm and the Shortest Job Next Algorithm
#The SJN program sorts the jobs by size before processing.



#Function to find waiting time of each job being processes

def findWaitingTime(job_list, wt): 
  
    # waiting time for first job is 0  
    wt[0] = 0
  
    # calculating waiting time 
    for i in range(1, len(job_list) ): 
        wt[i] = job_list[i - 1][2] + wt[i - 1]  
  


# Calculate turnaround time
def findTurnAroundTime(job_list, wt, tat): 
  
    # calculating turnaround  
    # time by adding cpu cycles + wait time of each job 
    for i in range(len(job_list)): 
        tat[i] = job_list[i][2] + wt[i] 
  
# Function to calculate average time 
 
def findavgTime(job_list): 
  
    wt = [0] * len(job_list) 
    tat = [0] * len(job_list)  
    total_wt = 0
    total_tat = 0
  
    # Calls function to find waiting  
    # time of all jobs 
    findWaitingTime(job_list, wt) 
  
    # Calls function to find turn around  
    # time for all jobs 
    findTurnAroundTime(job_list, wt, tat) 
  
    # Print job information with wait times and turnaround times 
    print( "Job Num \t" +
           "CPU time\t" + 
            " Waiting Time\t" + 
            " Turnaround Time") 
  
    # Calculate total waiting time and total turn around time  

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
      
    #job_list=[[1,0,5],[2,1,2],[3,3,6],[4,4,4]]
    job_list=[[1,0,6],[2,3,2],[3,5,1],
             [4,9,7],[5,10,5],[6,12,3],
             [7,14,4],[8,16,5],[9,17,7],
             [10,19,2]]

    print("First-Come,First-Served Algorithm")
    findavgTime(job_list)

    print()
    print("Shortest Job Next Algorithm")
    findavgTime(sorted(job_list, key=lambda x:x[2]))

    
        
  
