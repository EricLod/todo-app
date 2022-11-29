count = ""

with open("counts.txt", "w") as file:
    file.writelines(count)

while True:
    user_action = input("Throw the coin and enter head or tail here: ? ")
    heads = 0
    tails = 0

    match user_action:
        case "head":

            with open("counts.txt") as file:
                count = file.readlines()

            count.append("head\n")

            with open("counts.txt", "w") as file:
                file.writelines(count)

            with open("counts.txt") as file:
                count = file.readlines()

            for item in count:
                item = item.strip("\n")
                if item == "head":
                    heads += 1
                if item == "tail":
                    tails += 1

            percent = str((heads/(heads+tails))*100) + "%"
            print(f"Heads: {percent}")

        case "tail":

            with open("counts.txt") as file:
                count = file.readlines()

            count.append("tail\n")

            with open("counts.txt", "w") as file:
                file.writelines(count)

            with open("counts.txt") as file:
                count = file.readlines()

            for item in count:
                item = item.strip("\n")
                if item == "head":
                    heads += 1
                if item == "tail":
                    tails += 1

            percent = str((heads / (heads + tails)) * 100) + "%"
            print(f"Heads: {percent}")

        case "exit":
            print("Cheers!")
            break