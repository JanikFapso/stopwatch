import time

csv_file = open("data.csv", "w")

def stopwatch():
    rosta_times = ""
    janik_times = ""
    counter = 0

    while True:
        input1 = input("Press Enter to start the stopwatch")
        if input1 == "q":
            break
        start_time = time.time()

        input2 = input("Press Enter to stop the stopwatch")
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")

        if counter <= 1:
            rosta_times = rosta_times + str(round(elapsed_time, 2)) + ", "
            counter += 1
            
            if input2 == "q":
                break

            continue

        if counter == 2 or counter == 3:
            janik_times = janik_times + str(round(elapsed_time, 2)) + ", "
            counter += 1
            
        if counter == 4:
            counter = 0

        if input2 == "q":
            break

    rosta_times = rosta_times[:-2]
    janik_times = janik_times[:-2]
    print(f"Rosta times: {rosta_times}")
    print(f"Janik times: {janik_times}")
    csv_file.write(f"{rosta_times}\n{janik_times}")
    csv_file.close()

stopwatch()