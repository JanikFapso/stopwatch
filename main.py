import time

csv_file = open("data.csv", "w")

def stopwatch():
    times = ""

    while True:
        input1 = input("Press Enter to start the stopwatch")
        if input1 == "q":
            break
        start_time = time.time()

        input2 = input("Press Enter to stop the stopwatch")
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")

        times = times + str(round(elapsed_time, 2)) + ", "

        if input2 == "q":
            break

    times = times[:-2]
    print(times)
    csv_file.write(times)
    csv_file.close()

stopwatch()