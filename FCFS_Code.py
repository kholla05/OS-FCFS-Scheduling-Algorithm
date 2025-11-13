pids = ["P1", "P2", "P3", "P4"]
arrival = [0, 3, 7, 12]
burst = [5, 4, 9, 8]

time = 0
total_wait = total_turn = total_resp = 0
n = len(pids)

for i in range(n):
    if time < arrival[i]:
        time = arrival[i]
    wait = time - arrival[i]
    resp = wait
    done = time + burst[i]
    turn = done - arrival[i]

    total_wait += wait
    total_resp += resp
    total_turn += turn
    time = done

print("Average wait:", round(total_wait / n, 2))
print("Average turnaround:", round(total_turn / n, 2))
print("Average response:", round(total_resp / n, 2))
print("Throughput:", round(n / time, 3))
