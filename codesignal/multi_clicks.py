"""Medium

Codewriting

3000

The Asana center pane contains a list of tasks. These tasks are placed within rectangular blocks of size height × width, which are stacked on top of each other, and there are empty stripes of size yOffset × width left between each two consecutive blocks.

Asana lets you use a simple click and drag motion to select multiple tasks - i.e., you can click on the first task in your desired selection, then drag the mouse to the last task in your desired selection. The selected tasks can be visualized as follows: If you join the initial and the final positions of the mouse by a line, every task block that has at least one point in common with this line is considered to be "selected".

To test your skills, Asana engineers want you to implement a function that determines which tasks are selected based on the initial and final positions of the mouse.

Example

For
dimensions = [135, 9, 1],

tasks = ["Task 1", "Task 2", "Task 3", "Very Important Task",
         "Not So Important Task", "Yet Another Task", "The last task"],
and

mouseCoordinates = [[132, 42],
                    [35, 13]]
the output should be

multiSelection(dimensions, tasks, mouseCoordinates) =
    ["Task 2", "Task 3", "Very Important Task", "Not So Important Task"]
"Task 1" occupies the rectangle with an upper left corner at (0, 0) and a bottom right corner at (135, 9). "Task 2" is in the rectangle with corners at (0, 10) and (135, 19). The rectangle corners for the remaining tasks are as follows:

"Task 3": (0, 20), (135, 29)
"Very Important Task": (0, 30), (135, 39)
"Not So Important Task": (0, 40), (135, 49)
"Yet Another Task": (0, 50), (135, 59)
"The last task": (0, 60), (135, 69)


Input/Output

[execution time limit] 4 seconds (py3)

[input] array.integer dimensions

An array of three positive integers: [width, height, yOffset].

Guaranteed constraints:
1 ≤ dimensions[i] ≤ 106.

[input] array.string tasks

A non-empty array of strings representing the task names in top-down order as they appear in the Asana center pane.

Guaranteed constraints:
1 ≤ tasks.length ≤ 10,
1 ≤ tasks[i].length ≤ 25.

[input] array.array.integer mouseCoordinates

Mouse coordinates in the format [[x1, y1], [x2, y2]].

Guaranteed constraints:
0 ≤ x1, x2 < width,
0 ≤ y1, y2 < height · tasks.length + yOffset · (tasks.length - 1).
"""


def multiSelection(dimensions, tasks, mouseCoordinates):
    positions = []
    y_cord = 0
    for i, task in enumerate(tasks):
        positions.append([])
        positions[i].append(y_cord)
        y_cord += dimensions[1]
        positions[i].append(y_cord)
        y_cord += dimensions[2]

    positions = list(zip(positions, tasks))

    start = min(mouseCoordinates[1][1], mouseCoordinates[0][1])
    end = max(mouseCoordinates[1][1], mouseCoordinates[0][1])

    for item in positions:
        if item[0][0] <= start <= item[0][1]:
            start = tasks.index(item[1])
            break
    for item in positions:
        if item[0][0] <= end <= item[0][1]:
            end = tasks.index(item[1])+1
            break

    return tasks[start:end]


multiSelection([135, 9, 1], ["Task 1", "Task 2", "Task 3", "Very Important Task", "Not So Important Task", "Yet Another Task", "The last task"], [[132, 42], [35, 13]])