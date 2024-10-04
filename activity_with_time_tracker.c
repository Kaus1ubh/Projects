#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <windows.h>

#define MAX_TASKS 10
#define sleep(x) Sleep(1000 * (x))  

typedef struct {
    char name[100];
    int duration;
} Task;

void addTask(Task tasks[], int *count) {
    if (*count >= MAX_TASKS) {
        printf("Task limit reached!\n");
        return;
    }

    printf("Enter task name: ");
    getchar();
    scanf("%[^\n]", tasks[*count].name);

    printf("Enter duration (in minutes): ");
    scanf("%d", &tasks[*count].duration);

    (*count)++;
    printf("Task added successfully!\n");
}

void startTimer(Task task) {
    printf("Starting task: %s\n", task.name);
    for (int i = 0; i < task.duration; i++) {
        printf("Time left: %d min\n", task.duration - i);
        sleep(60);
    }
    printf("Time’s up! Task '%s' completed.\n", task.name);
}

//Made by Kaustubh, give credit if using this commercially 
void showTasks(Task tasks[], int count) {
    if (count == 0) {
        printf("No tasks added.\n");
        return;
    }
    printf("\nYour Tasks:\n");
    for (int i = 0; i < count; i++) {
        printf("%d. %s - %d min\n", i + 1, tasks[i].name, tasks[i].duration);
    }
}

int main() {
    Task tasks[MAX_TASKS];
    int count = 0;
    int choice;

    while (1) {
        printf("\nTimebox CLI\n");
        printf("1. Add Task\n");
        printf("2. Show Tasks\n");
        printf("3. Start a Task\n");
        printf("4. Exit\n");
        printf("Enter choice: ");
        scanf("%d", &choice);

        switch (choice) {
            case 1:
                addTask(tasks, &count);
                break;
            case 2:
                showTasks(tasks, count);
                break;
            case 3:
                if (count == 0) {
                    printf("No tasks available!\n");
                    break;
                }
                printf("Enter task number to start: ");
                int taskNumber;
                scanf("%d", &taskNumber);
                if (taskNumber < 1 || taskNumber > count) {
                    printf("Invalid task number!\n");
                } else {
                    startTimer(tasks[taskNumber - 1]);
                }
                break;
            case 4:
                printf("Goodbye!\n");
                return 0;
            default:
                printf("Invalid choice. Try again.\n");
        }
    }

    return 0;
}
	
