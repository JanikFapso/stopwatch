import time

csv_file = open("data.csv", "w")

def stopwatch():
    rosta_times = ""
    janik_times = ""

    while True:
        for i in range(2):
            input1 = input("Press Enter to start the stopwatch")
            if input1 == "q":
                break
            start_time = time.time()

            input2 = input("Press Enter to stop the stopwatch")
            end_time = time.time()
            
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")

            rosta_times = rosta_times + str(round(elapsed_time, 2)) + ", "
       
            if input2 == "q":
                break

        if input1 or input2 == "q": 
            break

        for i in range(2):
            input1 = input("Press Enter to start the stopwatch")
            if input1 == "q":
                break
            start_time = time.time()

            input2 = input("Press Enter to stop the stopwatch")
            end_time = time.time()
            
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")

            janik_times = janik_times + str(round(elapsed_time, 2)) + ", "

            if input2 == "q":
                break

        if input1 or input2 == "q": 
            break

    rosta_times = rosta_times[:-2]
    janik_times = janik_times[:-2]
    print(rosta_times)
    print(janik_times)
    csv_file.write(f"{rosta_times}\n{janik_times}")
    csv_file.close()

stopwatch()
